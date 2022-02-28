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

**git diff**: shows the difference between the working directory and the staging area
-  i.e., git diff changes.txt

**git commit**: permanently stores file changes from the staging area in the repository
-  i.e., git commit -m "made changes"
  -  git commit requires -m to note changes made (must be in quotes, written in present tense, and should be brief (50char or less)

**git log**: shows a list of all previous commits, stored chronologically
-  i.e., git log
  -  Shows *SHA* (40-character code that uniquely IDs the commit, appears in orange text)
  -  Commit author
  -  Date and time of commit
  -  The commit message
