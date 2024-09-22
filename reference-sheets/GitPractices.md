# Introduction

Git is a great tool for teams to collectively work on a project together. Conceptualizing the way git is structured is somewhat difficult for people who are very new to the subject, but this guide should make it super easy and digestible! After the explanation of concepts and definitions of terms, there is a Usage section where you will learn the commands to use git in the command line. After firmly grasping the concepts, remembering the commands become simple tasks, and once you practice enough with them, they become second nature to a programmer.
# Conceptualization

Before conceptualizing the ideas behind the various command line inputs, remembering the actual command line inputs is a little bit confusing. Although it is possible to learn **how** to use git and program with that, it is much better to learn **how git works** and then build off of that. Therefore, before going over the individual command line inputs, we will go over the main concepts, what they mean, and how they contribute to programming for your team.

### Repositories

If more than one person is working on a codebase, the codebase needs a place to be stored. The way nearly everyone does this is by using something called a **Github Repository**. A Repository is a place on the cloud for folders and files to be stored, which is **accessible by git**. Each repository is its own **git project**, or a unit of storage on git. 

Those were some fancy magic words, but to put it simply, it's a place on the internet where your team's code will go. 

If your team's repository has something called **branch protections**, which it most likely does, then you won't be able to edit the code directly. There are other ways that you can contribute, of which will be discussed later in this guide. 

When your team makes a project on Github and adds some files and folders to it, in order to get those files onto your computer for editing, you'll need to **clone** it. Cloning is the way you get git to **download** a git project, or repository, into files on your computer. This is because the most efficient ways to edit code is on an **Integrated Development Environment** (a code-editing app), such as **Visual Studio Code** (with plugins), which run by editing files on your computer.

### Branches

When many different people work on a single repository, it often happens that different people are attempting to make different changes at different times. Making changes directly to the main codebase creates some pretty serious issues. For one, changes can be made that either don't work, or perhaps break the code entirely if Java runs into an issue. Also, if multiple people are working on the same file and have a **conflict** in their code, editing the main codebase directly is **dangerous** and can cause the code to break. In order to circumvent this, it makes sense that contributors to a repository should be given their own little sandbox to work out the changes they will make before they are added to the **main codebase**.

**Branches** are a great reflection of this. When someone makes a **new branch**, they get a copy of the **entire** codebase at that time, and any changes made to that branch will **not** affect the main codebase. You could delete everything on that branch and no one would bat an eye. The idea is that a branch will be made, all of the relevant changes will be made to that branch, and once the proposed changes are good enough to be worthy of being on the main codebase, it will be reviewed and then eventually brought on.

The repository usually consists of many branches, with the main branch at the center of it all. The main branch is the main codebase, and nearly all of changes made to that branch must first go through a rigorous process of **review**. This keeps the main branch perfect, as any possible code-breaking glitches will have been sussed out far before the changes were added to the main branch.

### Commits

Saving **versions** of anything you make as you go along is very useful for big projects. It can help organize the changes that have been made, and also help you go back to a **previous version** in case something goes wrong. Consider this: you have just been working for a couple hours, making many changes in the process. Your code was working fine, and had no problems thirty minutes ago, but for some reason, it just isn't working now, and you have absolutely no idea why, even after looking at the error report. It would be nice to go back to a previous version, compare them, and see what the issue is.

A **commit**, put simply, is just this, a **version of the codebase.** Commits keep track of the **changes** that have been made to the code, bundles them up and slaps a **message** on them. When going back to previous versions, if the commit was labeled with a commit message, it makes it much easier to figure out where you went wrong, or where to return to. Changes that are made locally on the device that have not been committed yet are named **working changes**, which is pretty simple to remember since they are what you are working on at the current moment. 

Rather than bundling all the code, which is non storage-efficient for larger repositories, and would take very long both to download and to upload, git simply keeps track of the **changes you've made**. However, when committing, git doesn't know the changes you want to commit. So, you first have to **stage** those changes in the terminal (we will go over this later) and then you can commit. 

Make sure to commit with a **message**! If committing either without a message or with a irrelevant one (e.g. "g", "iglsjgf;l", "made some changes") then it takes out half of the reason you're committing in the first place, and makes it difficult for you and **people reviewing your changes** to determine what you did in each commit! So, always make a **very brief description** of the changes you've made. It's not just good practice, it's also helpful to everyone.

### Pushing and Pulling

