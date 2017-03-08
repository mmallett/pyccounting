from datetime import datetime

from entry import Entry

def parse(in_line):

    if 'Trans. Date,Post Date,Description,Amount,Category' in in_line:
        return None

    line = in_line.split(',')

    if len(line) < 5:
        return None

    for i in range(0,len(line)):
        line[i] = line[i].replace('"', '')
        line[i] = line[i].replace('\n', '')

    date = datetime.strptime(line[0], '%m/%d/%Y')
    amount = float(line[3])
    desc = line[2]

    category = ''
    if amount < 0:
        category = 'credit'
    elif 'METRO-NORTH' in desc :
        category = 'transportation'

    entry = Entry(date, amount, desc, category)

    if drop_line(entry):
        return None

    return entry

def drop_line(entry):

    if entry.category == 'credit' and 'INTERNET PAYMENT - THANK YOU' in entry.description:
        return True

    return False
