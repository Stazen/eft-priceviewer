class Item:
    def __init__(self, name, short_name, normalized_name, sell_for):
        self.name = name
        self.short_name = short_name
        self.normalized_name = normalized_name
        self.sell_for = sell_for

class Vendor:
    def __init__(self, name):
        self.name = name

class Price:
    def __init__(self, vendor, price, currency):
        self.vendor = vendor
        self.price = price
        self.currency = currency