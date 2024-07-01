#!/bin/bash

# Check if the input file was provided
if [ -z "$1" ]; then
    echo "Usage: $0 input_file [-desc]"
    exit 1
fi

# Define the input file
input_file="$1"

# Check if the file exists
if [ ! -f "$input_file" ]; then
    echo "File not found: $input_file"
    exit 1
fi

# Set the sorting mode variable
mode="asc"
if [ "$2" == "-desc" ]; then
    mode="desc"
fi

sort_users() {
    if [ $# -ne 2 ]; then
        echo "Error: This function requires two parameters"
        echo "Usage: sort_users <input_file> <mode>"
        return 1
    fi

    local input_file="$1"
    local mode="$2"

    if [ "$mode" == "desc" ]; then
        sort -rk1 "$input_file"
    else
        sort -k1 "$input_file"
    fi
}

sort_users "$input_file" "$mode"
