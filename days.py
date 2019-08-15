days = int(input("Enter days: "))
#divmod this function used to get two value(a,b) a=days//30 b=days%30
print("Months = {} Days = {}".format(*divmod(days,30)))
