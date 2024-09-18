# Introduction

Git is a great tool for teams to collectively work on a project together!

# Conceptualization

### Repositories

### Branches

When many different people work on a single repository, it often happens that different people are attempting to make different changes at different times. Making changes directly to the main codebase creates some pretty serious issues. For one, changes can be made that either don't work, or perhaps break the code entirely if Java runs into an issue. Also, if multiple people are working on the same file and have a conflict in their code, editing the main codebase directly is dangerous and can cause the code to break. In order to circumvent this, it makes sense that contributors to a repository should be given their own little sandbox to work out the changes they will make before they are added to the main codebase.

Branches are a great reflection of this. When someone makes a new branch, they get a copy of the entire codebase at that time, and any changes made to that branch will not affect the main codebase. You could delete everything on that branch and no one would bat an eye. The idea is that a branch will be made, all of the relevant changes will be made, and once the proposed changes are good enough to be worthy of being on the main codebase, it will be reviewed and then eventually brought on.

The repository usually consists of many branches, with the main branch at the center of it all. The main branch is the main codebase, and nearly all of changes made to that branch must first go through a rigorous process of review. This keeps the main branch perfect, as any possible code-breaking glitches will have been sussed out far before the changes were added to the main branch.

### Commits

Saving versions of anything you make as you go along is very useful for big projects. It can help organize the changes that have been made, and also help you go back to a previous version in case something goes wrong. Consider this: you have just been working for a couple hours, making many changes in the process. Your code was working fine, and had no problems thirty minutes ago, but for some reason, it just isn't working now, and you have absolutely no idea why, even after looking at the error report. It would be nice to go back to a previous version, compare them, and see what the issue is.

A commit, put simply, is just this, a version of the codebase. Commits keep track of the changes that have been made to the code, bundles them up and slaps a message on them. When going back to previous versions, if the commit was labeled with a commit message, it makes it much easier to figure out where you went wrong, or where to return to.

### Pushing and Pulling

### Merging

### Stashing

# Using Git

### Cloning

### Committing

### Branching

### Pushing

### Pulling

### Merging

### Pull Requests