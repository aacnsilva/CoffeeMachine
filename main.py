MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def has_enough_resources(order_ingredients):
    """Returns if the machine has enough resources for the given menu order ingredients"""
    for ingredient in order_ingredients:
        coffe_machine_resource = resources[ingredient]
        if coffe_machine_resource is None:
            print(ingredient + " is not available")
        if order_ingredients[ingredient] > coffe_machine_resource:
            print(f"Machine doesn't have enough {ingredient}")
            return False
    return True


def process_coins():
    """Returns the total amount of coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, order_price):
    """Returns if the payment is accepted"""
    if money_received >= order_price:
        change = round(money_received - order_price, 2)
        print(f"Here is your change: {change}€")
        global money
        money += order_price
        return True
    else:
        print("Insufficient funds")
        return False


def make_order(menu_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {menu_name}")


is_on = True
while is_on:
    user_selection = input("What would you like? (espresso/latte/cappuccino):\n")
    match user_selection:
        case "off":
            is_on = False
        case "report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}")
            print(f"Money: {money}€")
        case _:
            if user_selection not in MENU:
                print(f"{user_selection} is not available in the menu")
            else:
                menu_order = MENU[user_selection]
                if has_enough_resources(menu_order["ingredients"]):
                    payment = process_coins()
                    if is_transaction_successful(payment, menu_order["cost"]):
                        make_order(user_selection, menu_order["ingredients"])
