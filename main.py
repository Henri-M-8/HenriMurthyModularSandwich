import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        order = input("What size sandwich would you like? (small/medium/large): ").lower()
        if order in recipes:
            sandwich_ingredients = recipes[order]["ingredients"]
            sandwich_cost = recipes[order]["cost"]
            if sandwich_maker_instance.check_resources(sandwich_ingredients):
                print(f"The cost of the {order} sandwich is ${sandwich_cost:.2f}. Please insert coins.")
                if cashier_instance.transaction_result(sandwich_cost):
                    sandwich_maker_instance.make_sandwich(order, sandwich_ingredients)
        else:
            print("Invalid selection. Please choose small, medium, or large.")

if __name__=="__main__":
    main()
