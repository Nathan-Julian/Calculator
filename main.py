
import pygame

pygame.init()

for i in range(5):
	print("")
print("This is a calculator program.")
num1 = input("Enter the first number: ")
num1 = int(num1)
operation = input("Enter the operator(* is multiply, / is divide, + is add, - is subtract, ^ is exponent, toBin, fromBin are binary conversions): ")
if not(operation == "toBin" or operation == "fromBin"):
	num2 = input("Enter the second number: ")
	num2 = int(num2)

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def divide(a, b):
	return a / b

def multiply(a, b):
	return a * b

def exp(a, b):
	return a ** b

def toBin(a):
	bian = bin(a)
	bianStr = str(bian)
	binValues = list(bianStr)
	binValues.pop(0)
	binValues.pop(0)
	ansStr = "".join(binValues)
	#for i in range(len(binValues)):
	#	print(binValues[i], end="")
	return ansStr

def fromBin(a):
	decNo = 0

	aa = str(a)
	binNo = list(aa)

	for i in range(len(binNo)):
		if binNo[i] == "1":
			decNo = decNo + 1 * 2 ** (len(binNo) - (i+1))
	return decNo


if operation == "+":
	total = add(num1,num2)
	print("")
	print(f"				>>>> Answer: {total} <<<<")
elif operation == "-":
	total = subtract(num1,num2)
	print("")
	print(f"				>>>> Answer: {total} <<<<")
elif operation == "/":
	total = divide(num1,num2)
	print("")
	print(f"				>>>> Answer: {total} <<<<")
elif operation == "*":
	total = multiply(num1,num2)
	print("")
	print(f"				>>>> Answer: {total} <<<<")
elif operation == "^":
	total = exp(num1,num2)
	print("")
	print(f"				>>>> Answer: {total} <<<<")
elif operation == "toBin":
	total = toBin(num1)
	print("")
	print(f"				>>>> Answer: {total} <<<<")
elif operation == "fromBin":
	total = fromBin(num1)
	print("")
	print(f"				>>>> Answer: {total} <<<<")