import sys

import wells_fargo
import discover
import capital_one

mode = sys.argv[1] or 'other'

for line in sys.stdin:

    entry = None
    if mode == 'wells_fargo':
        entry = wells_fargo.parse(line)
    if mode == 'discover':
        entry = discover.parse(line)
    if mode == 'capital_one':
        entry = capital_one.parse(line)

    if entry == None:
        continue

    print entry.to_string()
