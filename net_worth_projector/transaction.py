from net_worth_projector.asset import Asset
from net_worth_projector.month import Month

class Transaction:
    def __init__(self, to_asset: Asset, amount: float, start_date: Month, end_date: Month):
        self.to_asset = to_asset
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
