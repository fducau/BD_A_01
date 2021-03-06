#!/usr/bin/python

# Call:
# hjs -D mapreduce.job.reduces=2 -files \
# /home/fnd212/BD/BD_A_01/task4 -mapper task4/map.py \
# -reducer task4/reduce.py -input \
# /user/ecc290/HW1data/parking-violations.csv \
# -output /user/fnd212/task4/task4.out

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

    key = entry[p_header.index('registration_state')]
    value = '1'
    if key == 'NY':
        print('{0}\t{1}'.format(key, value))
    else:
        print('{0}\t{1}'.format('Other', value))
