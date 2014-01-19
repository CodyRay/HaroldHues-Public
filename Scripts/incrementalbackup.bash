#!/bin/bash

#Todays date in ISO-8601 format:
DAY0=`date -I`
#Folder Number
#FLD
#The source directory:
SRC="/home/hoeftc/Storage/"
#The target directory:
LOC="/media/Passport/"
#The Specific backup location
#TRG="$LOC$DAY0"
#The logs for the backup
LGS="${LOC}logs"
#The link destination directory:
#LNK="$LOC$DAY1"

if [ ! -d $LGS ]
then
mkdir $LGS
fi

exec >>$LGS/$DAY0.txt 2>&1
echo log file $DAY0 Created 
echo $DAY0
date
echo ''
echo The Source Directory: $SRC
echo The Backup Directory: $LOC
echo ''

#for ((x=1;x<=5;x+=1)); do 
XEXIST=1
x=0
LNK=$LOC`printf "%03d" 0`
while [ $XEXIST -eq 1 ]; do
	let x=x+1
	FLD=`printf "%03d" $x`
	TRG=$LOC`printf "%03d" $x`
	if [ -d $TRG ]
		then
		echo Directoy $TRG exists
		LNK="$TRG"
		else
		echo Directoy $TRG Doesn\'t exist
		XEXIST=0
	fi
done

echo ''

if [ ! -d $LNK ]
then
echo ''
echo Creating Directory $LNK
echo ''
mkdir $LNK
fi

echo Changing name of file to $FLD.txt
mv $LGS/$DAY0.txt $LGS/$FLD.txt
echo ''
#The rsync options: n is dry-run
OPT="-rltDvh --delete --link-dest=$LNK"



#Execute the backup
echo rsync $OPT $SRC $TRG

rsync $OPT $SRC $TRG

cat $LGS/$FLD.txt
