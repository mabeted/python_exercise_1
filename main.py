#!/bin/env python
'''
First python exercise
'''

# import of std modules
import sys, os, shutil

# function to find all filenames and returns a list
def get_filenames(path) :
    return os.listdir(path)

# is the answer a N?
def has_N(line) :
    # convert to lower and split the line by using : as separator
    tmp_line = line.replace('\n', '').replace(' ', '')
    tmp_line = tmp_line.upper().split(':')
    # check if the first field is N
    if len(tmp_line)>1 and 'N' == tmp_line[1].strip(): return True
    return False

# change N to M
def fix_N(filename) :
    # open tmp_file
    tmp_filename = filename + '_tmp'
    shutil.copyfile(filename, tmp_filename)
    ifile = open(filename, 'r')
    ofile = open(tmp_filename, 'w')
    # process each line
    for line in ifile :
        if has_N(line):
            line = line.replace('N', 'M')
        ofile.write(line)
    # move to new name
    shutil.move(tmp_filename, filename)


# main function
def main():
    # save current data dir
    oldcwd = os.getcwd()
    # move to new data dir
    os.chdir(sys.argv[1])
    for filename in get_filenames('./'):
        fix_N(filename)
    #return to old wd
    os.chdir(oldcwd)
        

# call main
main()



