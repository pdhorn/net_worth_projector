class Asset:
    def __init__(self, name: str, initial_balance: float, growth_rate: float, tax: str):
        self.name = name
        self.balance = initial_balance
        self.initial_balance = initial_balance
        self.growth_rate = growth_rate
        self.tax = tax
    
    def __repr__(self):
        return "Asset: " + self.name
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False
    
    def grow(self) -> None:
        monthly_growth_multpilier = (1 + self.growth_rate) ** (1.0 / 12)
        self.balance = round(self.balance * monthly_growth_multpilier, 2)
    
    def update_balance(self, addition: float) -> None:
        self.balance += addition
