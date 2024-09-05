# Introduction
## Prerequisites

- Comfortable with all of the [goals for Programming101](/projects/Programming101#goals).
- Comfortable with [command-line navigation](link)
- Environment set up
	- [Code directory created](link)
	- [VSCode installed](link)
	- [Git & Github set up](link)
## Goals

come back
# Setup

## Create GitHub Repo

(maybe move this section to a separate ref sheet)
A GitHub repository, often referred to as a "repo," is a central location where you can store, manage, track, and control changes to your project files. It's like a folder for your project that is hosted on GitHub's servers. It also allows you to easily share your code, or collaborate with others.
You're going to create a repo for the code that you write in this tutorial.
1. Open [GitHub](github.com) and log in.
2. Create a new repository
	- Click the '+' icon in the top-right corner of the page.
	- Select "New repository" from the dropdown menu.
3. Set up your repository
	- Choose a name for your repository (e.g., "Learning Java").
	- Add a brief description (optional).
	- Choose "Public" or "Private" for your repository visibility (if you choose Private, no one will be able to see it unless you explicitly add them).
		- You can always change this later
	- Check the box to "Initialize this repository with a README".
	- Press the ".gitignore template" dropdown under "Add .gitignore" and choose "Java"
	- Click "Create repository"
4. Clone the repository on your local machine
	- On your new repository's page, click the green "Code" button.
	- Copy the HTTPS URL provided.
	- Open Terminal for Mac/Linux, or PowerShell for Windows
	- Navigate to the directory where you want to store your project, and clone the repositry:
```
cd path/to/your/code/folder
git clone HTTPS-LINK
```
Replace `path/to/your/code/folder` with the path to the directory you created for your code, and replace `HTTPS-LINK` with the URL you copied.
5. Verify the clone
	- Look at the contents of your code directory and check that the new repository is there"
```
ls
```

## Open Repo in VSCode

1. Open VSCode
	- If you installed regular, non-WPILib VSCode, open that
2. Open the repository folder
	- In VSCode, go to File > Open Folder (or use the keyboard shortcut: Ctrl+K Ctrl+O on Windows/Linux, Cmd+O on Mac).
    - Navigate to the directory where you cloned your repository.
    - Select the repository folder and click "Select Folder" (or "Open" on Mac).

In the left sidebar, you should see the file explorer with your repository's files (README.md and .gitignore).
## Write README

A README file is a text file that introduces and explains a project.

Open your README.md file, and write a few words about what this project is. Some suggestions:
- Say that you're learning Java
- **Link to this page**
	- This README (like this guide) is written in Markdown, a simple langauge for formatting text. Here's how you embed a link in Markdown:
```
[text](link)
```

## Create Main File

It's time to make your first Java file!

1. Right click in the file explorer on the left
2. Select "New File"
3. Name your file "Main.java"

Your file should look something like this:
```java
public class Main {

}
```
(If it doesn't have that code in it yet, copy it in from here.)

Put your curser on the line in between the two curly braces. Write "main" and then hit tab. Your file should end up looking like this:

```java
public class Main {
	public static void main(String[] args) {
	
	}
}
```

Above the words `public static void` you should see a little `Run | Debug`. You should be able to press on either word.

Okay, you're all set up!
# File Structure