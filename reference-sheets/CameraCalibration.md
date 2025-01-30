# Contents
- [Environment setup](#environment-setup)
- [Video Recording](#video-recording)
- [Command Crusades](#command-crusades)
- [Quick Overview](#quick-overview)

This guide provides a simpler, more direct approach to camera calibration. For a more comprehensive guide that covers everything in detail, refer to [this guide](https://mrcal.secretsauce.net/how-to-calibrate.html).

# Environment setup
To get started with camera calibration, you will need to set up your environment. Follow these steps:

1. **Download Ubuntu**: You will need to have Ubuntu installed on your system. You can download it from [here](https://ubuntu.com/download/desktop). Follow the instructions on the website to install it on your machine.

    - After it has been downloaded and setup, run this command to get mrcal setup for future usage: `apt install mrcal libmrcal-dev python3-mrcal`

2. **Troubleshooting Installation Issues**: If this is your first time installing Ubuntu, you might encounter some issues. Don't worry! Simply search for solutions online. There are plenty of resources and forums where you can find simple solutions to common problems.
3. **Installing Dependencies**: Throughout this process, you might not have all the necessary dependencies installed. If you run a command and it prompts you to install something, just go ahead and install it. This is a normal part of setting up your environment.

# Video Recording
To record the video for calibration, follow these steps:

1. **Download OBS**: You will need OBS Studio to record your video. Download it from [here](https://obsproject.com/). Follow the installation instructions on the website.
2. **OBS Setup**:
   - **Frame Rate**: Set the frame rate to 100 FPS.
   - **Output Location**: Change the output location to a new folder that you will use for this entire process.
   - **Resolution**: Set the resolution to match your camera's resolution (e.g., 1280x720).
   - **Output Format**: Ensure the video is lossless and saved in AVI format (will result in larger files).
3. **Print Chessboard Pattern**: Print the chessboard pattern from [here](https://github.com/dkogan/mrgingham/raw/master/chessboard.14x14.pdf). Make sure it is centered and fills up the whole page. When recording the video, the chessboard pattern must be on a flat surface, ideally taped down.
4. **Recording the Video**:
   - **Example Video**: Here is an example of a good video for reference: [Calibration Video Example](https://www.youtube.com/watch?v=ez_5TA_SDto).
   - **Setup**: Hold the chessboard in front of the camera, not too far away or too close, and focus the camera on the pattern. Once it looks very clear, start recording.
   - **Coverage**: Move the chessboard to cover all areas of the frame at different distances and angles. The entire chessboard must stay in the frame the whole time. Any frame that doesn't have the full chessboard will not be used.
   - **Angles**: Slightly wave and rotate the board to capture different angles. Pay special attention to the corners by moving the board around each corner while being a bit further away from the camera. This usually results in better corner coverage.
   - **Duration**: The ideal video length is around 1:30 to 1:45 minutes, with a maximum of 2 minutes.

# Command Crusades
After recording the video and saving it in the designated folder, follow these steps to process the video frames and generate the necessary files for calibration:

1. **Split Video into Frames**:
   - Using Ubuntu, navigate to the folder containing your video file.
   - Run the following command to split the video into individual PNG frames:
     ```
     ffmpeg -i input.avi %04d.JPG
     ```
   - Note: This process will take some time, depending on the length of the video and your system's performance.
   - Once the frames are generated, delete the original video file from the folder to save space.

2. **Generate Corners File**:
   - Run the following command to detect the chessboard corners in the frames and generate a `corners.vnl` file:
     ```sh
     mrgingham --jobs 4 --gridn 14 '*.JPG' > corners.vnl
     ```
   - This process will also take some time but will result in a `corners.vnl` file that we can use to evaluate the coverage of the calibration frames.

3. **Visualize Corners Coverage**:
   - Run the following command to visualize the corners coverage:
     ```sh
     < corners.vnl \
     vnl-filter -p x,y | \
     feedgnuplot --domain --square --set 'xrange [0:HORIZONTALRES] noextend' --set 'yrange [VERTICALRES:0] noextend'
     ```
   - Replace `HORIZONTALRES` and `VERTICALRES` with your video's resolution. For example, if your resolution is 1280x720, the command would be:
     ```sh
     < corners.vnl \
     vnl-filter -p x,y | \
     feedgnuplot --domain --square --set 'xrange [0:1280] noextend' --set 'yrange [720:0] noextend'
     ```
   - The screen should show purple areas in a graph representing your coverage. Here is an example of what good coverage should look like: [Good Coverage Example](https://www.chiefdelphi.com/uploads/default/original/3X/5/f/5f7f3a3729081426a83c6749b8e1705076b898c4.png).

4. **Calculate Focal Length**:
   - Once you have coverage you are happy with, you need to calculate the focal length of your camera since it is needed for the calibration.
   - **Note**: IVAN DO IT. (I forgor)

5. **Run Calibration**:
   - Run the following command to calibrate the camera:
     ```sh
     mrcal-calibrate-cameras \
     --corners-cache corners.vnl \
     --lensmodel LENSMODEL_OPENCV8 \
     --focal FOCAL HERE \
     --object-spacing 0.0588 \
     --object-width-n 14 \
     '*.JPG'
     ```
   - Replace `FOCAL HERE` with your calculated focal length.

6. **Show Projection Uncertainty**:
   - Run the following command to visualize the projection uncertainty:
     ```sh
     mrcal-show-projection-uncertainty opencv8.cameramodel --cbmax 0.5 --unset key
     ```
   - This will show values on your coverage, indicating uncertainties. You want really low/dark purple in the most middle areas and blue/0.2-0.3 range in your corners. This means good certainty because it is only struggling with the harder areas to get good coverage with, the deep corners. Lower the number the better.

7. **Convert Camera Model to JSON**:
   - Once the graph looks right and makes sense, convert the mrcal `.cameramodel` file to a JSON file.
   - You can run [this](https://www.chiefdelphi.com/uploads/short-url/tklQyeYOuxopG1xLZRCF0tlIk23.py) Python file from a command line and give it your path for the `.cameramodel` file and the path you want your new JSON file to be stored.
     ```sh
     ./file.py /path/to/cameramodel /path/to/json
     ```
    - Once json file is retrived, upload it to your robot project under `resources/calibrations/file.json`
# Conclusion
Calibrating a camera can be a learning process, especially if it's your first time. Take your time with the videos and see what works and what doesn't. Play around with different techniques and you might find a better way to get improved coverage.

**Important Note**: Be very clear and descriptive with both your files and in real life about which camera calibration belongs to which camera. Mixing them up can lead to incorrect calibrations and poor results. Label everything meticulously to avoid confusion.

Good luck with your camera calibration!

# Quick Overview
- Step 1: Record a video with the camera trying to get the calibration image to all areas of the frame at different distances and skews
- Step 2: Split it into frames (`ffmpeg -i input.avi %04d.JPG`)
- Step 3: Put those frames into a folder inside of the Ubuntu WSL instance
- Step 4: `apt install mrcal libmrcal-dev python3-mrcal`
- Step 5: Navigate into your folder with the images
- Step 6: `mrgingham --jobs 4 --gridn 14 '*.JPG' > corners.vnl`
- Step 7: `< corners.vnl vnl-filter -p x,y | feedgnuplot --domain --square --set 'xrange [0:HORIZONTALRES] noextend' --set 'yrange [VERTICALRES:0] noextend'`
- Step 8: Check you have good frame coverage
- Step 9: Calculate your focal
- Step 10: `mrcal-calibrate-cameras --corners-cache corners.vnl --lensmodel LENSMODEL_OPENCV8 --focal FOCAL HERE --object-spacing 0.0588 --object-width-n 14 '*.JPG'`
- Step 11: `mrcal-show-projection-uncertainty opencv8.cameramodel --cbmax 0.5 --unset key`
- Step 12: See if that output makes sense
- Step 13: Convert the mrcal .cameramodel file to a photonvision json and import it




