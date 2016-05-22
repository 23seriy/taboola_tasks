#!/bin/bash

if [ "$#" -ne 1 ]; then
   echo "ERROR: The script requires one parameter - log URL!"
   exit 1
fi

url_path=$1
log_file_name=access_log

echo "delete the log file"
rm -f  $log_file_name
echo "download the access log"
wget --output-document=${log_file_name}.gz $url_path
echo "unzip the log file"
gzip -d $log_file_name

ls -lh $log_file_name

echo "sorted list of clients:"
cat $log_file_name | awk '{print$1}' | sort | uniq -c | sort 
