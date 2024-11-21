# File Organizer Script

This Python script organizes files in the current directory into subfolders based on the first letter of their filenames. It provides options to create all letter folders (`A-Z`) or only the necessary ones based on the files present. Additionally, the script can delete itself after execution if desired.

## Features
- **Sorts files into letter-based folders**: Files are moved into folders named `A`, `B`, `C`, ..., based on the first letter of their filename.
- **Creates folders as needed**: Optionally, it only creates folders for the first letters of filenames that exist.
- **Deletes itself after execution**: Optionally, the script can delete itself after completing the file sorting task.
- **Gracefully handles file sorting**: Handles special characters in filenames, skips moving the script itself, and avoids errors when folders already exist.

## Prerequisites
- Python 3.x
- The script works on any platform (Linux, macOS, Windows) where Python is installed.

## Installation
1. Download or clone the repository to your local machine.
2. Move the script into the folder where you desire to organize you files.
3. Make sure Python 3.x is installed. You can verify by running:
   `python --version`
