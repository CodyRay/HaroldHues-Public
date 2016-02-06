#!/bin/bash
DATE =`date -I`

git add Code &&
git commit -m "Automatic Commit: $DATE" &&
git push
