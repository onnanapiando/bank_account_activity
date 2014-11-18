import unittest 
from account import Account

class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
      account = Account("001", 50)
      self.assertEqual(account.account_number, "001")
      self.assertEqual(account.balance, 50)
    
    def test_account_if_existing(self):
       account = Account("001", 50)
       self.assertEqual(account.existing_account(001), None)

if __name__ == '__main__':
    unittest.main()


