# !/usr/bin/python

import sys

# Expected format if entry coming from
# parking-violations:
# registration_state \t #of violations

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
            counter += 1
        else:
            # Generate output
            print('{}\t{}'.format(currentkey, counter))
            # Restart counter
            counter = 1
    else:
        counter += 1

    currentkey = key

# Compute/output result for the last key
print('{}\t{}'.format(currentkey, counter))