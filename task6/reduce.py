# !/usr/bin/python

import sys

# Expected format if entry coming from
# parking-violations:
# plate, state \t #of violations
N = 20

currentkey = None
counter = 0
max_keys = [None] * N
max_violations = [- float('inf')] * N

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
            if counter > min(max_violations):
                ixmin = max_violations.index(min(max_violations))
                max_violations[ixmin] = counter
                max_keys[ixmin] = currentkey

            # Restart counter
            counter = value
    else:
        counter += value

    currentkey = key

# Compute/output result for the last key
if counter > min(max_violations):
    ixmin = max_violations.index(min(max_violations))
    max_violations[ixmin] = counter
    max_keys[ixmin] = currentkey

while max_violations:
    ixmax = max_violations.index(max(max_violations))
    print('{0}\t{1}'.format(max_keys[ixmax], max_violations[ixmax]))
    max_violations.pop(ixmax)
    max_keys.pop(ixmax)
