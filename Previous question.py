n = int(input('Enter num1: '))
m = int(input('Enter num2: '))
div_num = []
div_sum = 0
Iteator_Non_div = 0
non_div = []
non_div_sum = 0
for i in range(n,m+1):
    if i%n == 0:
        div_sum += i
        div_num.append(i)
    else:
        non_div_sum += i
        non_div.append(i)
print(f'Divisible numbers of {n} to {m} are : ', div_num)
print(f'Total sum of all Divisible numbers from {n} to {m} are : ',div_sum)
print(f'Non-Divisible numbers of {n} to {m} are : ', non_div)
print(f'Total sum of all Non-Divisible numbers from {n} to {m} are : ',non_div_sum)
