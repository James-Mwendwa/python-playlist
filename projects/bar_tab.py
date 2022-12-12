class Tab:

    menu = {
        "wine": 14,
        "beer": 5,
        "beef": 10,
        "soft_drink": 4,
        "desert": 6,
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax = (tax / 100) * self.total
        service = (service / 100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f"{item} ${self.menu[item]}")

            print(f'{"Total"} ${total: .2f}')
