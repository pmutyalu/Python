a = 5
b = 0
'''
All the above statements are fine and there is no chance of generating an error(These are just declaration var's). 
But if we perform division operation on variables then we can't divide with zero, so there is an chance of error here we can write the statements which have chance of error in try statements.
'''
try:
    print(a/b)
    
    
    """
    This is just printing we got an error we don't know exact name of error.
    """
except Exception:
    print('The second variable is zero, can\'t divide with zero')