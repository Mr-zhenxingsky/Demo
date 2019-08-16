# this program is used to get the Hadamard of two matrices
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j]*b[i][j] for j in range(n)])
print("After matrix mutiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5),end=' ')
    print()
print("-" * 7 *n)
# [int(x) for x in input().split()] first get string[] through input[],then use split()# get a series of numeric strings ,last use int() get the integer
