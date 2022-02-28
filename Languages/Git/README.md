# Git

git status: Check status of changes in the working directory
-  untracked files : Git sees the file but has not started tracking changes yet

git add: For Git to start tracking a file, it must first be added to the staging area
-  i.e., git add filename

git diff: Check the differences between the working directory and the staging area
-  i.e., git diff changes.txt

git commit: Permanently stores changes from the staging area inside the repository
-  i.e., git commit -m "made changes"
  -  git commit requires -m to note changes made (must be in quotes, written in present tense, and should be brief (50char or less)

git log: refer back to an earlier version of a project, stored chronologically
-  i.e., git log
  -  Shows *SHA* (40-character code that uniquely IDs the commit, appears in orange text)
  -  Commit author
  -  Date and time of commit
  -  The commit message
