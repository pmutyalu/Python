a = int(input('Enter a number: '))
b = int(input('Enter b number: '))
c = int(input('Enter c number: '))

d = (b**2) - (4*a*c)

root1 = (-b + (d**0.5))/2*a
root2 = (-b - (d**0.5))/2*a

print(f'Roots are: ({root1}),({root2})')
