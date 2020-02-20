#Jose Zavala
#2/12/2020
#This program is supposed to help us find numbers that can be divisible by three.

myList=range(1,51)
for number in myList:
    print(number)
    
    if (number%3==0) and (number%5==0):
        print("Divisible by both")

    elif number%3==0:
        print("Divisible by three")
    elif number%5==0:
        print("Divisible by five")
