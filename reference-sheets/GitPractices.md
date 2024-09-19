# Introduction

Git is a great tool for teams to collectively work on a project together!

# Conceptualization

### Repositories

### Branches

When many different people work on a single repository, it often happens that different people are attempting to make different changes at different times. Making changes directly to the main codebase creates some pretty serious issues. For one, changes can be made that either don't work, or perhaps break the code entirely if Java runs into an issue. Also, if multiple people are working on the same file and have a **conflict** in their code, editing the main codebase directly is **dangerous** and can cause the code to break. In order to circumvent this, it makes sense that contributors to a repository should be given their own little sandbox to work out the changes they will make before they are added to the **main codebase**.

**Branches** are a great reflection of this. When someone makes a **new branch**, they get a copy of the **entire** codebase at that time, and any changes made to that branch will **not** affect the main codebase. You could delete everything on that branch and no one would bat an eye. The idea is that a branch will be made, all of the relevant changes will be made to that branch, and once the proposed changes are good enough to be worthy of being on the main codebase, it will be reviewed and then eventually brought on.

The repository usually consists of many branches, with the main branch at the center of it all. The main branch is the main codebase, and nearly all of changes made to that branch must first go through a rigorous process of **review**. This keeps the main branch perfect, as any possible code-breaking glitches will have been sussed out far before the changes were added to the main branch.

### Commits

Saving **versions** of anything you make as you go along is very useful for big projects. It can help organize the changes that have been made, and also help you go back to a **previous version** in case something goes wrong. Consider this: you have just been working for a couple hours, making many changes in the process. Your code was working fine, and had no problems thirty minutes ago, but for some reason, it just isn't working now, and you have absolutely no idea why, even after looking at the error report. It would be nice to go back to a previous version, compare them, and see what the issue is.

A **commit**, put simply, is just this, a **version of the codebase.** Commits keep track of the **changes** that have been made to the code, bundles them up and slaps a **message** on them. When going back to previous versions, if the commit was labeled with a commit message, it makes it much easier to figure out where you went wrong, or where to return to.

Rather than bundling all the code, which is non storage-efficient for larger repositories, and would take very long both to download and to upload, git simply keeps track of the **changes you've made**. However, when committing, git doesn't know the changes you want to commit. So, you first have to **stage** those changes in the terminal (we will go over this later) and then you can commit. 

Make sure to commit with a **message**! If committing either without a message or with a irrelevant one (e.g. "g", "iglsjgf;l", "made some changes") then it takes out half of the reason you're committing in the first place, and makes it difficult for you and **people reviewing your changes** to determine what you did in each commit! So, always make a **very brief description** of the changes you've made. It's not just good practice, it's also helpful to everyone.

### Pushing and Pulling

Commits are **local changes**, which means that they **aren't** put onto the cloud, or Github. This is mostly so you can go to a previous commit, before adding your changes to your branch. When we add our previous commits to the branch, we call this **"pushing our changes,"** because you are taking all of your changes, all of your previous commits, and applying them to the branch. You are **pushing** your changes to the branch. Pretty intuitive.

When pushing changes, it places it in the Github repository, and those changes are made **public** to all others working on the repository. When you push changes for the first time on a branch, it establishes the branch on the repository and people will be able to switch to it on the website. So, make sure to push somewhat regularly so that others can keep track of what you're doing.

Now, say you're working on a branch at a school computer. You push your changes, and then go home to work on your home computer. Your home computer has no idea that these changes occurred on the branch, so it will still have the code it last saw. In order to get your pushed changes from the cloud to your home computer, you need to **pull** them.

**Pulling changes** is especially useful when working with **multiple people** on the **same branch**. If one person pushes their changes, then another, they will have **conflicts**. So, it's important that, when doing this, changes are always pulled before they are pushed, so each new push is up-to-date. Make sure, in this situation, to pull extremely regularly because conflicts between the two users' code will stack up extremely quickly, and eventually it will be faster just to abandon and rewrite the entire branch than to sort out each and every one of those changes. I'm speaking from experience. Pull regularly.
### Merging

When you're finally done with your changes on a branch, and you are sure that it is absolutely perfect, you create something called a **Pull Request** on Github, to merge it to the main branch and be added to the main codebase. Someone with merge permissions (an admin of the repository) will look over your code, indirectly humble your coding skills, and then tell you what to change before your code can be added to main. After the person reviewing your code thinks that it is perfect, they will approve it and you can then **merge your code into main**, bringing your changes officially into the codebase!

Essentially, merging is how you transfer code from **branch to branch**. This, of course, will include transferring code **from** main **to** your branch, to stay updated with recent changes to main. If other people make a pull request and it gets approved, then the main branch will have some new code that is **not** currently in your working branch. This means that you are **not** up to date with main. Therefore, you need to **merge main into your branch** every now and again, and especially before you make a pull request, to make sure that everything is up to date. When you merge main into your branch, sometimes there will be conflicts, especially if the file being edited by both you and the other contributor are the same. These are called **Merge Conflicts**, and can happen both with merging **and** with pulling changes from a branch. You just have to sort these out manually, deciding which changes to keep and which changes to toss. It's a little annoying to do, but if you do it often enough and efficiently enough then it doesn't become that big of a problem.

There is another way to merge main into your code called **Rebasing**, but it's complicated to explain in writing and you'll never use it with a team as small as a high school robotics team. The idea behind it is that you rewrite your commit history during a rebase, and that **instead** of branching off of the main branch that was four commits ago, you are **now** technically branched off of the newest main commit. It's useful for organizing commits to turn the visualization from a web to a tree, but when you're doing such small changes to a tiny codebase like used in robotics, it doesn't even matter. 

### Stashing

# Using Git

### Cloning

### Committing

### Branching

### Pushing

### Pulling

### Merging

### Pull Requests