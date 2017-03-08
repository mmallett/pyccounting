import sys

import wells_fargo

for line in sys.stdin:

    entry = wells_fargo.parse(line)

    if entry == None:
        continue

    print entry.to_string()
