'''
Finding biggest and smallest in a given list of elements.
'''

arr = [12,3,36,2,9,29]
big = arr[0]
small = arr[0]

for i in arr:
    if big < i:
        big  = i
    elif small > i:
        small = i
        
print('Biggest element in the list is: ',big)

print('Smallest element in the list is: ',small)