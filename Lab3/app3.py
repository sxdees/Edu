class Order:
    def __init__(self, n, p, q):
        self.n = n  
        self.p = p  
        self.q = q  

class Store:
    def __init__(self):
        self.orders = []  

    def add_order(self, n, p, q):
        order = Order(n, p, q)
        self.orders.append(order)

    def total_price(self):
        total = 0
        for order in self.orders:
            total += order.p * order.q
        return total

    def print_receipt(self):
        print("=== Чек ===")
        for order in self.orders:
            print(f"{order.n} x{order.q} = {order.p * order.q}")
        print(f"Общая сумма: {self.total_price()}")

store = Store()
store.add_order("Яблоки", 2.5, 3)
store.add_order("Бананы", 1.8, 5)
store.print_receipt()
