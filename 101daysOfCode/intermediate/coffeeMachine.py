from coffeeMachine_data import menu, resources


def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${bank}")


def hasSufficientResources(beverage):
    if menu[beverage]['ingredients']['water'] <= resources['water']:
        if menu[beverage]['ingredients']['coffee'] <= resources['coffee']:
            if 'milk' not in menu[beverage]['ingredients']:
                return True
            elif menu[beverage]['ingredients']['milk'] <= resources['milk']:
                return True
    return False


def receivePayment(beverage):
    quarters = int(input("How many quarters do you insert? "))
    dimes = int(input("How many dimes do you insert? "))
    nickels = int(input("How many nickels do you insert? "))
    pennies = int(input("How many pennies do you insert? "))
    received = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    change = received - menu[beverage]['cost']
    if change > 0:
        print(f"Alright, here's your change ${change:.2f}")
    elif change == 0:
        print(f"You've inserted exact amount.")
    else:
        print(f"Insufficient amount, voiding the transaction.")
        return -1
    return menu[beverage]['cost']


def makeCoffee(beverage):
    resources['water'] -= menu[beverage]['ingredients']['water']
    resources['coffee'] -= menu[beverage]['ingredients']['coffee']
    if 'milk' in menu[beverage]['ingredients']:
        resources['milk'] -= menu[beverage]['ingredients']['milk']
    print(f"Here is your {beverage} ☕. Enjoy!")


bank = 0

while True:
    bev = input("What would you like? (espresso/latte/cappuccino): ")
    if bev == 'off':
        break
    elif bev == 'report':
        printReport()
    else:
        if hasSufficientResources(bev):
            payment = receivePayment(bev)
            if payment > 0:
                bank += payment
                makeCoffee(bev)
        else:
            print("Coffee machine has insufficient resources, please call maintenance.")

print("\nBye bye")
