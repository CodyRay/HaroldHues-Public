#!/bin/bash

#Todays date in ISO-8601 format:
DAY0=`date -I`
#Yesterdays date in ISO-8601 format:
DAY1=`date -I -d "1 day ago"`
#60 days ago in ISO-8601 format
DAY60=`date -I -d "60 days ago"`
#The source directory:
SRC="/files/"
#The target directory:
LOC="/archive/files/"
#The Specific backup location
TRG="$LOC$DAY0"
#The logs for the backup
LGS="$LOC/logs"
#The link destination directory:
LNK="$LOC$DAY1"
#The rsync options:
OPT="-avh --delete --link-dest=$LNK"

exec >>$LGS$DAY0.txt 2>&1
echo log file $DAY0 Created 
date
#Execute the backup
mount -a
echo rsync $OPT $SRC $TRG
if [ -d $LOC$DAY60 ]
then
echo Directoy to be Removed $LOC$DAY60
fi

rsync $OPT $SRC $TRG

#Delete the backup from 60 days ago, if it exists
if [ -d $LOC$DAY60 ]
then
echo Removing $LOC$DAY60
sudo rm -rf $LOC$DAY60
fi






#!/bin/bash

#Todays date in ISO-8601 format:
DAY0=`date -I`
#Yesterdays date in ISO-8601 format:
DAY1=`date -I -d "1 day ago"`
#60 days ago in ISO-8601 format
DAY60=`date -I -d "60 days ago"`
#The source directory:
SRC="/home/"
#The target directory:
TRG="/archive/users/$DAY0"
#The link destination directory:
LNK="/archive/users/$DAY1"
#The rsync options:
OPT="-avh --delete --link-dest=$LNK"

exec >>/archive/logs/users/$DAY0.txt 2>&1
echo log file $DAY0 Created
date
#Execute the backup
mount -a
echo rsync $OPT $SRC $TRG
if [ -d /archive/users/$DAY60 ]
then
echo Directoy to be Removed /archive/users/$DAY60
fi

rsync $OPT $SRC $TRG

#Delete the backup from 60 days ago, if it exists
if [ -d /archive/users/$DAY60 ]
then
echo Removing /archive/users/$DAY60
sudo rm -rf /archive/users/$DAY60
fi

