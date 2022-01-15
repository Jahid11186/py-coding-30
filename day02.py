meal_cost = float(input())
tip_p = int(input())
tax_p = int(input())

tip = (tip_p / 100) * meal_cost
tax = (tax_p / 100) * meal_cost

total = meal_cost + tip + tax

print(round(total))

