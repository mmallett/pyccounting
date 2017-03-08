import sys

import wells_fargo
import discover
import capital_one

for line in sys.stdin:

    # entry = wells_fargo.parse(line)
    # entry = discover.parse(line)
    entry = capital_one.parse(line)

    if entry == None:
        continue

    print entry.to_string()
