#!/bin/python3/

num = int(input("Enter the number ="))

temp=num


while(num>0):
	dig=num%10
	rev=rev*10+dig
	n=n/10

if(num==rev):
	print("This is palindrome number")

else:
	print("Not a palindrome")
