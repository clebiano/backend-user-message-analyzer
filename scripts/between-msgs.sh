#!/bin/bash

# Check if the parameters were provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 input_file min_msgs max_msgs"
    exit 1
fi

# Define the parameters
input_file="$1"
min_msgs="$2"
max_msgs="$3"

# Check if the file exists
if [ ! -f "$input_file" ]; then
    echo "File not found: $input_file"
    exit 1
fi

find_users_in_message_range() {
    if [ $# -ne 3 ]; then
        echo "Error: This function requires three parameters"
        echo "Usage: find_users_in_message_range <input_file> <min_msgs> <max_msgs>"
        return 1
    fi

    local input_file="$1"
    local min_msgs="$2"
    local max_msgs="$3"

    awk -v min="$min_msgs" -v max="$max_msgs" '
    {
        msgs = $3 + 0
        if (msgs >= min && msgs <= max) {
            print $0
        }
    }' "$input_file"
}

find_users_in_message_range "$input_file" "$min_msgs" "$max_msgs"
