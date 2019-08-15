#! /usr/bin/python3
N = 10
sum = 0
i = 0
while i < 10:
    sum = sum + float(input("please input num: "))
    i+=1
average = sum / N
print("N = {},sum = {}".format(N,sum))
print("Average = {:.2f}".format(average))
