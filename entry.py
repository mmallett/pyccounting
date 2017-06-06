class Entry:

    CATEGORIES = [
        'income',
        'bills',
        'healthcare',
        'rent',
        'transportation',
        'groceries',
        'shopping',
        'eating out',
        'fun',
        'petcare',
        'other',
        'credit'
    ]

    def __init__(self, date, account, amount, description, category):
        self.date = date
        self.account = account
        self.amount = amount
        self.description = description

        if category not in self.CATEGORIES:
            category = 'other'

        self.category = category

    def to_string(self):
        return self.date.strftime('%m/%d/%Y') + ',' + self.account + ',' + self.description + ',' + self.category + ',' + str(self.amount)
