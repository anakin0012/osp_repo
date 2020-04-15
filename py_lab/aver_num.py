#!/usr/bin/python3
n =int(input("input number of n:"))
sum = 0


for i in range(0,n):
	temp =int(input("input number:"))
	sum += temp
sum = sum / n
print("average:",sum)
