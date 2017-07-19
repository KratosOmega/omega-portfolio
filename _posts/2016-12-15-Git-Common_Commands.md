---
layout: post
section-type: post
title: Git Common Commands
category: Git
tags: [ 'git' ]
comments: true
---

#### About this post
<br>
This is my third month as a software developer and I had learned a lot practical skills and knowledge from the daily work\\
<br>
I noticed some developers in my workplace were using SourceTree, GitKraken and such Git-Based app to achieve the version control purpose.\\
<br>
However, I only use GitKraken when I want to quickly review the contents among different branches and I use Git-Bash for everything else. I am a not expert of Git, but the commands that I know serve me pretty well in my daily work. So I decide to write this post and summarize my experience to help any others who are interested about using Git.
<br>
Hopely, this will give someone a little help or inspiration.

<hr>
<br>

#### Commonly Used Commands:
<br>

~~~
cd <local_repos_path>
git checkout <existed_branch_name>
git checkout -b <new_branch_name>
git checkout -- .
git checkout <changed_file_path>
git branch -D <garbage_branch_name>
git push origin -delete <garbage_branch_name>
git status
git diff
git diff <changed_file_path>
git add --all
git add <changed_file_path>
git reset HEAD <staged_file_name>
git commit -m "message to describe commit"
git log
git log --oneline --graph --decorate
git push origin <current_branch_name>
git merge <merging_branch_name> --no-ff
git diff <from_commit> <to_commit> > <output_patch_path>
git apply <patch_file_path>
~~~

<br>

###### Description:
1. Before you do anything, always make sure you are in the local repository.
2. Swiching to a existed branch. <existed_branch_name> here has 2 meaning, one is that you have the copy of existed remote branch on your local machine, another is that you don't have the copy of existed remote branch on your local machine. The difference between these two situation, in simply words, you may switch to an outdated branch in the first situation, and the second situation will always give you the most updated situation, since git can not find a local copy of the remote branch, it will grab the current version on remote and make a local copy of it.
3. Branch off the current branch. If you want to start a new feature or fix a bug base which is based on a particular branch (usually master or develop branch), make sure you switch to that branch (by using git checkout). Then execute Line-3 commands. Line-3 is actually a combined command, which are made of "git branch <new_branch_name>" and "git checkout <new_branch_name>".
4. Remove ALL the changes which are not in staging area or committed yet.
5. Remove particular non-staging or non-comitted changes.
6. Remove an existed branch on your LOCAL machine. (Remote branch will not be affected)
7. Remove an existed branch on remote.
8. Display the current status of your local branch. (local file changes, comparison with remote version, etc.)
9. Display all the changes of your local branch since last commit.
10. Display the changes of a particular file in your local branch since last commit.
11. Move ALL the changes (modified, new file, etc) to the staging area and ready for committing.
12. Move a particular file to the staging area and ready for committing.
13. Remove a particular file from the staging area. (undo the git add).
14. Commit ALL the changes in staging area with a description (message is very important!) and ready for pushing to origin (remote).
15. Display the commit history.
16. Display the commit history in a more readble way.
17. Push all the commits from local machine to the remote. (This will UPDATE the remote branch!!!)
18. Merge a particular local branch to your current local branch WITHOUT fast forward (which means a individual commit will be created for this merge).
19. Create a patch which covers the changes between 2 commit points.
20. Apply a patch to the current branch.

<br>

###### NOTE:
- Utill you "PUSH", no changes will affect the remote, so it is completely safe to messing around in your local machine.

<br>

<hr>
> The commands above are the frequently used ones in my daily work and there are definitely more usefully commands that we should master to optimize our version control.\\
Next, I will use some common scenarios to demonstrate how to use these commands in combinations.
<hr>
<br>

#### Remote vs. Local
<br>

This used be a concept that confused me a lot when I first started learning git, but here are the simply ONE-WORD definitions to help you understand them.\\
<br>
Remote: Shared (Common)\\
Local: Non-Shared (Yours)\\
<br>

Simple enough right? Alright, here goes the details.\\
<br>
[Remote], you can understand it as a office and [Local] is considered as your home.
You know, as a software developer, we are able to work from home most of time (which is not completely true for most developer >.< Yeah, I know).
You will need to get your tasks from office (Remote) and bring them to home (Local) and start to work on them. Once you are done, you will need to go back to office and report (or return) your result to the office. The office get the finished work and store them to allow the entire office to share these work.\\
<br>
<hr>
<br>

#### When you need to work on something new (feature or bug)
<br>
Branch is very important!!!
For daily development, team usually has a main branch such as "master" or "develop" which should not never be a working branch at all. That means no one should ever work on the main branch for any fixes or features. The only thing that we will do to main branch is merging & branch-off.

Whenever you want to work on something, execute the following commands to create a separate branch base on the main branch (I will assume you are already in your local repository):\\
<br>
The __Commonly Used Commands__ command reference is [2]->[6]->[2]->[3]

<br>

~~~
git checkout other_Branch
git branch -D master
git checkout master
git checkout -b new_feature
~~~

<br>

