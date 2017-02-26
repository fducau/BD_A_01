# !/usr/bin/python

import sys

# Expected format if entry coming from
# parking-violations:
# key \t inp_file plate_id, violation_precint, violation_code, issue_date

currentkey = None
counter = 0

for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Get key/value
    key, value = line.split('\t', 1)
    value = int(value)

    if key != currentkey:
        # If it is the first key
        if currentkey is None:
            counter += value
        else:
            # Generate output
            print('{1}\t{2}'.format(currentkey, counter))
            # Restart counter
            counter = value
    else:
        counter += value

    currentkey = key

# Compute/output result for the last key
print('{1}\t{2}'.format(currentkey, counter))
