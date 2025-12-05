sum_p  = 0
sum_n = 0
total = 0


while True:
    n = int(input('Enter a number (0 for Stop): '))
    if n == 0:
        break
    elif n > 0:
        sum_p += n
    elif n < 0:
        sum_n += n    
print('-----------------------------------')
print(f'somme of number Positif is {sum_p}')
print('-----------------------------------')
print(f'somme of number Negatif is {sum_n}')
print('-----------------------------------')
total = sum_p + sum_n
print(f'somme total is {total}')
