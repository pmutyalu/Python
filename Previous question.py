'''
here we will have two numbers n and m. we have to find divisibles and non-divisibles of n in between the range of n to m. 
We have to print the sum of total divisibles and non-divisibles in given range.

'''
n = int(input('Enter num1: '))
m = int(input('Enter num2: '))
Total_div_iterations = 0
div_num = []
div_sum = 0
Total_non_div_iterations = 0
non_div = []
non_div_sum = 0
for i in range(n,m+1):
    if i%n == 0:
        Total_div_iterations +=  1
        div_sum += i
        div_num.append(i)
    else:
        Total_non_div_iterations += 1
        non_div_sum += i
        non_div.append(i)
print(f'Divisible numbers of {n} to {m} are : ', div_num)
print(f'Total sum of all Divisible numbers from {n} to {m} are : ',div_sum)
print(f'Non-Divisible numbers of {n} to {m} are : ', non_div)
print(f'Total sum of all Non-Divisible numbers from {n} to {m} are : ',non_div_sum)
print(f'Divisibles loop has iterated for {Total_div_iterations} times.')
print(f'Non-Divisibles loop has iterated for {Total_non_div_iterations} times.')