#!/bin/bash

# Script: Ops 301 Class 05 Ops Challenges: Clearing Logs
# Author: Alexander Echols
# Date of Creation 17 Mar 2023
# Date of last revision: 17 Mar 2023    
# Purpose: Write a Bash script that will clear my logs

# main
# start by printing the size of the log files before we compress them
echo "How big it is!!!!!"
# we use the command "du -h" to display the disk usage in a human-readable format.
du -h /var/log/syslog /var/log/wtmp
# Next we need to create the backup directory and might as well create the timestamp as well.
Dir_Backup="/var/log/backups"
Time="$(date +%Y%m%d%H%M%S)"
# This step is where we compress the log files with the "tar" and 3 flags which are: 
#-c'creates new archive' -z'compresses the archive w/ gzip' & -f'specifies the filename of the archive. 
tar -czf "$Dir_Backup/syslog-$Time.tar.gz" /var/log/syslog
tar -czf "$Dir_Backup/wtmp-$Time.tar.gz" /var/log/wtmp
# Here is where we are going to clear the logs using the
cat /dev/null > /var/log/syslog
cat /dev/null > /var/log/wtmp
# We print the file size after the files are compressed
echo "How big it is now!!!!"
du -h "$Dir_Backup/syslog-$Time.tar.gz" "$Dir_Backup/wtmp-$Time.tar.gz"
# Finally we are going to compare the sizes of the compressed files against the original log files
echo "Big to small"
du -h /var/log/syslog /var/log/wtmp "$Dir_Backup/syslog-$Time.tar.gz" "$Dir_Backup/wtmp-$Time.tar.gz"

# End