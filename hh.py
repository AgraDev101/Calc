def add():
	num1 = input("1st number  ")
	num2 = input("2nd nuber  + ")
	res = float(num1) + float(num2)
	print("Ans    -----------\n           " +str(res))

def sub():
	num1 = input("1st number  ")
	num2 = input("2nd nuber  - ")
	res = float(num1) - float(num2)
	print("Ans    -----------\n           " +str(res))

def mul():
	num1 = input("1st number  ")
	num2 = input("2nd nuber  x ")
	res = float(num1) * float(num2)
	print("Ans    -----------\n           " +str(res))

def div():
	num1 = input("1st number  ")
	num2 = input("2nd nuber   ")
	res = float(num1) / float(num2)
	print("Ans    -----------\n           " +str(res))


def calc():
    op = input("Enter operator ")

    if op == "+":
    	add()
    elif op == "-":
    	sub()
    elif op == "*":
    	mul()
    elif op == "/":
    	div()
    else:
    	print("Invalid operator")
	
	
cont = "y"

while cont != "n" or not(cont):
    calc()
    cont1 = str(input("Cont. Y/N?"))
    cont = cont1.lower()

print("Exiting..")






