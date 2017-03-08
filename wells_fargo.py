from datetime import datetime

from entry import Entry

def parse(in_line):

    line = in_line.split(',')

    if len(line) < 5:
        return None

    for i in range(0,len(line)):
        line[i] = line[i].replace('"', '')
        line[i] = line[i].replace('\n', '')

    date = datetime.strptime(line[0], '%m/%d/%Y')
    amount = float(line[1])
    desc = line[4]

    category = ''
    if amount > 0:
        category = 'income'
    elif 'CON ED OF NY' in desc:
        category = 'bills'
    elif 'Apuovia LLC' in desc:
        category = 'rent'

    entry = Entry(date, amount, desc, category)

    if drop_line(entry):
        return None

    return entry

def drop_line(entry):

    if 'CAPITAL ONE ONLINE PMT' in entry.description or 'DISCOVER E-PAYMENT' in entry.description:
        return True

    if entry.category == 'income' and 'ONLINE TRANSFER FROM' in entry.description:
        return True

    return False
