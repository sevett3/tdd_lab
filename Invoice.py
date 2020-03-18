class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    # Owner: Erik Salazar
    # Finding the most expensive product price
    def mostExpensiveProductPrice(self, products):
        most_expensive_product_price = 0
        for k, v in products.items():
            if float(v['unit_price']) > most_expensive_product_price:
                most_expensive_product_price = float(v['unit_price'])
        return most_expensive_product_price

    # Owner: Joshua Ellis
    # Finding the total average impure price
    def averageImpurePrice(self, products):
        total_items = 0
        for k, v in products.items():
            total_items += int(v['qnt'])
        average_impure_price = round(self.totalImpurePrice(products) / total_items, 2)
        return average_impure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
