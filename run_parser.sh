#!/bin/sh
FILEDIR=$1
PRODDIR="./prod/productions.txt"

TESTFILE="./data/test.txt"
TRAINFILE="./data/train.trees"
GOLDFILE="./data/test.trees"

PARSEFILE="./results/test_parsed.trees"


python2 ./commands/system.py $FILEDIR $TRAINFILE $TESTFILE $GOLDFILE $2 $3
python2 ./commands/pcfg_learn.py $TRAINFILE $PRODDIR
python2 ./commands/cykslover.py $PRODDIR $TESTFILE $PARSEFILE
python2 ./commands/evals.py $PARSEFILE $GOLDFILE