Commits are **local changes**, which means that they **aren't** put onto the cloud, or Github. This is mostly so you can go to a previous commit, before adding your changes to your branch. When we add our previous commits to the branch, we call this **"pushing our changes,"** because you are taking all of your changes, all of your previous commits, and applying them to the **remote branch**. Put simply, you are taking your **local changes** and making them **remote**, or uploading them to the cloud (Github).

When pushing changes, it places it in the Github repository, and those changes are made **public** to all others working on the repository. When you push changes for the first time on a branch, it establishes the branch on the repository and people will be able to switch to it on the website. So, make sure to push somewhat regularly so that others can keep track of what you're doing.

Now, say you're working on a branch at a school computer. You push your changes, and then go home to work on your home computer. Your home computer has no idea that these changes occurred on the branch, so it will still have the code it last saw. In order to get your pushed changes from the cloud to your home computer, you need to **pull** them.

**Pulling changes** is especially useful when working with **multiple people** on the **same branch**. If one person pushes their changes, then another, they will have **conflicts**. So, it's important that, when doing this, changes are always pulled before they are pushed, so each new push is up-to-date. Make sure, in this situation, to pull extremely regularly because conflicts between the two users' code will stack up extremely quickly, and eventually it will be faster just to abandon and rewrite the entire branch than to sort out each and every one of those changes. I'm speaking from experience. Pull regularly.

### Stashing

Sometimes you'll be working on a branch, then realize that you need those changes that your friend pushed five minutes ago in order to finish your code. If you decide to commit now and pull after, then you will have to sort out a bunch of annoying merge conflicts, and have an unfinished commit in the tree, but if you decide to pull, then all of **your** working changes will need to be **undone** first. To avoid this, there must be a way to **store** your changes locally **without** committing, so that you can pull your **friend's** changes and then apply **your** changes, so **both** changes will be applied in the next commit. 

Thankfully, the git overlords have gifted us the ability to **stash** our changes. When you stash your changes, it bundles all your working changes into the git stash and removes all those changes from your files; it reverts you to the most recent commit. You can do what you'd like, but when you want those changes back, you can simply reapply them to your code, even if you're a commit forward. 

Removing your changes from the stash and placing them back in your working changes is called **popping** the changes. Popping your stashed working changes throws them back into your code, like popping a bubble full of working changes, and once it's popped the working changes fall back onto the code.

Two people on a branch is not the only situation when you'd use stash. Sometimes, you want to write something a different way, but want to keep your changes just in case you change your mind. In this scenario, you can just stash your working changes, then rewrite it all, and if you don't like the rewrite, all you have to do is pop! Stashed changes restored. 

### Merging

When you're finally done with your changes on a branch, and you are sure that it is absolutely perfect, you create something called a **Pull Request** on Github, to merge it to the main branch and be added to the main codebase. Someone with merge permissions (an admin of the repository) will look over your code, indirectly humble your coding skills, and then tell you what to change before your code can be added to main. After the person reviewing your code thinks that it is perfect, they will approve it and you can then **merge your code into main**, bringing your changes officially into the codebase!

Essentially, merging is how you transfer code from **branch to branch**. This, of course, will include transferring code **from** main **to** your branch, to stay updated with recent changes to main. If other people make a pull request and it gets approved, then the main branch will have some new code that is **not** currently in your working branch. This means that you are **not** up to date with main. Therefore, you need to **merge main into your branch** every now and again, and especially before you make a pull request, to make sure that everything is up to date. When you merge main into your branch, sometimes there will be conflicts, especially if the file being edited by both you and the other contributor are the same. These are called **Merge Conflicts**, and can happen both with merging **and** with pulling changes from a branch. You just have to sort these out manually, deciding which changes to keep and which changes to toss. It's a little annoying to do, but if you do it often enough and efficiently enough then it doesn't become that big of a problem.

There is another way to merge main into your code called **Rebasing**, but it's complicated to explain in writing and you'll never use it with a team as small as a high school robotics team. The idea behind it is that you rewrite your commit history during a rebase, and that **instead** of branching off of the main branch that was four commits ago, you are **now** technically branched off of the newest main commit. It's useful for organizing commits to turn the visualization from a web to a tree, but when you're doing such small changes to a tiny codebase like used in robotics, it doesn't even matter. 

# Usage

Looks like you got through all the conceptualization. Nice job! However, that means absolutely nothing if you don't know how to put it into practice. So, in this section, we will go over the actual git command line inputs.

