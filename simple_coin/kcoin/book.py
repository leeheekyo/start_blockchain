"""account book"""
import kcoin.config as cfg


class Account:
    def __init__(self):
        self.target = []  # sender or recipient
        self.amount = []  # - / + amount

    def sum(self):
        return sum(self.amount)

    def add(self, target, amount):
        self.target.append(target)
        self.amount.append(amount)


class Book:
    def __init__(self):
        self.account = {}

    def check_balance(self, transaction):
        # transaction : obj
        if transaction.sender == cfg.GENESIS_ACCOUNT_ID:  # for mining rewards
            return True
        if transaction.sender in self.account:
            account = self.account[transaction.sender]
            return account.sum() - transaction.amount >= 0
        else:
            return False

    def get_account(self, account_id):
        if account_id not in self.account:
            self.account[account_id] = Account()

        return self.account[account_id]

    def apply(self, transactions):
        # transactions : obj
        
        for t in transactions:
            sender = self.get_account(t.sender)
            recipient = self.get_account(t.recipient)

            sender.add(recipient, -t.amount)
            recipient.add(sender, t.amount)
