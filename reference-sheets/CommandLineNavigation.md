# Introduction

The command line interface (CLI), also known as the terminal or shell, is a text-based interface for interacting with your computer's operating system. Instead of using a graphical user interface (GUI) with icons and windows, you type commands to perform actions like navigating directories, creating files, or running programs.
## Goals

Familiarity with the following ideas and commands:
- How a computer organizes files
- Command Line shortcuts
- Basic commands
	- pwd
	- ls
	- cd
	- mkdir
	- touch/type nul >
	- cat
	- cp
	- mv
	- rm

This guide is really only scratching the surface on Command Line use, but it should give you what you need to get started.
## Best Practices

If you're learning this for the first time, follow along! Whenever a new command is taught, try the examples on your own machine.
## LLMs

Command Line navigation is an area in which LLMs are incredibly useful. If you ever want to know how to do something on Command Line, ask ChatGPT or Claude!
# Computer Organization

Computers organize files and folders in a hierarchical structure, often called a file system. The top-level directory is called the root directory. On Windows, this is typically represented by `C:\`, while on Mac and Linux, it's represented by `/`.

Your user account has a home directory where your personal files are stored:

- On Mac and Linux: `/home/username` (often shortened to `~`)
- On Windows: `C:\Users\username`

That's where the folders that you're used to seeing (Documents, Downloads, etc) are.

As you navigate through the file system, you'll be working within a specific directory at any given time. This is called your working directory. When you open a new terminal, it usually starts in your home directory.

When referring to directories, there are two special references you'll often encounter: `.` (dot) refers to the current directory, and `..` (dot dot) refers to the parent directory (one level up). These are useful for navigating the file system and specifying file paths.
## Paths

When referring to files or directories, we use paths. There are two types of paths: absolute and relative.

An absolute path provides the complete location of a file or directory from a fixed point in the file system, regardless of the current working directory. This fixed point is typically:

- The root directory, represented by `/` on Mac/Linux or a drive letter (e.g., `C:\`) on Windows.
- The home directory, often represented by `~` on Unix-like systems.

Examples of absolute paths:

- `/home/username/Documents/file.txt` (from root on Unix-like systems)
- `C:\Users\username\Documents\file.txt` (from root on Windows)
- `~/Documents/file.txt` (from home directory)

A relative path, on the other hand, specifies the location of a file or directory relative to the current working directory. It doesn't start with `/`, a drive letter, or `~`.

For instance, if you're in `/home/username`, you can refer to a file in your Documents folder as `Documents/file.txt`. Relative paths often make commands shorter and more portable, especially when working within your own directory structure.

And remember, you can use `.` to refer to the current directory and `..` to refer to the parent. So if you were in the `/home/username/Documents`, and you want to refer to a file whose absolute path is `/home/username/file.txt`, you could do that using `../file.txt`.
# Accessing the Command Line

- **Mac**: Open the "Terminal" application (found in Applications > Utilities)
- **Windows**: Open "PowerShell" (or "Command Prompt" if your computer does not have "PowerShell")
	- If you end up using "CommandPrompt", some of the commands in this guide will not work. When that happens, ask ChatGPT or Claude or another LLM how to translate the command to use in "CommandPrompt".
- **Linux**: Open your distribution's terminal application (often accessible with Ctrl+Alt+T)

Once you've got your CLI open, all you need to do to execute a command is type it and hit enter!
# Command Line Shortcuts

These keyboard shortcuts will be very important to efficiently using Command Line. The most important ones are italicized.

1. **Tab Completion**: Press the Tab key to autocomplete file names, directory names, and commands. If there are multiple possibilities, press Tab twice to see all options.
2. **Command History**:
    - *Use the Up and Down arrow keys to navigate through previously used commands.*
    - Ctrl + R: Search through command history (start typing to search).
3. **Cursor Movement**:
    - *Ctrl + A: Move cursor to the beginning of the line.*
    - *Ctrl + E: Move cursor to the end of the line.*
    - *Option + Left/Right Arrow (Mac) or Ctrl + Left/Right Arrow (Windows/Linux): Move cursor word by word.*
4. **Editing**:
    - *Ctrl + U: Clear the line before the cursor.*
    - *Ctrl + K: Clear the line after the cursor.*
    - *Ctrl + W: Delete the word before the cursor.*
5. **Process Control**:
    - *Ctrl + C: Interrupt (terminate) the current command.*
    - Ctrl + Z: Suspend the current command (can be resumed later).
6. **Screen Control**:
    - Ctrl + L: Clear the screen (same as the `clear` command).
7. **Terminal Output Control**:
    - Ctrl + S: Pause output to the screen.
    - Ctrl + Q: Resume output to the screen.
# Basic Commands

## 1. pwd (Print Working Directory)

`pwd` shows your current location in the file system.
## 2. ls (List)

`ls` lists the contents of a directory.
### Usage

To list contents of working directory:
```bash
ls
```

To list contents of another directory:
```bash
ls [path to directory]
```
### Examples

Show contents of parent directory:
```bash
ls ..
```

Show contents of parent of parent directory:
```bash
ls ../..
```

Show contents of Documents:
```bash
ls ~/Documents
```
## 3. cd (Change Directory)

`cd` allows you to move between directories.
### Usage

To move to the home directory:
```bash
cd
```

To move to another directory:
```bash
cd [path-to-directory]
```
### Examples

Move to parent directory:
```bash
cd ..
```

Move to Documents:
```bash
cd ~/Documents
```

Move to the parent of the home directory:
```bash
cd ~/..
```

Move back to your home directory:
```bash
cd
```
## 4. mkdir (Make Directory)

`mkdir` creates a new directory.
### Usage

```bash
mkdir [path-to-new-directory]
```
### Examples

Make a new directory in your working directory:
```bash
mkdir cml-practice
```

Make a new directory inside of `cml-practice`:
```bash
mkdir cml-practice/foo
```

Make a new directory in `cml-practice`, but do so from within `foo`:
```bash
cd cml-practice/foo
mkdir ../bar
```

Make a new directory in Documents:
```bash
mkdir ~/Documents/cml-practice-documents
```
## 5. touch (macOS/Linux) or type nul > (Windows)

These commands create a new, empty file.
### Usage

`touch`:
```bash
touch [path-to-new-file]
```

`type nul >`:
```powershell
type nul > [path-to-new-file]
```
### Examples

Create a file inside of `foo` (Mac/Linux):
```bash
touch cml-practice/foo/file.txt
```

Create a file inside of `foo` (Windows):
```powershell
type nul > cml-practice/foo/file.txt
```
## 6. cat (Concatenate and Print)

`cat` displays the contents of a file.
### Usage

```bash
cat [path-to-file]
```
### Examples

Before we look at the contents of a file, let's make a file with something in it to see (you don't need to understand exactly what's happening here -- it shouldn't be super useful to you):

```bash
echo "Hello world!" > cml-practice/foo/hello.txt
```

(If you're using CommandPrompt, don't include the quotation marks)

Now we should have a file `cml-practice/foo/hello.txt` whose contents is the text "Hello World!"

Let's look at it:
```bash
cat cml-practice/foo/hello.txt
```
## 7. cp (Copy)

`cp` copies files or directories.
### Usage

To copy a file:
```bash
cp [path-to-source] [path-to-destination]
```

If the destination path is a directory, it will copy the source file into that destination directory, with the original file name. If the destination path is to a file name, the contents of the source file will be moved to the destination file.

To copy a directory (Mac/Linux):
```bash
cp -r [path-to-source-dir] [path-to-destination]
```
### Examples

Copy hello.txt to bar (and then print the contents to confirm that it worked):
```bash
cp cml-practice/foo/hello.txt cml-practice/bar
cat cml-pracice/bar/hello.txt
```

Copy file.txt to cml-practice/baz.txt (and list the contents of cml-practice to confirm that it worked):
```bash
cp cml-practice/foo/file.txt cml-practice/baz.txt
ls cml-practice
```
## 8. mv (Move or Rename)

`mv` moves files or directories. It can also be used to rename files or directories, because renaming something is really just moving its contents to something with a different name.
### Usage

To move a file or directory:
```bash
mv [path-to-source] [path-to-destination]
```

If the source is a file and the destination is a directory, the file will be moved into that directory. If the source and destination are both files, the contents of the file will be moved to a file at the destination path. If the source is a directory, the destination cannot be a file.

With both files and directories, if the source and destination have the same parent directory, the file or directory will effectively just be renamed.
### Examples

Rename file.txt to new-name.txt (and then verify that it worked):
```bash
mv cml-practice/foo/file.txt cml-practice/foo/new-name.txt
ls cml-practice/foo
```

Make a new directory inside of bar, and then move it to cml-practice (and then verify that it worked):
```bash
mkdir cml-practice/bar/foobar
ls cml-practice/bar
mv cml-practice/bar/foobar cml-practice
ls cml-practice
```
## 9. rm (Remove)

`rm` deletes files or directories.
### Usage

To remove a file:
```bash
rm [path-to-file]
```

To remove an empty directory:
```bash
rm -d [path-to-empty-dir]
```

To remove a directory and its contents:
```bash
rm -r [path-to-dir]
```

*Be very careful with rm -r. This will delete everything in a directory, and there is no undo!*

### Examples

Remove cml-pracice/bar/hello.txt:
```bash
rm cml-pracice/bar/hello.txt
```

Remove ~/Documents/cml-practice-documents:
```bash
rm -d ~/Documents/cml-practice-documents
```

Remove the entirety of cml-practice:
```bash
rm -r cml-practice
```