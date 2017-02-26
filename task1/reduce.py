# !/usr/bin/python

import sys
import csv
import os


# Expected format if entry coming from
# parking-violations:
# key \t inp_file plate_id, violation_precint, violation_code, issue_date

currentkey = None
in_o_dataset = False
in_p_dataset = False

for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Get key/value
    key, values = line.split('\t', 1)
    values = values.split(', ')

    if key != currentkey:
        # If this is a new key and not the first key we've seen
        if currentkey:
            if in_p_dataset and not in_o_dataset:
                print('{}\t{}'.format(currentkey, ', '.join(p_values[1:])))

            # Restart the boolean values
            in_o_dataset = values[0] == 'o'
            in_p_datsaet = values[0] == 'p'
            if in_p_dataset:
                p_values = values

        # If is the first key
        else:
            if values[0] == 'o':
                in_o_dataset = True
            elif values[0] == 'p':
                in_p_dataset = True
                p_values = values

    # If we continue on the same key
    else:
        if values[0] == 'o':
            in_o_dataset = True
        elif values[0] == 'p':
            in_p_dataset = True
            p_values = values

    currentkey = key

# Compute/output result for the last key
if in_p_dataset and not in_o_dataset:
    if currentkey:
        print('{}\t{}'.format(currentkey, ', '.join(p_values[1:])))