If you work in a team environment, it is possible that your local main branch is outdated due to the pushed commits from your team members. Thus, before we branch off from the main branch, I recommand to ALWAYS grab the most updated main branch from remote. Some people will use "git fetch" & "git merge", well, I prefer to simply delete my local copy and grab it from remote directly, so that I don't have to deal with the merging pain.\\
<br>
<hr>
<br>

#### Save you work and Share it to others (add, commit & push)
<br>
The __Commonly Used Commands__ command reference is [7]->[8/9]->[10/11]->[13]->[15]->[16]

<br>

~~~
git status
git diff
git add --all
git commit -m "message to explain this commit"
git log --oneline --graph --decorate
git push origin current_branch_name
~~~

<br>

I strongly suggestion to frequently use [7], "git status" to track the current status of your current branch.\\
<br>
Next, before you add any changes to the staging area, if you saw you made a bunch of changed file, but  are not sure what changes that you made, [8/9] will help you pull the details for reviewing purpose. [7], [8], [9] will not make changes to your branch but just for auditing/reviewing/tracking purpose, so feel free to use them.\\
<br>
After you are confident about the changes, you are ready to add them to the staging area. Here are 2 options for staging, one is to stage particular changes, and another is to stage all the changes. The difference is depended on how you want your commit to cover those changes (e.g. 1 commit to cover all the changes, or several commits). By using [10] or [11] will do the trick for you.\\
<br>
Next, after the staging process, we need to make commit before the pushing. Remember, commit will simply bundle all the stagged changes into a single commit, and that's why we need to decide ahead what changes need to be added to the staging area. Always leave a meaningful but simple message to describe the commit. Your team will thank you for that (No, they won't...). Using [13] for this action.\\
<br>
After the commit, you can quickly review the commit history by using [15].\\
<br>
You can create multiple commits before you do the push. Push the commits to the origin will update the remote branch and that's how the changes will be shared within your team. [16] will do the trick.
<hr>
<br>

#### Feature/Fix is done (merge & conflicts)
<br>
The __Commonly Used Commands__ command reference is [2]->[6]->[2]->[17]

<br>

~~~
git checkout other_Branch
git branch -D master
git checkout master
git merge new_feature --no-ff
~~~

<br>

Before you start doing the merging, PLEASE!!! make sure you have the main branch on latest version. You team will thank you for doing this and it will make your life much easier, trust me.\\
To get the latest vesion of main branch, execute the Line-1~3. (which are [2], [6], [2])
<br>

Now, we are ready for the merging by using "git merge" ([17]) with the branch that you want to merge into the "master". Attention here, [--no-ff] is an optional, but I highly recommand it since it will create a separate commit as the merging point of "master" & "new_feature". It is just another professional practice to make the log history more readable.\\
<br>

Well, life is not always easy. Sometimes, there will be merge conflicts which require you to do the merge manual (git add & git commit).\\
<br>

~~~
<<<<<<<<<<<< HEAD
// codes
// ...
============
// conflicts_codes
// ...
>>>>>>>>>>>> merging_branch_name
~~~

<br>

In order to solve the merge conflicts, first of all, find the conflicts codes by looking for "<<< HEAD" or "=====" (these 2 patterns are pretty unique and you should locate the conflicts very easily by using them) and fix the conflicts.\\
<br>
As soon as all the conflicts are resolved, do the [git add --all] & [git commit -m "merge_conflicts_message"] to manually merge the changes.
<hr>
<br>

#### Create & Apply Patch
<br>

__&#60;from_commit&#62;__: is the commit point (commit hash) which we want the patch to start from and excluding this point.\\
<br>
__&#60;to_commit&#62;__: is the commit point (commit hash) which we want the patch to cover up to and including this point.\\
<br>
__&#60;output_patch_patch&#62;__: is the file name and location (path) for the patch. (the file should be names with ".diff")\\
<br>
 
NOTE: if either form_commit or to_commit are omitted, they will be assumed to be HEAD.\\
<br>

The codes below is a example of how to create a patch with commit hash.

<br>

~~~
$ git log --oneline -5

0f0840b commit msg 5
c248f0b commit msg 4
253f5f0 commit msg 3
410cf8e commit msg 2
c100172 commit msg 1
 
$ git diff 410cf8e 0f0840b > example_path.diff
~~~ 

<br>

After you have done with the patch, it is fairly easy to apply it. However, before you apply the patch, make sure you have checked out the branch that you want to apply the patch to (also make sure the version of it is updated).\\
<br>

~~~
git apply example_path.diff
~~~

<br>

<hr>

> Next Section is about some useful git commands that I had learned.\\
<br>
I didn't find them to be frequently used as the commands that I introduced above, but knowing them will definitely make your life easier.\\
<br>
(I will continuously update this post since I am still learning git. Also, if I have made any mistakes regarding Git, please leave comments or contact me, thank you!)
<hr>
<br>

#### Useful Commands
<br>

~~~
git ls-remote | grep <branch_partial_name>
~~~

<br>

1. First it will search all the branches on remote by using the "branch_partial_name" that you provided, then it will list the search results.

<br>
<hr>
<br>

#### Resources
- [Git Reference](https://git-scm.com/docs)
- [GitHub Cheat Sheet ](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
- [Visual Git Cheat Sheet](http://ndpsoftware.com/git-cheatsheet.html)
