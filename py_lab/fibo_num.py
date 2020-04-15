#!/usr/bin/python3
n = int(input("fibonacci number?"))
x = 1
y = 1
temp = 0
print(x)
print(y)
for i in range(2,n):
	temp = y 
	y = x + y 
	x = temp
	print(y)
print("F{} = {}".format(n,y) )

