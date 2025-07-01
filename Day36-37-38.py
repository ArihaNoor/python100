#Exception Handling

# a = input("Enter Input: ")

# try: 
#     if int(a)<0:
#         print("Negative Number")
#     elif int(a)>0:
#         print("Positive Number")
# except Exception as e:
#     print("Error Occured: " , e)


# we can also print IndexError as well as ValueError and many other types of errors 

# try:
#     a = int(input("Enter Input: "))
#     num = [1,4,5]
#     print(num[a])
# except ValueError:
#     print("Entered Value is not Number")
# except IndexError:
#     print("Index doesn't Exists")
    

    
#Finally Keyword-- we can use it with try and except for cleanup 

# code in the finally block always execute


# try:
#     a = int(input("Enter Input: "))
#     num = [1,4,5]
#     print(num[a])
# except ValueError:
#     print("Entered Value is not Number")
# except IndexError:
#     print("Index doesn't Exists")
# finally:
#     print("Do you want to try again?")
    
# also -- if function returned the value it will still execute 

def fun(data):
   try:
        integers = [1,2,3,4,5,6,7,8,9]
        if integers.index(int(data)):
            return "Integer"
        elif type(data) == str:
            return "String"
   except:
       print("Error Occured")
   finally:
       print("Every One is Dancing on the floor!!!")
    

# x = input("Enter Data :")

# start = fun(x)

# print(f"{start} is Dancing!")


## Custom Errors Raising 


inputData = input("Enter Number between 5 and 9: ")

try:
    if type(inputData)==str and inputData=="quit":
        print("Okay, Fine")
    else: 
        number = int(inputData)
        if number>5 and number<9:
            print("Okay, Good")
        else:
            print("Number out of Range")
except ValueError:
    print("Value Error")