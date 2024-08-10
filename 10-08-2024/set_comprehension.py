# Set comprehenison means..cretaing a list from pre-existing list
'''
printing a particular elements from a pre-existing list.
here we have to print the elements the elements consisting 'g'
'''
# the below block of code will retrive every element which has g in it.

companys = {'google','goldman sachas','jaguar','titan'} 
g_company = []
for company in companys:
    if 'g' in company:
        g_company.append(company)
print(g_company)