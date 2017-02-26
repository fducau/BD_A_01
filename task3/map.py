#!/usr/bin/python

# Call:
# hjs -D mapreduce.job.reduces=2 -files \
# /home/fnd212/BD/BD_A_01/task3 -mapper task3/map.py \
# -reducer task3/reduce.py -input \
# /user/ecc290/HW1data/open-violations.csv \
# -output /user/fnd212/task3/task3.out

import sys
import csv

o_header = ['summons_number', 'plate',
            'license_type',
            'county', 'state', 'prescint',
            'issuing_agency', 'violation',
            'violation_status', 'issue_date',
            'violation_time', 'judgment_entry_date',
            'amount_due', 'payment_amount',
            'penalty_amount', 'fine_amount',
            'interest_amount', 'reduction_amount']


# input comes from STDIN (stream data that goes to the program)
for entry in csv.reader(sys.stdin, delimiter=','):

    key = entry[o_header.index('license_type')]
    value = entry[o_header.index('amount_due')]
    print('{0}\t{1}'.format(key, value))
