#!/bin/bash

#The source directory:
SRC="/home/hoeftc/Versioning/Target/"
#The target directory:
LOC="/home/hoeftc/Versioning/"
#The logs for the backup
LGS="${LOC}logs"

if [ ! -d $LGS ]
then
mkdir $LGS
fi

exec >>$LGS/log.txt 2>&1
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
mv $LGS/log.txt $LGS/${FLD}_$date.txt
echo ''
#The rsync options: n is dry-run
OPT="-rltDvh --delete --link-dest=$LNK"



#Execute the backup
echo rsync $OPT $SRC $TRG

rsync $OPT $SRC $TRG

while inotifywait -re modify,move,delete,create $SRC; do

LNK="$TRG"
OPT="-rltDvh --delete --link-dest=$LNK"
let x=x+1
FLD=`printf "%03d" $x`
TRG=$LOC`printf "%03d" $x`
echo ''
echo rsync $OPT $SRC $TRG
echo ''
rsync $OPT $SRC $TRG

done
