import heapq
from typing import List


class Solution:
    def __init__(self):
        self.buy_backlog = []
        self.sell_backlog = []
        heapq.heapify(self.buy_backlog)
        heapq._heapify_max(self.sell_backlog)


    def handleOrder(self, amount, price, order_type):
        # Case for buy order
        if order_type == 0:
            while self.sell_backlog and amount > 0:
                lowest_sell_price = self.sell_backlog[0]
                if lowest_sell_price <= price:
                    heapq.heappop(self.sell_backlog)
                    amount -= 1
                    
            while amount > 0:
                heapq.heappush(self.buy_backlog, price)
                amount -= 1
            return
        
        # Case for sell order
        while self.buy_backlog and amount > 0:
            greatest_buy_price = self.buy_backlog[0]
            if greatest_buy_price >= price:
                heapq.heappop(self.buy_backlog)
                amount -= 1
        
        while amount > 0:
                heapq.heappush(self.sell_backlog, price)
                amount -= 1

        

    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        for order in orders:
            amount = order[0]
            price = order[1]
            order_type = order[2]

            self.handleOrder(amount, price, order_type)


        
        return (len(self.buy_backlog) + len(self.sell_backlog)) % (1e9 + 7)
