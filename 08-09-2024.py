a = 5
b = 0
sample_lis = [1,2,3,4,5]
'''
All the above statements are fine and there is no chance of generating an error(These are just declaration var's). 
But if we perform division operation on variables then we can't divide with zero, so there is an chance of error here we can write the statements which have chance of error in try statements.
'''

try:
    print('helllo this is before exception raised')
    print(a/b)
    """
    we can perform any oprations in try block as normally but whenever a lines hits the error below statements will not be executed.
    To overcome such problem we have to use different try and except blocks
    """
    
    """
    This is just printing we got an error we don't know exact name of error.
    if we print custom error message along with the error name we should write the following. 
    """

except ZeroDivisionError:
    print('The second variable is zero, can\'t divide with zero\n')
    
    """
    Finally will get executed no matter what the above code
    """

try:
    print(sample_lis[10])

except IndexError:
    print('Give proper range.')

except Exception as e:
    print(e)
    
finally:
    print('helllo this is after exception raised')
