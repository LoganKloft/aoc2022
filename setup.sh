#!/bin/bash

# Define the starting and ending day numbers
START_DAY=1
END_DAY=25

# Loop from START_DAY to END_DAY
for i in $(seq $START_DAY $END_DAY); do
    # Create the folder name
    FOLDER_NAME="day_$i"

    # Create the directory
    mkdir -p "$FOLDER_NAME"

    # Check if the directory was created successfully
    if [ $? -eq 0 ]; then
        # Create the files inside the folder
        touch "$FOLDER_NAME/input.txt"
        touch "$FOLDER_NAME/puzzle1.py"
        touch "$FOLDER_NAME/puzzle2.py"
    else
        echo "Error: Could not create folder $FOLDER_NAME"
    fi
done
