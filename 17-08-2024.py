'''
A dictionary is an unordered collection of key-value pairs. Are used to store data in the form of key-value pairs, where each key is unique.
'''

'''
Creating Dictionaries
To create a dictionary, you use curly braces {} and specify key-value pairs separated by colons :. Keys and values can be of any data type.
'''

sample_dict = {'Dtype_String': 'AB','Dtype_boolean': True, 'Dtype_Integer': 850}
print(sample_dict)



'''
Accessing Values
You can access the values in a dictionary using square brackets [] with the key.
'''

first_index = sample_dict['Dtype_String']
print(first_index)


'''
Adding Values
To add new key-value pairs or update existing ones in a dictionary, you can use square brackets [] and the assignment operator.
'''

sample_dict['Addeding_val'] = "I'm added"
print(sample_dict)

print(sample_dict.values())    #Gives only values of the dictionary.

print(sample_dict.keys())    #Gives only keys of the dictionary.

print(sample_dict.items())    #Print all items of the dictionary.

for keys in sample_dict:
    print(keys)    #Print all keys of the dictionary
    
print('\n')

for values in sample_dict:
    print(values)    #Print all values of the dictionary
    
for key,values in sample_dict.items():
    print(key,values) #Print all values of the dictionary