## Introduction
GitHub is a platform for managing and sharing code, built on top of Git, a version control system. It lets you track changes to your code, work on different features or fixes in separate branches, and merge everything together without losing progress. It’s especially useful for teams, making it easy to review code, resolve conflicts, and collaborate on projects efficiently. 

This guide covers how to use GitHub to manage code effectively, best practices to keep in mind while using git, and a cheat sheet with all the important commands. It's also recommended that you checkout this [intro to git](https://developer.ibm.com/tutorials/d-learn-workings-git/) for a more indepth analysis on the inner workings of git. 

## Best Practices
A list of everything you should and are expected to do when working with git. 

#### Use branches effectively
Always create a new branch for each task, feature, or fix. This keeps your work isolated, makes collaboration easier, and helps prevent conflicts with the main branch.

#### Merge regularly
Merge changes back into the main branch often, once they’re tested and complete. Regular merging keeps the main branch current and helps avoid larger conflicts later on.

#### Commit and push frequently
Save and push your changes to the remote repository consistently. This keeps your progress backed up and ensures your team has access to the latest updates.

#### Review code thoroughly
Review and discuss changes before merging them into the main branch. This helps catch errors, improve code quality, and ensure everyone is aligned.

## Cheat Sheet

Simple list of all the most commonly used commands.

#### Cloning
`git clone <repository-link | repository-name> [repository-folder]`

Copies the repo (repository) from github and puts it in a folder on your computer. It will put it in a folder with the name of the repository unless you specify a folder afterwards.


#### Committing
`git commit [-m <message>]`

Every commit in GitHub you can think of as saving your progress. Although we’d like for our commit messages to be as descriptive as possible, being too detailed would be inappropriate as nobody would want to read such long commit messages. Try to limit your message lengths to at most a sentence, or make it like a title.

`git commit -m “decreased code duplication in Robot.java”`

However, before you can commit, you need to “mark” the files you would like to save. Only marked files will be saved. To mark a file you will need to  git add  modified files. For example, to add all changed files in your current directory, you may use: 

`git add .`

#### Pulling
`git pull`

Copies any new commits that are on the remote GitHub repo to your local repo.

#### Pushing
`git push`

Sends any commits you’ve made to your local repo to GitHub.

#### Status
`git status`

Tells you what files have been committed and added. It is very helpful and pretty self-explanatory once you run it.

#### Stashing  
`git stash`  

Temporarily saves your uncommitted changes so you can work on something else without losing progress.  
 
`git stash apply`  

Restores your stashed changes when you're ready to continue working on them.

#### Checkout
`git checkout <branch-name>`

Moves you to the specified branch.

`git checkout -b <new-branch-name>`

Creates that branch and moves you to it. This is equivalent to:

- `git branch ball-counter`
- `git checkout ball-counter`

#### Merging
`git merge <branch-to-pull-changes-from>`

Merges a branch into your branch. That is, changes from the specified branch will be added to your branch, and not the other way around.