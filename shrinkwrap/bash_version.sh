#!/bin/bash

TARGET_SIZE=1000000   # Specify the target size in bytes
DIRECTORY=/path/to/starting/directory   # Specify the starting directory

function choose_directory {
    local dir=$1
    local size=$2
    local parent_size=$(du -s "$dir"/.. | awk '{print $1}')
    if ((size <= TARGET_SIZE)); then
        if ((size >= parent_size - size)); then
            echo "$(dirname "$dir")"
        else
            echo "$dir"
        fi
        return 0
    fi
    local chosen_dir=""
    local chosen_size=0
    for d in "$dir"/*/; do
        local sub_size=$(du -s "$d" | awk '{print $1}')
        if ((sub_size < size)); then
            if [[ -z $chosen_dir ]] || ((size - sub_size < size - chosen_size)); then
                chosen_dir="$d"
                chosen_size=$sub_size
            fi
        fi
    done
    if [[ -z $chosen_dir ]]; then
        echo "$(dirname "$dir")"
    else
        choose_directory "$chosen_dir" "$chosen_size"
    fi
}

function compress_and_remove {
    local dir=$1
    echo "Compressing directory: $dir"
    7z a "$dir".7z "$dir"
    rm -rf "$dir"
}

function process_directory {
    local dir=$1
    local size=$(du -s "$dir" | awk '{print $1}')
    local chosen_dir=$(choose_directory "$dir" "$size")
    compress_and_remove "$chosen_dir"
}

find "$DIRECTORY" -type d -exec bash -c 'process_directory "$0"' {} \;
