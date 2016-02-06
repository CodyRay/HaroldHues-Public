#!/bin/bash
set -o errexit
# "I recently had a need to rewrite a git repository’s history. This isn’t 
# generally a very good idea, though it is useful if your repository contains 
# files it should not (such as unneeded large binary files or copyrighted 
# material). I also am using it because I had a branch where I only wanted to 
# merge a subset of files back into master (though there are probably better ways 
# of doing this). Anyway, it is not very hard to rewrite history thanks to the 
# excellent git-filter-branch tool which comes with git. However, if your goal 
# was to reduce a large repository’s size then git-filter-branch does not quite 
# finish the job since it makes temporary backups of the filtered out files. To 
# remove those, you need to do a little more work. To make it easier to 
# permanently remove files, I wrapped it in a little bash script 
# git-remove-history (also shown below) — simply go to the root of your 
# repository and run the script with the list of files you want to delete and it 
# will do the rest. There is an interesting thread about doing this here on 
# KernelTrap." - Author from thread
 
# Author: David Underhill
# http://dound.com/2009/04/git-forever-remove-files-or-folders-from-history/
# Script to permanently delete files/folders from your git repository.  To use 
# it, cd to your repository's root and then run the script with a list of paths
# you want to delete, e.g., git-delete-history path1 path2
 
if [ $# -eq 0 ]; then
    exit 0
fi
 
# make sure we're at the root of git repo
if [ ! -d .git ]; then
    echo "Error: must run this script from the root of a git repository"
    exit 1
fi
 
# remove all paths passed as arguments from the history of the repo
files=$@
git filter-branch -–index-filter “git rm -rf –cached –ignore-unmatch \”${files}\”" HEAD
 
# remove the temporary history git-filter-branch otherwise leaves behind for a long time
rm -rf .git/refs/original/ && git reflog expire --all &&  git gc --aggressive --prune
