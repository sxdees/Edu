class Order:
    
    def __init__(self, name: str, price: float, quantity: int):
        self._name = name  
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def get_total_price(self) -> float:
        return self._price * self._quantity


class Store:

    def __init__(self):
        self._orders = []  

    def add_order(self, name: str, price: float, quantity: int):
        order = Order(name, price, quantity)
        self._orders.append(order)

    def total_price(self) -> float:
        return sum(order.get_total_price() for order in self._orders)

    def get_orders(self):
        return self._orders


class ReceiptPrinter:
    
    @staticmethod
    def print_receipt(store: Store):
        print("=== Чек ===")
        for order in store.get_orders():
            print(f"{order.name} x{order.quantity} = {order.get_total_price()}")
        print(f"Общая сумма: {store.total_price()}")


store = Store()
store.add_order("Яблоки", 2.5, 3)
store.add_order("Бананы", 1.8, 5)

ReceiptPrinter.print_receipt(store)
