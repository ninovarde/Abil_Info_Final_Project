#!/bin/bash

echo "Make sure that the specified path is the correct one !"

# SPECIFY THE LOCATION WHERE YOU WOULD LIKE THE FOLDER TO BE CREATED:
path=/home/ABINFO/Desktop

# Make the directory 'Varde_AbInfo' in the specified location
mkdir $path/Varde_AbInfo

script_directory=$(dirname "$0")
mv $script_directory/Bash_Script.sh $path/Varde_AbInfo
