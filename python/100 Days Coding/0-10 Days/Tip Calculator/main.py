print("Project 2")
print("=============")
print("Welcome to the tip Calculator.")
totalBill = float(input("What was the total bill?  $"))
percentage = float(input("What percentage tip'd you like to give? 10? 12? 15? "))
howMany = float(input("How many people to split the bill? "))

eachPerson = round((((totalBill / 100) * percentage) / howMany) + (totalBill / howMany), 2) 


print(f"Each person should pay {eachPerson}")
