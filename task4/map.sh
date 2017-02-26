#!/bin/bash

# the Hadoop-streaming enviroment does not read the standard bash startup files,
# so we must use a wrapper to explicitly set up the modules environment and load 
# the relevant modules

# Call:
# hjs -D mapreduce.job.reduces=2 -files \
#		/home/fnd212/BD/BD_A_01/task3 -mapper task3/map.sh \
#		-reducer task3/reduce.sh -input \
#		/user/ecc290/HW1data/open-violations.csv \
#		-output /user/fnd212/task3.out

. /etc/profile.d/modules.sh
module load python
python task4/map.py
