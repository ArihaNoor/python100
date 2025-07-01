# if else short hand 


a = 100
b = 102

print("true") if a > b else print("false")


# Enumerate operator 

# sometimes we need indexing in list  -- enumerate will make the list tuple (index,value)

word = "Ariha"
for i,word in enumerate(word):
    print(i)
    if i==3:
        print("Your letter is: ", word)