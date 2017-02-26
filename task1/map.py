#!/usr/bin/python

import sys
import csv
import os
# cat matsmall.txt | python src/map.py 2 3 | sort -n | python src/reduce.py 5

o_header = ['summons_number', 'plate',
            'license_type',
            'county', 'state', 'prescint',
            'issuing_agency', 'violation',
            'violation_status', 'issue_date',
            'violation_time', 'judgment_entry_date',
            'amount_due', 'payment_amount',
            'penalty_amount', 'fine_amount',
            'interest_amount', 'reduction_amount']

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

    inp_file = os.environ.get('mapreduce_map_input_file')

    if 'parking' in inp_file:
        key = entry[p_header.index('summons_number')]
        plate_id = entry[p_header.index('plate_id')]
        violation_precint = entry[p_header.index('violation_precint')]
        violation_code = entry[p_header.index('violation_code')]
        issue_date = entry[p_header.index('issue_date')]

        print('{0}\tp, {1}, {2}, {3}, {4}'.format(key, plate_id, violation_precint,
                                                  violation_code, issue_date))

    elif 'open' in inp_file:
        key = entry[o_header.index('summons_number')]
        print('{0}\to'.format(key))
