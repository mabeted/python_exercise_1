#!/bin/env python
'''
First python exercise
'''

# import of std modules
import sys,os

# function to find all filenames and returns a list
def get_filenames(path):
    return os.listdir(path)

# main function
def main():
    # testing
    print get_filenames(sys.argv[1])


# call main
main()



