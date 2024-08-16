'''

Given a sorted array of N integers and an integer X, find the integer in array that is closest to X. If there are multiple such integers, print the smaller number.

Closeness of two integers u and v is simply absolute value of u - v.

Input
First line contains two integers N and X.

Second line contains N integers describing the array.

Output
Print smallest integer in array that is closest to X.

'''


x = int(input('Enter an integer: '))
arr = [3, 2, 8, 5, 6]
arr.sort()  # Sorting the list
closest = arr[0]
smallest = abs(closest - x)

for i in arr:
    current_diff = abs(i - x)    #useing abs to make incase of negative value occurance can be changed to positive
    if current_diff < smallest:
        closest = i
        smallest = current_diff

print("The closest number to", x, "is", closest)
