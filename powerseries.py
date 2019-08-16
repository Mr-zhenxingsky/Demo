# this is a program for deal with e^x = 1 + x + x^2/2! + x^3/3! + ... + x^n/n! (0<x<n)
x = float(input("Enter x: "))
n = 1
term = 1
sum=1.0
while n < 100:
    term *= x/n
    sum += term
    n += 1
    if term < 0.0001:
        break
print(" No of Times = {} and Sum = {}".format(n,sum))
