from net_worth_projector.asset import Asset
from net_worth_projector.month import Month
from net_worth_projector.asset import Asset
from net_worth_projector.life import Life
from net_worth_projector.transaction import Transaction
from net_worth_projector.change import TransactionChange, BalanceChange

if __name__ == "__main__":
    investment_return_rate = 0.10
    start = Month(2023,9)
    end = Month(2043,9)
    assets = [
            Asset("roth_ira", 200000, investment_return_rate, "post"), # 200k initial balance in roth ira
            Asset("401k", 125000, investment_return_rate, "post"), # 125k initial balance in 401k
            Asset("college", 113000, investment_return_rate, "pre"), # 113k initial college savings
            Asset("house", 300000, 0.05, "pre"), # house worth 300k
            Asset("after_house", 0, investment_return_rate, "pre"), # initialize 0 balance account for saving after house paid fof
    ]
    asset_dict = {a.name: a for a in assets}
    transactions = [
        Transaction(asset_dict["roth_ira"], (13000.0)/12, start, end), # max out roth ira for 2 adults
        Transaction(asset_dict["401k"], 22500.0/12, start, end), # max out 401k for 1 adult
        Transaction(asset_dict["college"], 2000, start, end),
    ]
    transaction_changes = [
        TransactionChange(asset_dict["college"], Month(2028,9), 1000), # stop contributing to kid1 college
        TransactionChange(asset_dict["college"], Month(2031,9), 0), # stop contributing to kid2 college
        TransactionChange(asset_dict["after_house"], Month(2025,9), 2000), # once house paid off, put payment into pre-tax investment
    ]
    balance_changes = [
        BalanceChange(asset_dict["college"], Month(2035, 9), 0), # zero out college to pay for tuition
    ]
    life = Life(start, end, assets, transactions, transaction_changes, balance_changes)
    life.run()