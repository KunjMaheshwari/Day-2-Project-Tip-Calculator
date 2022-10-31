#Tip Calculator Project (100 Days Of Code: Complete Python Bootcamp)
#Day 2 

print("Welcome to the Tip Calculator")

totalbill = int(input("What was the total bill? "))

numberofpeople = int(input("How many people to split the bill? "))

Tip = int(input("What percentage tip would you like to give? "))

total = (((totalbill)/numberofpeople)*((Tip)/100))
print("Each person should pay: " + str(total))