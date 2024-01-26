def calculate_income_tax(income):
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = 1000 * 0.1
    else:
        tax = 1000 * 0.1 + 10000 * 0.1 + (income - 20000) * 0.2
    return tax

income = int(input("Insert your income: "))
result = calculate_income_tax(income)
print("Your tax is: ", result)