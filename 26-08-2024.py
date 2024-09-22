'''
String handling functionS
-'''

name = "aryan"

'''
Accessing Characters
'''

print(name[0])  
print(name[1])  


'''
String Slicing:
String Slicing is meant by accessing an given range of characters in a string.
We can skip writing the first index number if we want to access the string from first index. Simply we can proceed to write :
'''
print(name[0:2])

print(name[:2])

A = "My name is " 
print(A+name)

str_Repetation = name * 2
print(str_Repetation)

'''
Nested list has another list in the original list.
In the below esxample 0,1,2,4 indices contains normal elements. But 3rd index contains another list of n elements. all the elements in the sub list will come under index of 3.
Using slicing we can acces the sublist or we can access them useing their index positions.'''
