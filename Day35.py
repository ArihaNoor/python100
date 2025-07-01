# for with else 

# when you are using some for loop or while loop 
# when all conditions executed and you want to run some code then use else


for i in range(0):
    print(i)
else:
    print("I is 0")
    
# else will only print if loop has completed or finished successfully
# all the condtions are run 

# if loop ends than it will not execute the else case 

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Hello, in the else block")
    
  
i=0  
while i<7:
    print(i)
    i=i+1
else:
    print("Hello, in the else block")