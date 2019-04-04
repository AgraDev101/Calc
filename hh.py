

def add():
	num1 = input("1st number  ")
	num2 = input("2nd nuber  + ")
	res = float(num1) + float(num2)
	print("Ans    --------\n           " +str(res))

def sub():
	num1 = input("1st number  ")
	num2 = input("2nd nuber  - ")
	res = float(num1) - float(num2)
	print("Ans    --------\n           " +str(res))

def mul():
	num1 = input("1st number  ")
	num2 = input("2nd nuber  x ")
	res = float(num1) * float(num2)
	print("Ans    --------\n           " +str(res))

def div():
	num1 = input("1st number  ")
	num2 = input("2nd nuber   ")
	res = float(num1) / float(num2)
	print("Ans    --------\n           " +str(res))


def calc():
    op = input("enter operator ")

    if op == "+":
    	add()
    elif op == "-":
    	sub()
    elif op == "*":
    	mul()
    elif op == "/":
    	div()
    else:
    	print("invalid")

cont = "Y"

while cont != "N" or not(cont):
	calc()
	cont = input("cont Y/N?")


print("Exiting")






