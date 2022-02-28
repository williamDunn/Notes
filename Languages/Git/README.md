# Git

https://education.github.com/git-cheat-sheet-education.pdf
------------------

## Git Commands

**git init**: creates a new Git repository

**git status**: inspects the contents of the working directory and staging area
-  Check status of changes in the working directory
-  untracked files : Git sees the file but has not started tracking changes yet

**git add**: adds files from the working directory to the staging area
-  For Git to start tracking a file, it must first be added to the staging area
-  i.e., git add filename
  -  git add filename1 filename2, git add*

**git diff**: shows the difference between the working directory and the staging area
-  i.e., git diff changes.txt

**git commit**: permanently stores file changes from the staging area in the repository
-  i.e., git commit -m "made changes"
  -  git commit requires -m to note changes made (must be in quotes, written in present tense, and should be brief (50char or less)
-  Ability to correct mistakes and edit commits easily instead of creating a completely new commit
  -  To do this, create your changes, stage them with *git add* and then type *git commit --amend* to update your previous commit
    -  i.e., git commit -ammend  
  -  if you want to keep the same commit message, *git commit --amend --no-edit*

**git log**: shows a list of all previous commits, stored chronologically
-  i.e., git log
  -  Shows *SHA* (40-character code that uniquely IDs the commit, appears in orange text)
  -  Commit author
  -  Date and time of commit
  -  The commit message
-  Show list of coommits in one line format
  -  i.e., git log --oneline
-  display a list of commits that contains a keyword
  -  i.e., git log -S "keyword"
-  Display a visual representation of how the brnaches and commits were created in order to help you make sense of your repository history
  -  i.e., git log --graph OR git log --online --graph

**git stash**: when you want to record the current state of the working directory and the index, but want to go back to a clean working directory
-  i.e., git stash (will store you current work temporarily for later use in a hidden directory)
-  then 'git stash pop'

**git push -u origin**: push to origin remote repo

**git clone <url>**: Clone existing remote repo
  
**git <command> -help**: Get help for specific command
  
**git branch**: list all local branches
-  git branch -d <branch>: delete branch
-
------------------------
## Backtracking

**head commit**: the commit you are currently on, or in many cases the most recently made commit is the *head* commit
-  i.e., git show HEAD

**git checkout**: command will restore the file in your working directory to what it was when you last made a commit
-  i.e., git checkout HEAD filename

**git reset**: unstage a certain file from the staging area (will reset to be the same as the HEAD commit)
-  i.e., git reset HEAD filename
-  i.e., git reset commit_SHA(SHA id number)
