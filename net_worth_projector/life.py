from typing import List
from net_worth_projector.asset import Asset
from net_worth_projector.month import Month
from net_worth_projector.asset import Asset
from net_worth_projector.report import Report
from net_worth_projector.transaction import Transaction
from net_worth_projector.change import TransactionChange, BalanceChange


class Life:
    def __init__(self,
                 start_date: Month,
                 end_date: Month,
                 assets: List[Asset],
                 transactions: List[Transaction],
                 transaction_changes: List[TransactionChange],
                 balance_changes: List[BalanceChange]):
        self.report = Report()
        self.current_date = start_date
        
        self.start_date = start_date
        self.end_date = end_date
        self.assets = assets
        self.transactions = transactions
        self.transaction_changes = transaction_changes
        self.balance_changes = balance_changes

        # find TransactionChanges where the target account may not have any transactions yet
        # and create empty transactions for it
        for change in self.transaction_changes:
            found_transaction = False
            for t in self.transactions:
                if t.to_asset == change.to_asset:
                    found_transaction = True
            if not found_transaction:
                self.transactions.append(Transaction(change.to_asset, 0, self.start_date, self.end_date))

    def step(self) -> None:
        self.current_date = self.current_date.next()
    
    def do_contributions(self) -> None:
        for t in self.transactions:
            t_a = t.to_asset
            if t.end_date >= self.current_date:
                for a in self.assets:
                    if a == t_a:
                        a.update_balance(t.amount)
    
    def tweak_transactions(self) -> None:
        ''' call get_new_transactions and updates transactions to this '''
        self.transactions = Life.get_new_transactions(self.current_date, self.transactions, self.transaction_changes)
    
    @staticmethod
    def get_new_transactions(current_date: Month, transactions: List[Transaction], events: List[TransactionChange])\
        -> List[Transaction]:
        # adjust each transaction that has a change, else keep it
        return_transactions = []
        for t in transactions:
            matching_event_found = False
            for e in events:
                if t.to_asset == e.to_asset and current_date == e.start_date:
                    matching_event_found = True
                    new_t = Transaction(e.to_asset, e.new_amount, e.start_date, t.end_date)
            if matching_event_found:
                return_transactions.append(new_t)
            else:
                return_transactions.append(t)
        return return_transactions
    
    def handle_balance_changes(self) -> None:
        for bc in self.balance_changes:
            if self.current_date == bc.effective_date:
                for a in self.assets:
                    if bc.to_asset == a:
                        a.balance = bc.new_balance
    
    def grow_assets(self) -> None:
        for a in self.assets:
            a.grow()

    def update_report(self) -> None:
        self.report.add_month_to_history(self.current_date, self.assets)
        self.report.add_month_to_balance_sheet(self.current_date, self.assets)
    
    def run(self, display_report_every: int =12) -> None:
        steps = 0
        while self.current_date <= self.end_date:
            self.tweak_transactions()
            self.do_contributions()
            self.grow_assets()
            self.handle_balance_changes()
            self.update_report()
            if steps % display_report_every == 0:
                print(f"\n\nBalance at {self.current_date}: \n", self.report.balance_sheet.tail(1))
            steps += 1
            self.step()