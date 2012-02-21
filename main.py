#!/bin/env python
'''
First python exercise
'''

# import of std modules
import sys,os

# function to find all filenames and returns a list
def get_filenames(path):
    return os.listdir(path)

# is the answer a N?
def has_N(line):
    # convert to lower and split the line by using : as separator
    tmp_line = line.upper().split(':')
    # check if the first field is N
    if 'N' == tmp_line[1].strip(): return True
    return False

# main function
def main():
    # testing
    # print get_filenames(sys.argv[1])
    print has_N('Sex: N')
    print has_N('Sex: n')
    print has_N('Sex:N')
    print has_N('Sex:n')
    print has_N('Sex:meme')
    print has_N(':N')
    print has_N('N:sex')

# call main
main()



