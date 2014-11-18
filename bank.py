from account import Account

class Bank(object):
    def __init__(self):
      self.accounts = {}

    def add_account(self, account):
      self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
      return self.accounts.get(account_number)

    def withdraw(self, account_number, amt_withdraw):
    	account = Account("001",50)
        balance =  account.balance
        new_amount = balance - account.balance
        return new_amount

