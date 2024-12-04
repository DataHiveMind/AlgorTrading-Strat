import pandas as pd
import backtrader as bt
from dataclasses import dataclass

from dataclasses import dataclass

@dataclass
class Trader(bt.Strategy):
    capital: float
    commission: float

    def buy(self, price, quantity):
        total_cost = price * quantity * (1 + self.commission)
        if total_cost > self.capital:
            raise ValueError("Insufficient capital for purchase.")
        self.capital -= total_cost
        return {"price": price, "quantity": quantity, "cost": total_cost}

    def sell(self, price, quantity):
        # Implement logic to track owned assets (quantity)
        # This example assumes the trader has enough to sell
        total_revenue = price * quantity * (1 - self.commission)
        self.capital += total_revenue
        return {"price": price, "quantity": quantity, "revenue": total_revenue}

    def hold(self):
        # This function can be used to track holding periods
        # and potentially calculate any holding costs
        pass