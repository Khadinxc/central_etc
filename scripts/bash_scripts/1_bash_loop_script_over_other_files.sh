#!/bin/bash

Archives_dir="/root/home"

# gets the folder name where the script is run from which should be the year and month eg 202210
For file in "$archives_dir"/*t3_oe_4_${PWD##*/}*".zip"
Do
  mkdir temp
  echo "unzipping file $file to the temp directory"
  for unzipped_file in temp/*"table"
  do
    echo "sending events from file $unzipped_file"
    python2 ../scriptname.py $unzipped_file #uncomment to save events in the output file
  done
  rm -rf temp
