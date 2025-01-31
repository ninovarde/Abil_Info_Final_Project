!/bin/bash

echo "Make sure that the specified path is the correct one !"

# SPECIFY THE LOCATION WHERE YOU WOULD LIKE THE FOLDER TO BE CREATED:
path=/choose/the/location

# Make the directory 'Varde_AbInfo' in the specified location
mkdir $path/Varde_AbInfo

# Move this script to the created directory
script_directory=$(dirname "$0")
mv $script_directory/Bash_Script.sh $path/Varde_AbInfo

# Download the data and the Python script for data analysis from the given links 
wget -P $path/Varde_AbInfo https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/refs/heads/main/Nemo_6670.dat
wget -P $path/Varde_AbInfo https://raw.githubusercontent.com/ninovarde/Abil_Info_Final_Project/refs/heads/main/data_analysis.py

# Run the Python script to make the data analysis
python3 $path/Varde_AbInfo/data_analysis.py
