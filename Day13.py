#String Methods 

name = "Ariha Noor"
# Strings are immutable when we apply some 
# function it will generate new string 

# methods 
print(name.upper())
print(name.lower())

# it will strip trailing characters 
print(name.rstrip("r"))

print(name.replace("o", "0"))

print(name.split(" "))


# It will capitalize the fist letter and all other letters to lowercase
print(name.capitalize())

# It will add 50-length spaces at the leading of string
print(name.center(50))


print(name.count("o"))

print(name.endswith("r"))


# first occurence of the string 
print(name.find("o"))

# It will raise error if not found 
print(name.index("r"))


# it will return true if it is alphanumeric
print(name.isalnum())

# to check all the alphabets or not
print(name.isalpha())