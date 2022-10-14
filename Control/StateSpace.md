# SciGuides Part 1 SysID


### Additional Info Can Be Found [Here](#https://docs.wpilib.org/en/stable/docs/software/pathplanning/system-identification/index.html)
## Table of Contents
### 1. [What is SysID?](#what-is-SysID)
### 2. [How does SysID work?](#how-does-sysid-work)
### 3. [How do you use SysID?](#how-do-you-use-sysid)
### 4. [SysID for Drivetrain](#sysid-for-drivetrain)

### What is SysID?
#### 
    SysID is a built in feature in wpilib that allows us to get values for PID 
    and Feedforward loops and is one of the first things you have to learn about 
    when learning about control theory in robotics.This As it is what allows us 
    to effectively tune PID and SVA values. For more information on PID and SVA 
    values check [insert link when made] and [insert link when made].

### How does SysID work?

#### 
    SysID works by deploying code made by the people behind wpilib that allows 
    you to run tests on your robot and collect data about your robot mechanism. 
    SysID also includes code that allows you to analyze this data where you get 
    your PID and SVA values

### How do you use SysID? (General Mechanism)
####
    1. Open SysID by typing SysID into the your search bar and if you have SysID installed you will be SysID. 
    2. Go to the generator tab and put your team number under team/IP 
    3. There are then different modes for different mechanisms we will only focus 
    on Drivetrain and general mechanism sysID right now 
    4. For the motor controller section as of 2022/2023 put the motor controller 
    as Spark Max(Brushless), set inverted if the motor is meant to be inverted and for the CAN ID just put the ID found on the Spark Max connected to the motor for the mechanism you are testing. Add extra motors with the plus if the mechanism uses more motors.
    5. In the encoder section put encoder port if you unless you are using CanCoders(if we buy them)
    6. Under encoder parameters set the gearing to whatever the gear ratio is for 
    the mechanism(if it doesnt work try to switch it around) For counts per revolution set it to the value 8192 if you are using throughbores or 1 if you are using integrated Neo encoders and look up counts per revolution if you are using another encoder.
    7. Now under logger go to project parameters for mechanism set it to the 
    mechanism you are using for example hopper is elevator intake and flywheel are under simple
    8. For unit type use whatever unit you are using and set units per rotation 
    to see the distance went for rotation and use rotation only if the mechanism is 1 to 1.
    9. Voltage Parameters, this represents the voltage applied during tests set 
    the parameter for slide the slider to whatever voltage ramp rate you want for precise or very breakable mechanisms like hood set both quasistatic low and dynamic step voltage low as well. Low Voltage also tends to be more accurate.
    10. To test on the robot plug in the laptop with the SysID setup. Set logger 
    mode to enabled click apply if NT Connected is shown to the right of it click deploy under team/ip in generator choose a save location on your computer ideally in the sysID folder in the cloned respository run all your tests. Click save now you have your data.
    11. To analyze your data go to analyzer select the sysID data from the folder 
    you stored it run the analyzer and get the Feedback and Feedforward analysis note Feedback will yield PID values and Feedforward will yield SVA values.
    12. Once you get your data now you have PID and SVA Values.

### SysID for Drivetrain
####
    4. In loggers go to motor controllers Set your motor controllers to Spark Max
     Brushless and choose which side of motors are inverted and for encoders use the encoder we are using whether it be CanCoders, Integrated Neos or whatever. Assuming we use swerve with CanCoders Invert one side of the cancoders
    5. For Gyro set the gyro to pigeon get the CAN ID and as of 2022/2023 we do 
    not have talons
    6. Encoder Parameters, the counts per revolution on a CanCoder is 4096 Counts 
    Per Revolution and Gearing is just the gear ratio of where the encoder is mounted
    7. Go to Logger and project parameters have mechanism as Drivetrain and Unit 
    Type as meters and set the Units Per Rotation as the circumfrence of the wheel
    8. Set up your voltage parameters lower values more precise values but don't 
    be afraid to go wild as long as you have a lot of space
    9. Basically follow the rest of the steps from SysID for General Mechanisms


    
