class Product:
    def __init__(self,id, name, brand ,buy_price, sell_price,quantity):
        self.id = id
        self.name = name
        self.brand = brand
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity

    def save (self):
        print(f"{self.id}-{self.name}-{self.brand}-{self.buy_price}-{self.sell_price}-{self.quantity} saved")
