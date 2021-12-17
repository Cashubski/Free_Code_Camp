class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False    

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output


def create_spend_chart(cats):
    cat_names = []
    spent = []
    spent_perc = []

    for category in cats:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total -= item['amount']
        spent.append(round(total, 2))
        cat_names.append(category.name)

    for amount in spent:
        spent_perc.append(round(amount / sum(spent), 2) * 100)

    G = "Percentage spent by category\n"

    labels = range(100, -10, -10)

    for label in labels:
        G += str(label).rjust(3) + "| "
        for percent in spent_perc:
            if percent >= label:
                G += "o  "
            else:
                G += "   "
        G += "\n"

    G += "    ----" + ("---" * (len(cat_names) - 1))
    G += "\n     "

    longest_name_length = 0

    for name in cat_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)

    for i in range(longest_name_length):
        for name in cat_names:
            if len(name) > i:
                G += name[i] + "  "
            else:
                G += "   "
        if i < longest_name_length - 1:
            G += "\n     "

    return (G)
