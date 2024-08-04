a = int(input('Enter A value: '))
b = int(input('Enter B value: '))

print("\nThe value of a before swaping is ",a)
print("The value of b before swaping is ",b)

a = a + b
b = a - b
a = a - b

print("\nThe value of a after swaping is ",a)
print("The value of b after swaping is ",b)