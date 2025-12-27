#!/bin/bash

# Source directory to flatten (e.g., the current directory)
SOURCE_DIR="."

# Target directory for the flattened files
TARGET_DIR="./flattened_dir"

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Find all files recursively in the source directory
find "$SOURCE_DIR" -type f -print0 | while IFS= read -r -d '' file; do
    # Get the relative path of the file from the source directory
    relative_path="${file#"$SOURCE_DIR"/}"

    # Replace all '/' with '_' in the relative path to create the new filename prefix
    # Adjust the delimiter '_' as needed
    new_filename=$(echo "$relative_path" | tr '/' '_')

    # Construct the full destination path
    destination="$TARGET_DIR/$new_filename"

    # Move/rename the file to the target directory
    # Use 'cp' instead of 'mv' if you want to keep original files
    #mv "$file" "$destination"
    cp "$file" "$destination"
done

# Optional: Remove the original (now empty) subdirectories
# Use with caution: this removes all directories except the target directory itself
#find "$SOURCE_DIR" -mindepth 1 -not -path "$TARGET_DIR" -type d -exec rmdir {} +
