income = float(input("Enter the annual income: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax_amount = income - 85528
    tax = 14839.02 + 0.32 * tax_amount

tax = round(tax, 0)
print("The tax is", tax, "thalers.")