# !/usr/bin/python

import sys

# Expected format if entry coming from
# parking-violations:
# plate, state \t #of violations

currentkey = None
counter = 0
max_violations = - float('inf')

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
            # Keep track of maximum
            if counter > max_violations:
                max_key = currentkey
                max_violations = counter
            # Restart counter
            counter = value
    else:
        counter += value

    currentkey = key

# Compute/output result for the last key
if counter > max_violations:
    max_key = currentkey
    max_violations = counter

print('{0}\t{1}'.format(max_key, max_violations))
