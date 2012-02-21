#!/bin/env bash
CLEANDATADIR=../cleandata
CLEANDATADIR_BCK=../cleandata_bck

# first test: check with grep
echo "Checking with grep. If there is no output, is good news"
grep ': N' $CLEANDATADIR/*
echo "End of the test with grep"

echo "Please press enter to continue:"
read

# second test: run a diff for every file inside 
# the cleandata a cleandata_bck directory
echo "Checking with strict diff per file. "
echo "Original data assumed in $CLEANDATADIR_BCK/"
echo "Processed data assumed in $CLEANDATADIR/"
echo "If differences show M and N, is good news."
for a in $(ls $CLEANDATADIR/); do
    diff $CLEANDATADIR/$a $CLEANDATADIR_BCK/$(basename $a)
done


echo "Test finished."
