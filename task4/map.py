# !/usr/bin/python

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
        print('{}\t{}'.format(key, value))
    else:
        print('{}\t{}'.format('Other', value))
