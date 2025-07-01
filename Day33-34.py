# Dictionaries

# we can use dictionaries where we have key value pair data

dic = {"name": "Ariha Noor", "cgpa": "3.82", "degree": "BSSE"}

# print(dic)

# we can access single value in the dictionary using 2 methods 

# print(dic["cgpa"])

# but this dic.get function will not raise an error if value doesn't exists, it will print None

# print(dic.get('cgpa'))


#Access Multiple Values 

# print(dic.keys())

# for key in dic.keys():
#     print(dic[key])
    
# print(dic.items())


# Dictionaries are ordered but sets are unordered


#Methods 


# dic.pop("name")  #will pop added key:value from the dictionary

# dic.popitem() #will pop added last key:value

# dic.clear() #clear items

# del dic #delete dictionary

print(dic)