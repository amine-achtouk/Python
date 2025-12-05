
foods = []
prices = []
total = 0

while True:
    food = input('enter a food to by (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'entrer price of {food} : DH '))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"total prices is {total} DH")

