from datetime import datetime

from entry import Entry

def parse(in_line):

    if 'Stage, Transaction Date, Posted Date, Card No., Description, Category, Debit, Credit' in in_line:
        return None

    line = in_line.split(',')

    if len(line) < 8:
        return None

    for i in range(0,len(line)):
        line[i] = line[i].replace('\n', '')

    date = datetime.strptime(line[1], '%m/%d/%Y')
    debit = credit = None
    try:
        debit = float(line[6])
    except:
        pass
    try:
        credit = float(line[7])
    except:
        pass

    desc = line[4]

    amount = debit if debit != None else credit * -1

    category = line[5]
    category = convert_category(desc, category)
    if amount < 0:
        category = 'credit'

    entry = Entry(date, amount, desc, category)

    if drop_line(entry):
        return None

    return entry

def convert_category(description, category):
    if category == 'Healthcare':
        return 'healthcare'
    if category == 'Dining':
        return 'eating out'
    if category == 'Phone/Cable':
        return 'bills'
    if category == 'Gas/Automotive':
        return 'transportation'
    if category == 'Other Travel':
        return 'transportation'
    if category == 'Payment':
        return 'credit'
    if category == 'Merchandise':
        if 'STOP & SHOP' in description or 'SHOPRITE' in description:
            return 'groceries'
        if 'PET GOODS' in description:
            return 'pet care'
        else:
            return 'shopping'

    return 'other'

def drop_line(entry):

    if entry.category == 'credit' and 'CAPITAL ONE ONLINE PYMT' in entry.description:
        return True

    return False
