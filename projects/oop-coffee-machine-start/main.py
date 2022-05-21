from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    items = menu.get_items()

    while True:
        selection = input(f"What would you like? ({items}): ")
        if selection == "report":
            coffee_maker.report()
            money_machine.report()
        elif selection == "off":
            break
        else:
            item = menu.find_drink(selection)
            if not item:
                continue
            if not coffee_maker.is_resource_sufficient(item):
                continue
            if not money_machine.make_payment(item.cost):
                continue
            coffee_maker.make_coffee(item)



main()