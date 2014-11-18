from account import Account

class Bank(object):
    def __init__(self):
      self.accounts = {}

    def add_account(self, account):
      self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
      return self.accounts.get(account_number)

    def withdraw(self, account_number, amt_withdraw):
      if self.accounts.get(account_number) - amt_withdraw:
          new_balance = self.accounts.get(account_number) - amt_withdraw
          return new_balance
      else:
          return 'Transaction Error'