#!/usr/bin/env bash
NOW=$(date +"%Y-%m-%d-%H%M")
FILE="kopacznursery-no-media.$NOW.tar"
BACKUP_DIR="/home3/kopacznu/backups"
WWW_DIR="/home3/kopacznu/public_html"

DB_USER="wordpress"
DB_PASS="password"
DB_NAME="wordpress"
DB_FILE="database.$NOW.sql"

WWW_TRANSFORM='s,^home3/kopacznu/public_html,www,'
DB_TRANSFORM='s,^home3/kopacznu/backups,database,'
echo $NOW
echo ""
echo "These are the Pre-Existing Backups"
tree -L 1 -h -P "*.tar.gz" /home3/kopacznu/backups/
echo "If there are too many then there may be a problem with the off-site backup not deleting them."
echo ""
echo "Compressing Wordpress Files..."
tar --exclude=$WWW_DIR/wp-content/uploads -cf $BACKUP_DIR/$FILE --transform $WWW_TRANSFORM $WWW_DIR/ &&
echo "Tar Didn't Report any Errors" ||
echo "Errors Were Reported" 
echo ""
echo "Exporting Wordpress Database..."
mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/$DB_FILE
echo ""
echo "Appending Wordpress Database File to Backup..."
tar --append --file=$BACKUP_DIR/$FILE --transform $DB_TRANSFORM $BACKUP_DIR/$DB_FILE
echo ""
echo "Compressing Non-Media Backup File Again..."
gzip -9 $BACKUP_DIR/$FILE
echo ""
echo "Removing Uncompressed Version of Database File..."
rm $BACKUP_DIR/$DB_FILE
echo ""
echo "Synchronizing Media in Uploads Folder..."
echo "rsync -rLtDvzh --delete $WWW_DIR/wp-content/uploads/ $BACKUP_DIR/uploads/"
rsync -rLtDvzh --delete $WWW_DIR/wp-content/uploads/ $BACKUP_DIR/uploads/ &&
echo "Rsync Didn't Report any Errors" ||
echo "Errors Were Reported" 
echo ""
