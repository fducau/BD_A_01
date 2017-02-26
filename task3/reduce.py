# !/usr/bin/python

import sys

# Expected format if entry coming from
# parking-violations:
# plate_id \t amount_due

currentkey = None
counter = 0
total = 0

for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Get key/value
    key, value = line.split('\t', 1)
    value = float(value)

    if key != currentkey:
        # If it is the first key
        if currentkey is None:
            total += value
            counter += 1
        else:
            # Generate output
            print('{0}\t{1:.2f}, {2:.2f}'.format(currentkey,
                                              total, total / counter))
            # Restart counter
            total = value
            counter = 1

    else:
        total += value
        counter += 1

    currentkey = key

# Compute/output result for the last key
print('{0}\t{1:.2f}, {2:.2f}'.format(currentkey,
                                  total, total / counter))
