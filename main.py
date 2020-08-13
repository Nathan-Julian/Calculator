
import pygame

pygame.init()

print("This is a calculator program.")
number1 = input("Enter the first number: ")
number1 = int(number1)
operation = input("Enter the operator(* is multiply, / is divide, + is add, and - is subtract): ")
number2 = input("Enter the second number: ")
number2 = int(number2)

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

if operation == "+":
	total = add(number1,number2)
	print(total)