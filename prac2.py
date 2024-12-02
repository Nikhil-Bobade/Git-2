Age = int(input("Enter the Value: \n"))
Day = input("Enter the day: \n")
Price = 12 if Age >=18 else 8
if Day =="Wendnesday":
    #price = price-2
    Price-= 2
print("Ticket price for you is $",Price)
