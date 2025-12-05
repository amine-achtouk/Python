

# lists = [1, 2, 4, 5, 6, 7, 8, 12, 9, 11]
# max_n = lists[0]
# min_n = lists[0]
# som = 0

# for list in lists[0:]:
#     if list > max_n:
#         max_n = list
#     elif list < min_n:
#         min_n = list    
#     som += list 
    
# print(max_n)
# print(min_n)
# print(som)

numbers = [12, -7, 5, -3, 9, -20, 0, 4, -1]

count_pos = 0
count_neg = 0
sum_even = 0
sum_odd = 0
max_n = numbers[0]
min_n = numbers[0]

# التكرار على كل العناصر
for num in numbers:
    # عدد الموجب والسالب
    if num > 0:
        count_pos += 1
    elif num < 0:
        count_neg += 1

    # مجموع الزوجي والفردي
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

    # أكبر وأصغر عدد
    if num > max_n:
        max_n = num
    if num < min_n:
        min_n = num

print(count_pos)
print('------------')
print(count_neg)
print('------------')
print(sum_even)
print('------------')
print(sum_odd)
print('------------')
print(max_n)
print('------------')
print(min_n)



