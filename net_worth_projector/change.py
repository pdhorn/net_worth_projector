from net_worth_projector.month import Month
from net_worth_projector.asset import Asset

class TransactionChange:
    def __init__(self, to_asset: Asset, start_date: Month, new_amount: float):
        self.to_asset = to_asset
        self.start_date = start_date
        self.new_amount = new_amount

class BalanceChange:
    def __init__(self, to_asset: Asset, effective_date: Month, new_balance: float):
        self.to_asset = to_asset
        self.effective_date = effective_date
        self.new_balance = new_balance
