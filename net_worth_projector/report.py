from typing import List
import pandas as pd
from net_worth_projector.asset import Asset
from net_worth_projector.month import Month

class Report:
    def __init__(self):
        self.history = {}
        self.initial_columns = ["pre_total", "post_total", "total"]
        self.balance_sheet = pd.DataFrame([], columns=self.initial_columns)
    
    def add_month_to_history(self, month: Month, assets: List[Asset]) -> None:
        self.history[month.__repr__()] = assets
    
    def add_month_to_balance_sheet(self, month: Month, assets: List[Asset]) -> None:
        for asset in assets:
            if asset.name not in self.balance_sheet.columns:
                self.balance_sheet[asset.name] = 0
        
        new_row = {asset.name: asset.balance for asset in assets}
        new_row["pre_total"] = sum([asset.balance for asset in assets if asset.tax == "pre"])
        new_row["post_total"] = sum([asset.balance for asset in assets if asset.tax == "post"])
        new_row["total"] = 0
        new_df = pd.DataFrame([], columns=self.balance_sheet.columns)
        new_df.loc[month.__repr__()] = new_row

        # self.balance_sheet.append(pd.Series(new_row), name=month.__repr__())
        self.balance_sheet = pd.concat([self.balance_sheet, new_df])
        self.balance_sheet = self.balance_sheet[[col for col in self.balance_sheet.columns if col not in self.initial_columns] + self.initial_columns]
        self.balance_sheet['total'] = self.balance_sheet.pre_total + self.balance_sheet.post_total
