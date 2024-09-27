'''
Write a program to generate the Fibonacci series and find the sum of elements up to N terms.
'''


def fib_cal(n):
    total = 0
    a,b = 0,1
    for _ in range(n):
        print(a,end=' ')
        total += a
        a,b = b,a+b
    print('\nThe toatl sum\'s of fib is: ',total)
n = int(input('Enter a num to find fib : '))
fib_cal(n)


'''
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
'''