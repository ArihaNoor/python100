#Match Case Statements 

x = int(input("Enter the value of X: "))

match x:
    case 0:
        print("X is 0.")
    case _ if x>10 and x<99:
        print("X is Greater than 10")
    case _ if x>100 and x<1000:
        print("X is Greater than 100.")
    case _:
        print("No Match......")