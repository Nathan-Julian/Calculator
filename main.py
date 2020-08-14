
import pygame

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

pygame.init()
pygame.font.init()

# setting up the screen
print('setting up screen')
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
color = (255, 255, 255)
print('done')
print('setting up fonts')
font1 = pygame.font.SysFont(None, 75)
font2 = pygame.font.SysFont(None, 40)
print('done')

# setting up the clock
clock = pygame.time.Clock()

while True:
	clock.tick(60)
	screen.fill(color)
	txtStage = 1
	calcTxt1 = font1.render('This is a calculator program.', True, (0, 0, 0))
	calcTxt2 = font2.render('Enter mode. console or screen.', True, (0, 0, 0))
	if txtStage == 1:
		screen.blit(calcTxt1, (50, height / 4))
		screen.blit(calcTxt2, (200, 400))
		pygame.display.flip() # move back to bottom of loop once you are displaying text
	for i in range(5):
		print("")
	print("This is a calculator program.")
	num1 = input("Enter the first number: ")
	num1 = int(num1)
	operation = input("Enter the operator(* is multiply, / is divide, + is add, - is subtract, ^ is exponent, toBin, fromBin are binary conversions): ")
	if not(operation == "toBin" or operation == "fromBin"):
		num2 = input("Enter the second number: ")
		num2 = int(num2)

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
	