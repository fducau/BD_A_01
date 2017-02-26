# !/usr/bin/python

import sys

# Expected format if entry coming from
# parking-violations:
# violation_code \t date, #violations
weekends = ['2016-03-05', '2016-03-06', '2016-03-12',
            '2016-03-13', '2016-03-19', '2016-03-20',
            '2016-03-26', '2016-03-27']
weekend_days = 8
week_days = 23

currentkey = None
total = 0
weekend_violations = 0
week_violations = 0

for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Get key/value
    key, values = line.split('\t', 1)
    date, value = values.split(', ')
    value = int(value)

    if key != currentkey:
        # If it is the first key
        if currentkey is None:
            total += value
            if date in weekends:
                weekend_violations += value
            else:
                week_violations += value
        else:
            weekend_avg = 1.0 * weekend_violations / weekend_days
            week_avg = 1.0 * week_violations / week_days
            print('{}\t{:.2f}, {:.2f}'.format(currentkey, weekend_avg,
                                              week_avg))

            # Restart counters
            total = value
            weekend_violations = 0
            week_violations = 0
            if date in weekends:
                weekend_violations += value
            else:
                week_violations += value

    else:
        total += value
        if date in weekends:
            weekend_violations += value
        else:
            week_violations += value

    currentkey = key

# Compute/output result for the last key
weekend_avg = 1.0 * weekend_violations / weekend_days
week_avg = 1.0 * week_violations / week_days
print('{}\t{:.2f}, {:.2f}'.format(currentkey, weekend_avg,
                                  week_avg))
