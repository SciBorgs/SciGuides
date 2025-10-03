# Setting up Software

**Hello young aspiring Sciborg programmer!** This guide will go over how to setup the software you will need to code a robot.

Here is what will be covered here:

1. **[How to download and install WPILIB®](#how-to-download-and-install-wpilib)**
2. **[How to download and install Git](#how-to-download-and-install-git)**

If you are curious on **what exactly you are downloading** head over to [our Introduction](./Intro.md) to learn more.

## How to download and install WPILIB®

Head over to [the Github page for WPILIB®](https://github.com/wpilibsuite/allwpilib/releases/tag/v2025.3.2) and scroll down a bit in order to find the **"Downloads"** section. From here, pick your favorite operating system and **click the link** to install the ISO / DMG file.

> If you are unsure of what to download, no worries! Search up: **"How do I tell what my operating system is?"**. If you are on a **Mac®**, then you also should look up **"How do I tell what processor I have?"** in order to pick between **ARM** and **Intel®**. ARM chips are the ones **made by Apple®**, while Intel chips are (surprisingly) the ones **made by Intel®**. If you are using Linux and are wondering about what processor you have: **I will personally remove you from the JV Robotics Program and meet with your parents**.

If you are on the **Windows® Operating System** you will need to **mount** the **ISO file** after it has been downloaded. **Go to file explorer, right-click the file, and click 'Mount'.** After that, go to File Explorer again and find the **newly mounted folder** (it will probably be next to your **Local Disk C: Drive** in the sidebar). Once you have found this: **Run the WPILIB® Installer**.

If you are on the **Mac® Operating System** you will need to **open** the **DMG file** and then **run** the **Run the WPILIB® Installer**.

> Make sure to install **everything** for **this user only** (if this is not your own private computer) and **download VS Code for your computer only**.

## How to download and install Git

Head over to [the official Git website](https://git-scm.com/downloads) and install the **Git Installer** (feel free to use portable if you prefer that). Then, **run** the **Git Installer** and use the **default settings** (if you know what you are doing, feel free to use whatever settings you would like). After that we need to do some **extra stuff** before successfully installing git (**we will need to create a Github account first**).

## How to create a Github account

Head over to [the official Github website](https://github.com) and **sign up** with any email you would like. **Feel free to use your Bronx Science email for this**. You don't have to worry too much about the settings for now, just make sure to **remember your email and username**.

## How to link Git with Github

**Open up the Command Line**. If you are unsure about how to do this, **just look it up**! (it is different for each operating system). **Run these 3 commands to configure Git**. Make sure to **swap out** "[Your Name]" with your Github username and "[Your Email]" with your Github-associated email address.

``` 
git config --global user.name "[Your Name]" 
git config --global user.email "[Your Email]"
git config --global core.editor "code --wait"
```

### Authentication

1. Go to GitHub and **log in**
2. Click on your profile picture in the top-right corner and **select** "Settings"
3. **Scroll down** to "Developer settings" in the **left sidebar**
4. **Click** on "Personal access tokens" and **then** "Generate new token"
5. **Give your token a descriptive name**, set the expiration to the maximum amount (1 year), and select the appropriate scopes (**at minimum, select "repo"**)
6. **Click** "Generate token" at the bottom of the page
7. **Copy the generated token** immediately (you won't be able to see it again)
8. Open Terminal once again
9. **Run** the following command:
```
git ls-remote https://github.com/fake-username/fake-repo-name.git
```
10. When prompted for your password, enter your PAT instead.
11. If you got a "Repository not found" error, everything went right! If you get If you get an "Authentication failed" error, double-check your PAT and try again.
12. On most modern systems, Git will automatically store your credentials after you've entered them once. If, however, you find that you're being asked for your PAT repeatedly, you may need to set up a credential helper:

**For Mac:**

```
git config --global credential.helper store
```

**For Windows:**

```
git config --global credential.helper wincred
```

>That is all! Farewell young aspiring Sciborgs programmer! Head on to **[Day 2](../Day%202/Java101.md)** if you'd like.


