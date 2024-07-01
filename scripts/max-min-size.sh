#!/bin/bash

# Check if the input file was provided
if [ -z "$1" ]; then
    echo "Usage: $0 input_file [-min]"
    exit 1
fi

# Define the input file
input_file="$1"

# Check if the file exists
if [ ! -f "$input_file" ]; then
    echo "File not found: $input_file"
    exit 1
fi

# Set the variable for the mode (max or min)
mode="max"
if [ "$2" == "-min" ]; then
    mode="min"
fi

find_user_by_message_size() {
    if [ $# -ne 2 ]; then
        echo "Error: This function requires two parameters"
        echo "Usage: find_user_by_message_size <input_file> <mode>"
        return 1
    fi

    local input_file="$1"
    local mode="$2"

    awk -v mode="$mode" '
    {
        size = $5 + 0

        if (mode == "max") {
            if (NR == 1 || size > max_size) {
                max_size = size
                max_line = $0
            }
        }
        else if (mode == "min") {
            if (NR == 1 || size < min_size) {
                min_size = size
                min_line = $0
            }
        }
    }
    END {
        if (mode == "max") {
            print max_line
        }
        else if (mode == "min") {
            print min_line
        }
    }' "$input_file"
}

find_user_by_message_size "$input_file" "$mode"
