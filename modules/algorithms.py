"""
Written by: Hovig Ohannessian
Email: hovigg@hotmail.com
"""

import sys


# Function to open each file
def open_file(filename, file_opening_mode):
    try:
        # Open file
        myfile = open(filename, file_opening_mode)
    except IOError:
        print("Cannot open file " , filename, " - exiting!\n")
        sys.exit(1)
    return myfile


# Function to read from each file
def read_all_lines_from_file(file):
    # Read the lines
    all_lines = file.readlines()
    if not all_lines:
        print("Empty file.\n")
    # Close file
    file.close()
    return all_lines
