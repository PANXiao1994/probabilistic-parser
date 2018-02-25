# probabilistic-parser
a basic probabilistic parser for French based on the CYK algorithm and the PCFG model.

## Requirements
For running successfully this system, you need python 2.7.

## Quick-start
Open the terminal, run the command below:

```
sh run_parser.sh [file] [train_num] [test_num]
```
* [file]: The input file: some of lines will be used for training, some will be used for test.
* [train_num]: the first several lines in [file] used for training(learning PCFG probas).
* [test_num]: the last several lines in [file] used for test.

### Example
```
sh run_parser.sh ./data/sequoia-corpus+fct.mrg_strict 3098 5
```
This will take 1-3098 lines in the file "./data/sequoia-corpus+fct.mrg_strict"(totally 3099 lines) as train file, and take 3095-3099 lines in the file as test file.

## run_parser.sh

```
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
```


* FILEDIR: The input file path
* PRODDIR: The file storing the result of PCFG
* TESTFILE: The file storing the sentences of test lines
* TRAINFILE: The file storing the parsed tree of train lines
* GOLDFILE: The file storing the parsed tree of test lines
* PARSEFILE: The file storing the parsed tree of test lines derived from the algorithm


