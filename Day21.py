# Function Arguments
# Default Arguments
# Keyword Arguments
# Variable length Argument
# Required Arguments


# Default Arguments: These are actually work if we haven't provided any value
# This way the function assumes a default value even if a value is not provided in the function call for that argument.
def Average(a=9, b=1):
    print("The Average is : ", (a + b) / 2)


# Average(8)

# Keyword Arguments
# we add arguments with named keys, in which order doesn't matter

# Average(b=9, a=21)

# Average(b=9)

# Variable length argument
# using * at the start of the argument we can make it variable length, than it will automatically considers it as a tuple
# if we use ** than it will consider it as a dictionary


# Required Arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# when number of arguments passed does not match to the actual function definition. It will given an error.


def name(fname, mname, lname):
    print("Hello, ", fname,mname,lname)
    

name("Ariha", "Noor", "Ariha") #Here if you miss any one argument it will give an error 


def fullName(lname,fname="Ariha",mname="Noor"):
    print("Hello, ", fname,mname,lname)
    

fullName("Noor") #Here default value will be used 


def players(*player):
    # for i in player:
    #     print(i)
    print(player)

#It will consider it as tuple
# players("Ariha", "Jim", "Jane", "Jenifer", "Juliet", "Shradha")



def team(**player):
    for i,j in player.items():
        print(j)
    # print(player)

#It will consider it as tuple
team(player1="Ariha", player2="Noor", player3="Jenifer")


