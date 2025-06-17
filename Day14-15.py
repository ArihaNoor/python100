#conditional statements 

import time 

currentTime = int(time.strftime("%H"))

name = input("Enter Your Name: ")


if currentTime<12:
    print("Good Morning, ", name)
elif currentTime>12 and currentTime<=16:
    print("Good AfterNoon, ", name)
elif currentTime>16 and currentTime<=19:
    print("Good Evening, ", name)
else: 
    print("Good Night, ", name)