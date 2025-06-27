#Tuple 

tup = (1,4,5,6)

# print(type(tup))

# In tuple you cannot assign value on the basis of index or change values in the tuple like in list 

# tup[0] = 90  (this is not possible it will give an error)


print(tup[-1])  #it is same like len-1 in -ve indexing 


#Merging Tuples 

countries1 = ("Pakistan", "Saudia", "UAE")

countries2 = ("USA", "UK", "Canada")


countries = countries1 + countries2

print(countries)


NumbersTup = (1,2,45,6,4,2,5,2,2,6,5,8,5,6)

print(NumbersTup.count(3))

# print(NumbersTup.index(3)) #if element doesn't exists than it will raise error

print(NumbersTup.index(4,2,9)) #check 4 from index 2-9


#length of tuple

print(len(NumbersTup))


# you can make changes to lists, once you convert the tuple to list and than make changes to it after than convert it to tuple again