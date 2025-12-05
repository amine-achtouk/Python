
import random

num_high = 50
num_low = 1

answer = random.randint(num_low, num_high)

is_run = True

while True:
    geuss = input('Geuss a Number Between 50 and 1 : ')
    if geuss.isdigit():
        geuss = int(geuss)

        if geuss > num_high or geuss < num_low:
            print('number is Out Range')
        elif geuss > answer:
             print('to Low')
        elif geuss < answer:
             print('to High')  
        else:
             print('CORRECT') 
             is_run = False 
             break 
    else:
        print('invalid pass') 
                       



# number = random.randint(1,20)

# while True:
#     n = int(input('Geuss a number between 1 and 20: '))
#     if n == number:
#         print('congrate')
#         break



# while True:
#     n = input('enter a number : ')
#     if n.isdigit():
#        pass
#     else:
#         print("🛑 Invalid input. Please enter a whole, positive number.")
#         break

