# Sets 

# Set is a collection of distinct objects or values 

new_set = {1,3,4,5,6,3}

# print(new_set)

# it doesn't maintain order of the values  

ariha = {}

# print(type(ariha)) #its giving type dictionary 

# because the syntax of writing set and dictionary is same 

# if you want to create an empty set you will write it as 

new = set()

# print(type(new))


# Methods in set for its manipulation

#Union 

a = {1,3,5,6,7,4,8,9}
b = {4,6,8,9}

# it will show both sets values, except duplicated, and will not update the original sets 
# print(a.union(b))

# it will show both sets values, except duplicated, and will update the original sets 

# a.update(b)
# print(a,b)


#Intersection 

# intersection will give intersection of two sets  

# intersection_update will update your sets 


# print(a.intersection(b))

# print(" A: ", a)
# print(" B: ", b)

# print(a.intersection_update(b))

# print(" A: ", a)
# print(" B: ", b)




# difference will provide symmetric difference of 2 sets 

# print(" A: ", a)
# print(" B: ", b)
# print(a.difference(b))
# print(" A: ", a)
# print(" B: ", b)
# print(a.difference_update(b)) #this will remove the elements which are common in both sets 
# print(" A: ", a)
# print(" B: ", b)


# print(a.isdisjoint(b))

# print(a.issuperset(b))

# print(a.issuperset(b))


# print(a)

# a.discard(6)

# print(a)

# #If you try to remvoe some element which is not present in the set, remove will raise error, discard will not

# a.remove(6)

# print(a)


#pop --- some random value will be poped out

#del -- keyword its not a method, will delete the entire set

#clear -- used to delete all the elements of the set, set will remain intact only elements will be removed 