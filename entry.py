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
        'other'
    ]

    def __init__(self, date, amount, description, category):
        self.date = date
        self.amount = amount
        self.description = description

        if category not in self.CATEGORIES:
            category = 'other'

        self.category = category

    def to_string(self):
        return self.date.strftime('%m/%d/%Y') + ',' + str(self.amount) + ',' + self.description + ',' + self.category
