#!/bin/bash

url_path=$1
log_file_name=access_log

echo "delete the log file"
rm $log_file_name
echo "download the access log"
wget --output-document=${log_file_name}.gz $url_path
echo "unzip the log file"
gzip -d $log_file_name

ls -lh $log_file_name

echo "list of broken and/or relocated urls:"
cat $log_file_name | grep -v ' 200 ' | sed \$d | cut -d "\"" -f 2 | sed -e 's/HTTP\/1.0//g' | cut -d " " -f 2 
