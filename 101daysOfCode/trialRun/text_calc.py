import common


def perform_calc(n1, n2, operator):
    if operator == "+":
        res = n1 + n2
    elif operator == "-":
        res = n1 - n2
    elif operator == "*":
        res = n1 * n2
    else:
        res = n1 / n2
    return res


print(common.art_calc)
decision = ""
result = 0.0

while True:
    if decision != 'y':
        a = float(input("What's the first number?: "))
        print("+")
        print("-")
        print("*")
        print("/")
    else:
        a = result
    op = input("Pick an operation: ")
    b = float(input("What's the next number?: "))
    result = perform_calc(a, b, op)
    print(f"{a} {op} {b} = {result}")
    decision = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, type 'q' "
                     f"to quit: ")
    if decision == 'q':
        break
