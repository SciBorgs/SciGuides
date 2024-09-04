# Introduction

This is a guide to setting up your computer. It includes instructions on organizing files locally, setting up git and Github, setting up an environment to code in Java, and setting up an environment to write robotics-specific code.
## Goals

- [Create code folder](#local-code-organization)
- [Set up git & Github](#git)
	- Make sure git is installed
	- Make Github account
	- Add PAT
- [Set up regular VSCode](#visual-studio-code-not-wpilib)
- [Set up WPILib VSCode](#wpilib)
# Local Code Organization

All of the files on your computer are organized into a tree of *directories*, or folders. When you use Finder or File Explorer, you are navigating through those directories. 

Most of the relevant files on your computer are inside of your home directory. The top level contents of your home directory include Downloads, Documents, Desktop, Applications, and other directories that you should be familiar with.

When you write code, the files that you write in will exist somewhere on your computer. For the sake of organization, you need to decide where that is.

Oftentimes, people will make one directory that contains all of their code. Within that, they might have separate directories for robotics code and other code. And then individual projects are placed inside of those directories.

Another option is to just make one directory for robotics, and if you ever want to write non-robotics code, you can make a different directory for that.

You can do whichever of those you feel more comfortable with. Or if there's another way you want to organize your code, that's fine -- as long as it's all in its own directory and not on one drive!

Next, you need to decide where you want to put your code/robotics directory. You really only have two reasonable options for this:
1. Directly in your home directory
2. Inside Documents
If you're coding a lot, I'd definitely recommend number 1. Otherwise, either way is fine.

Once you've decided how you want to organize your code on your computer, you have a couple options for how you're actually going to make the directory:
## Finder (Mac) or File Explorer (Windows)

Open Finder/File Explorer. 

If you want to put your folder in Documents, open Documents.

If you want to put your folder in the home directory, go to the home directory
- for Mac: Command + Shift + H
- for Windows: go to the location bar and enter %USERPROFILE%

Once you're in the right place, create a new folder (right click, press *new folder*). Give your folder a descriptive name, and make sure it has ***no spaces***.

Make sure your folder is easily accessible
- for Mac: drag your folder over to the sidebar
- for Windows: save your folder to quick access
## Command Line (Mac, Windows, Linux)

Open command line.
- for Mac or Linux: open Terminal
- for Windows: open PowerShell

For each of the next steps, I'm going to give you a line to write in the console that you just pulled up, and explain what it does.

Navigate to your home directory (you're probably there already by default, but this will make sure):
```
cd
```

Only if you want your directory to be in Documents:
```
cd Documents
```

Make the directory:
```
mkdir <name>
```
Replace \<name> with whatever you want your directory to be called. So if you wanted the name to be "code", you'd write `mkdir code`. Whatever you do, make sure your name has no spaces!

Lastly, I highly recommend you go to whatever file navigator you use (Finder, File Explorer, etc) and pin the folder you made so that it's easily accessible. If you're not sure how to do that, read the [Finder/File Explorer section](#finder-mac-or-file-explorer-windows).
# Git

Git is a distributed version control system that helps you track changes in your code over time. It allows multiple people to work on the same project simultaneously and merge their changes seamlessly. Git is essential for collaborative coding and is widely used in software development, including robotics projects.

## Checking if Git is installed

Before installing Git, let's check if it's already installed on your system.

### For Mac and Linux:

1. Open Terminal
2. Type the following command and press Enter:
   ```
   git --version
   ```
3. If Git is installed, you'll see a version number (e.g., "git version 2.30.1")
4. If you see "command not found", you'll need to install Git

### For Windows:

1. Open PowerShell
2. Type the following command and press Enter:
   ```
   git --version
   ```
3. If Git is installed, you'll see a version number
4. If you see an error message, you'll need to install Git

## Installing Git

If Git is not installed on your system, follow these steps:

### For Mac:

1. Install Homebrew if you haven't already (visit https://brew.sh/ for instructions)
2. Open Terminal
3. Run the following command:
   ```
   brew install git
   ```

### For Windows:

1. Visit https://git-scm.com/download/win
2. Download the latest version for your system (64-bit or 32-bit)
3. Run the installer and follow the prompts (you can use the default settings)

### For Linux:

For Ubuntu or Debian-based distributions:
1. Open Terminal
2. Run the following commands:
   ```
   sudo apt update
   sudo apt install git
   ```

For other distributions, consult your package manager's documentation.

## Creating a GitHub Account

GitHub is a web-based platform that uses Git for version control. It's where you'll store your code repositories online.

1. Visit https://github.com/
2. Click "Sign up" in the top right corner
3. Follow the prompts to create your account
## Configuring Git

After installing Git and creating a GitHub account, you need to configure Git with your name and email:

1. Open Terminal (Mac/Linux) or PowerShell (Windows)
2. Set your name:
   ```
   git config --global user.name "Your Name"
   ```
3. Set your email (use the same email as your GitHub account):
   ```
   git config --global user.email "youremail@example.com"
   ```
## Authentication: Personal Access Token (PAT)

GitHub now requires a Personal Access Token for authentication instead of a password when using Git from the command line. Here's how to set it up:

1. Go to GitHub and log in
2. Click on your profile picture in the top-right corner and select "Settings"
3. Scroll down to "Developer settings" in the left sidebar
4. Click on "Personal access tokens" and then "Generate new token"
5. Give your token a descriptive name, set the expiration to the maximum amount (1 year), and select the appropriate scopes (at minimum, select "repo")
6. Click "Generate token" at the bottom of the page
7. Copy the generated token immediately (you won't be able to see it again)
8. Open Terminal (Mac/Linux) or PowerShell (Windows)
9. Run the following command (Replace `YOUR-USERNAME` with your GitHub username):
```
git ls-remote https://github.com/YOUR-USERNAME/fake-repo-name.git
```
10. When prompted for your password, enter your PAT instead.
11. If you get an "Authentication failed" error, double-check your PAT and try again.
12. On most modern systems, Git will automatically store your credentials after you've entered them once. If, however, you find that you're being asked for your PAT repeatedly, you may need to set up a credential helper:
For Mac/Linux:
```
git config --global credential.helper store
```
For Windows:
```
git config --global credential.helper wincred
```

Note: There are other authentication methods available, such as SSH keys, but PAT is recommended for its simplicity and security. If you're interested in exploring other options, you can refer to GitHub's documentation on authentication.
# Visual Studio Code (not WPILib)

This is going to be for writing non-robotics code. For instance, you can use regular VSC for [Java101](link) and [Java102](link). If you'd rather not have this on your computer, feel free to skip this step.

1. [Download VSCode here](https://code.visualstudio.com/download).
2. Once VSCode is installed, open it.
3. Install the Java Extension Pack:
    - Click on the Extensions icon in the left sidebar (it looks like four squares)
    - In the search bar, type "Extension Pack for Java"
    - Look for the package by Microsoft and click "Install"
    - This pack includes several useful extensions for Java development, including the Language Support for Java by Red Hat, Debugger for Java, Java Test Runner, and Maven for Java
4. Optional: Install Git Graph:
    - In the Extensions sidebar, search for "Git Graph"
    - Look for the extension by mhutchie and click "Install"
    - This extension provides a graphical view of your Git repository, which can be very helpful when working with version control

# WPILib

1. [Follow this guide to install WPILib](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html) (we use Java, so ignore the additional C++ installation)
2. Optional: Change the WPILib VSCode icon to distinguish from regular VSCode
	1. Download [the WPILib logo](link to image)
	2. Replace the icon:
        - For Windows:
            1. Right-click on the WPILib VSCode shortcut
            2. Select "Properties"
            3. Click "Change Icon"
            4. Browse to the downloaded WPILib logo and select it
            5. Click "OK" to apply the changes
        - For Mac:
            1. Locate the WPILib VSCode app in Finder
            2. Right-click (or Control-click) on the app and select "Get Info"
            3. Drag the downloaded WPILib logo onto the icon in the top-left corner of the Get Info window
        - For Linux:
            1. Locate your .desktop file for WPILib VSCode (usually in ~/.local/share/applications/ or /usr/share/applications/)
            2. Open the .desktop file with a text editor
            3. Find the line starting with "Icon="
            4. Replace the value with the full path to your downloaded WPILib logo
            5. Save the file and refresh your desktop environment
3. Install additional extensions:
    - Open WPILib VSCode
    - Click on the Extensions icon in the left sidebar (it looks like four squares)
    - Install "Test Runner for Java" by Microsoft
    - Optionally: Install "Git Graph" by mhutchie
# A Secret

I didn't write the [git section](#git). I also didn't write several parts of the [VSCode](#visual-studio-code-not-wpilib) and [WPILib](#wpilib) sections. Instead, I prompted [Claude](claude.ai) to do it for me.

The moral of this story is that chat bots like Claude and ChatGPT are fantastic resources when used well. And getting help with git or command line or installing things are all great uses for AI.

[Go here](link) for more tips on how to use (and how not to use) chat bots and AI for programming!