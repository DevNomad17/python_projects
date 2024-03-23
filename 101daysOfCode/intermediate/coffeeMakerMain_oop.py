from coffeeMenu_oop import Menu
from coffeeMaker_oop import CoffeeMaker
from moneyMachine_oop import MoneyMachine

delonghi = CoffeeMaker()
delonghi_menu = Menu()
delonghi_pay = MoneyMachine()
ordered_item = None

while True:
    order = input(f"What would you like? {delonghi_menu.get_items()}: ")
    if order == "report":
        delonghi.report()
        delonghi_pay.report()
    elif order == "off":
        break
    else:
        ordered_item = delonghi_menu.find_drink(order)
        if ordered_item is not None:
            if delonghi.is_resource_sufficient(ordered_item):
                if delonghi_pay.make_payment(ordered_item.cost):
                    delonghi.make_coffee(ordered_item)

print("Bye bye")