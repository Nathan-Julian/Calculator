
import pygame

pygame.init()

for i in range(5):
	print("")
print("This is a calculator program.")
num1 = input("Enter the first number: ")
num1 = int(num1)
operation = input("Enter the operator(* is multiply, / is divide, + is add, - is subtract, ^ is exponent): ")
if not(operation == toBin or operation == fromBin):
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
	

def fromBin(a):
	


if operation == "+":
	total = add(num1,num2)
	print("")
	print(f"				>>>> Answer: {total} <<<<")
elif operation == "-":
	total = subtract(num1,num2)
	print("")
	print(f"				>>>>	Answer: {total} <<<<")
elif operation == "/":
	total = divide(num1,num2)
	print("")
	print(f"				>>>>	Answer: {total} <<<<")
elif operation == "*":
	total = multiply(num1,num2)
	print("")
	print(f"				>>>>	Answer: {total} <<<<")
elif operation == "^":
	total = exp(num1,num2)
	print("")
	print(f"				>>>>	Answer: {total} <<<<")
elif operation == "toBin":
	total = toBin(num1)
	print("")
	print(f"				>>>>	Answer: {total} <<<<")
elif operation == "-":
	total = fromBin(num1)
	print("")
	print(f"				>>>>	Answer: {total} <<<<")