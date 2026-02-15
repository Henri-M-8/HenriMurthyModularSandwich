class Cashier:
    def __init__(self):
        self.profit = 0

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0
        total += float(input("how many quarters?: ")) * 0.25
        total += float(input("how many dimes?: ")) * 0.10
        total += float(input("how many nickels?: ")) * 0.05
        total += float(input("how many pennies?: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        coins = self.process_coins()
        if coins >= cost:
            change = coins - cost
            print(f"Payment accepted. Your change is ${change:.2f}.")
            self.profit += cost
            return True
        else:
            print("Insufficient funds. Transaction failed.")
            return False


