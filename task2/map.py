#!/usr/bin/python

# Call:
# hjs -D mapreduce.job.reduces=2 -files \
# /home/fnd212/BD/BD_A_01/task2 -mapper task2/map.py \
# -reducer task2/reduce.py -input \
# /user/ecc290/HW1data/parking-violations.csv \
# -output /user/fnd212/task2/task2.out

import sys
import csv

p_header = ['summons_number', 'issue_date', 'violation_code',
            'violation_county', 'violation_description',
            'violation_location', 'violation_precint',
            'violation_time', 'time_first_observed',
            'meter_number', 'issuer_code',
            'issuer_command', 'issuer_precinct',
            'issuing_agency', 'plate_id', 'plate_type',
            'registration_state', 'street_name',
            'vehicle_body_type', 'vehicle_color',
            'vehicle_make', 'vehicle_year']


# input comes from STDIN (stream data that goes to the program)
for entry in csv.reader(sys.stdin, delimiter=','):

    key = entry[p_header.index('violation_code')]
    print('{0}\t1'.format(key))

