from menu import MENU, resources


def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def is_enough_resources(ingredients):
    enough_resources = True
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            enough_resources = False
    return enough_resources


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return round(
        0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)


def transaction_successful(paid_amount, drink_cost):
    if paid_amount > drink_cost:
        change_amount = round(paid_amount - drink_cost, 2)
        resources['money'] += round(drink_cost, 2)
        print(f"Here is ${change_amount} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def prepare_drink(selection):
    """ prepare drink documentation """
    if not is_enough_resources(selection['ingredients']):
        return False

    paid_amount = process_coins()
    if not transaction_successful(paid_amount, selection['cost']):
        return False

    for i in selection['ingredients']:
        resources[i] -= selection['ingredients'][i]
    return True


def main():
    coffee_machine_on = True
    while coffee_machine_on:
        selection = prompt_user()
        if selection == "report":
            print_report()
        elif selection == "off":
            coffee_machine_on = False
        else:
            if prepare_drink(MENU[selection]):
                print(f"Here is your {selection} Enjoy!")


main()
