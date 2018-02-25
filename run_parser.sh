#!/bin/sh
FILEDIR="./data/sequoia-corpus+fct.mrg_strict"
PRODDIR="./prod/productions.txt"

TESTFILE="./data/test.txt"
TRAINFILE="./data/train.trees"
GOLDFILE="./data/test.trees"

PARSEFILE="./results/test_parsed.trees"


python2 ./commands/system.py $FILEDIR $TRAINFILE $TESTFILE $GOLDFILE 3099 5
python2 ./commands/pcfg_learn.py $TRAINFILE $PRODDIR
python2 ./commands/cykslover.py $PRODDIR $TESTFILE $PARSEFILE
python2 ./commands/evals.py $PARSEFILE $GOLDFILE
#python3 ./commands/preprocess.py $1 $2 $3 $PREPROCESSED

#python2 ./commands/system.py $PREPROCESSED $CONTEXT2VECDIR $DICTDIR $4 $5