Opening the command line isn't a difficult task. Visual Studio Code has one built in (accessible by pressing ctrl+\`), which makes using git much easier. 
If you're not using VSCode, 
Windows: Press *Win + \X* to open the Command Prompt.
Mac: Press *Cmd + Space* to open spotlight search, then type "Terminal" to open the Terminal.
Linux: Spin around five times and then sing Mary Had A Little Lamb.

### Cloning

There are a few ways to clone a Github repository onto your computer, but the best way and the way that we'll be going over is by using the command line. 

Go onto the GitHub website, then find the repository. There should be a green button that says "Code." Click that, and then copy the link that shows up under it. This will be used in the command. It tells git what exactly to clone off of the internet.

Next, navigate using the command line to the target folder where you want your cloned repository to be on your computer. You can alternatively move the cloned folder after your clone it, but moving around using the command line makes me feel like a hacker so i do that instead.

Type this text into the command line:

`git clone <copied link>`

It should look something like this:

`git clone https://github.com/SciBorgs/SciGuides.git`

This would clone this repository, the SciBorgs' SciGuides onto your computer in your working directory.

### Branching

To make a branch, type into the command line:

`git branch <branch name>`

Make sure that your chosen branch name follows the naming standards! Your name should be:
1. Relevant: something indicative of what the branch is for
2. All lowercase
3. Spaces replaced with dashes

So, these would be fine:
- drivetrain
- auto-align
- feeder-fix
But these wouldn't:
- Drivetrain
- auto_align
- i-hate-git 

However, after you decide to create the branch, you still need to switch to that branch!
To do that, type into the command line:

`git checkout <branch name>`

You can also switch to a branch that isn't yours using `checkout`. If your friend was coding something and told you to go to their branch, you could just use checkout and it would work.

### Committing

Remember when we talked about staging our changes before committing? Well, to do that, type into the command line:

`git add .`

This will stage all of your working changes and make them ready for committing. The "." in this situation means all of your working changes.

Of course, there is a way for you to stage only certain files but there's really no situation where it would be used.

Once your changes are staged, we will want to commit those staged changes. Type into the command line:

`git commit -m "Put your message here"`

This will commit all of your changes, and the commit message on this commit will be '*Put your message here*. Make sure that your message is always useful and indicative of what you did in that commit! 

### Pushing

This one is very simple. Once you've committed and are ready to push your commits to the branch, just type into the command line:

`git push`

Super easy right?

Well, this is git we're talking about. If it so happens that the branch you're pushing to is local and not remote, meaning that you're pushing for the first time on a new branch, then git will raise an eyebrow and confirm that you are really trying to push this new branch, since technically you are pushing to a branch that doesn't particularly exist yet. In this case, it yells at you and tells you to type a certain command in, which should look somewhat like this:

`git push --set-upstream origin <branch>`

Instead of "<branch\>" put your branch name and you should have no problem pushing from that point on with that branch.

### Pulling

`git pull`

Yep. That's it. Just make sure that you have no working changes, or it won't work.

### Merging

This one seems simple at first, too, but unfortunately we are using git. 

Before we can merge the more recent changes to main with our branch, it is necessary for us to get the changes from main first. So, we're going to do just that. Type into the command line:

`git checkout main`
`git pull`

Now that we have fetched the changes from the cloud, we can go back to our branch to merge.

`git checkout <branch>`
`git merge main`

That second command will move those fetched changes from main to our branch. This will make a merge commit, meaning that it will commit for you. It still hasn't pushed these changes, though, so make sure you do that once you are ready to push.

### Pull Requests

There's no command line input for making a pull request. For this we'll have to go to the Github website.

At the top of the website, the third option from the left should say Pull Requests. click that one.

There should be a green button that says "New Pull Request."

It'll bring up a menu of branches. Click your branch.

After that, it'll bring up all your changes. Click the green "New Pull Request" button.

After that, pour your soul out in a wonderful paragraph description of what you did. It should be relatively brief; don't go over every last thing. Just say the main function of what you added.

After that, click the "Create pull request" button and you're done! Now other people will review your changes, and once that's done, they can be merged.

# Conclusion

Well. That's it! You now know all of the essentials for using git in projects. Now, the only thing you can do is get experience with it! Get one or two friends and start a collaborative project on Github, then get to it. Happy Coding!