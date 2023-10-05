from __future__ import annotations
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Month:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
    
    def __repr__(self):
        return str(self.year) + "-" + '{:02d}'.format(self.month)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    
    def __gt__(self, other):
        return self.year > other.year or (self.year >= other.year and self.month > other.month)
    
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def asDatetime(self) -> datetime:
        return datetime(self.year, self.month, 1)
    
    def next(self) -> Month:
        next_month = self.asDatetime() + relativedelta(months=1)
        return Month(next_month.year, next_month.month)
