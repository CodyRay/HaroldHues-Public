#!/bin/bash
NOW=$(date +"%Y-%m-%d-%H%M")
FILE="kopacznursery-full.$NOW.tar"
BACKUP_DIR="/home3/kopacznu/backups"
WWW_DIR="/home3/kopacznu/public_html/"

DB_USER="wordpress"
DB_PASS="password"
DB_NAME="wordpress"
DB_FILE="database.$NOW.sql"

WWW_TRANSFORM='s,^home3/kopacznu/public_html,www,'
DB_TRANSFORM='s,^home3/kopacznu/backups,database,'

tar -cvf $BACKUP_DIR/$FILE --transform $WWW_TRANSFORM $WWW_DIR
mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/$DB_FILE

tar --append --file=$BACKUP_DIR/$FILE --transform $DB_TRANSFORM $BACKUP_DIR/$DB_FILE
rm $BACKUP_DIR/$DB_FILE
gzip -9 $BACKUP_DIR/$FILE
