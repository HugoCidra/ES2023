#!/bin/bash

if [[ $(pwd) != *"/pl1/DEV/testing"* ]]; then
    echo -e "\n---------------------Please run this script from the testing directory. Exiting...---------------------\n"
    exit 1
fi

# Check if the user wants to generate a report
CONFIRMATION_MESSAGE="Are you sure you want to generate a report? (y/n): "
read -p "$CONFIRMATION_MESSAGE" resposta

if [ "$resposta" != "y" ]; then
    echo -e "\n---------------------Operation cancelled. Exiting...---------------------\n"
    exit 0
fi

mkdir -p testt

cd testt

# Create a loop that iterates through all directories in the current directory
for dir in ../REQ*; do
    dir_name=$(basename "$dir")
    mkdir "$dir_name"
    cd "$dir_name"
    

    # check if it is the req7 directory
    if [ "$dir_name" = "REQ7" ]; then
        cd ../../REQ7
        pytest "$dir" -v --alluredir="./../testt/$dir_name"
        cd ../testt/$dir_name
        continue
    fi

    pytest "../$dir" -v --alluredir="."

    cd ..
done

