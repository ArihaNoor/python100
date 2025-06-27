#Lists 

#Operations + Iterations 

list = [3,5,6,7,8,9,10,2]

print(list)

# 0 Based Indexing 

# length will be based on 1

# length of list - (index)
print(list[-2])

# In keyword -- we can apply this same in keyword for string as well

if "6" in list: 
    print("true")
else:
    print("false")
    
print(list[:])
print(list[1:])
    
#Jump Index 
print(list[1:4:2])


list2 = [i*i for i in range(10)]
print(list2)