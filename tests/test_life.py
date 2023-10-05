import unittest
from net_worth_projector.asset import Asset
from net_worth_projector.life import Life
from net_worth_projector.month import Month
from net_worth_projector.transaction import Transaction
from net_worth_projector.change import TransactionChange

class TestLife(unittest.TestCase):
    def setUp(self):
        months = [
            Month(2020,1),
            Month(2020,2),
            Month(2020,3),
            Month(2020,4)
        ]
        assets = [
            Asset("one", 100, .10, "pre"),
            Asset("two", 100, .10, "pre")
        ]
        transactions = [
            Transaction(assets[0], 100, months[0], months[-1])
        ]
        events = [
            TransactionChange(assets[0], months[1], 200)
        ]
        self.life = Life(months[0], months[-1], assets, transactions, events)
    
    def test_do_contributions_no_mods(self):
        self.life.do_contributions()
        self.assertEqual(self.life.assets[0].balance, 200)
        self.assertEqual(self.life.assets[1].balance, 100)
    
    def test_get_new_transactions(self):
        same_transactions = Life.get_new_transactions(self.life.start_date, self.life.transactions, self.life.transaction_changes)
        self.assertEqual(len(self.life.transactions), len(same_transactions))
        self.assertEqual(self.life.transactions[0], same_transactions[0])

        second_month_transactions = [
            Transaction(self.life.assets[0], 200, self.life.start_date.next(), self.life.end_date)
        ]
        returned_transactions = Life.get_new_transactions(self.life.start_date.next(), self.life.transactions, self.life.transaction_changes)
        self.assertEqual(len(second_month_transactions), len(returned_transactions))
        self.assertEqual(second_month_transactions[0], returned_transactions[0])
    

if __name__ == '__main__':
    unittest.main()
