my_tuple = 1,2,3    #By default this will be considered as tuple, without using ()
list_conversion = set(my_tuple)
print(list_conversion)

set1 = {1,2,1}    #ignores repeated values
print(set1)

set1.add(4)    #adding new element into set1
print(set1)

set1.remove(4)   #removing element from set1
print(set1)

set1.pop()    #removing element from set1
print(set1)
