# Set comprehenison means..cretaing a list from pre-existing list

'''
printing a particular elements from a pre-existing list.
here we have to print the elements the elements consisting 'g'
'''


# the below block of code will retrive every element which has g in it.

companys = {'google','goldman sachas','jaguar','titan'} #creating a set
g_company = set() #creating an empty set to store elements of 'g' consisting company
for company in companys: #we are storing each element in the list of companys as a company during each iteration 
    if 'g' in company:    #check the element contains 'g' in it or not 
        g_company.add(company)   #if the element contains 'g' then add it to the list
print(g_company)    #print the company names starting with 'g'


# the below block of code will create an set of elements starting with 'g'

companys = {'google','goldman sachas','jaguar','titan'} #creating a set
g_company = set() #creating an empty set to store elements of 'g' starting company
for company in companys: #we are storing each element in the list of companys as a company during each iteration 
    if company[0] == 'g':    #check the element contains 'g' in it or not 
        g_company.add(company)   #if the element contains 'g' then add it to the list
print(g_company)    #print the company names starting with 'g' 


#finding squares of a number using list comprehension

num = [i**2 for i in range(1,6)]
print(num)