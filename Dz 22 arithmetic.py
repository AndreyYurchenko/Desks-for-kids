def arithmetic (x, y, z):
    if z == "+" :
		return (x + y)
	elif z == "-":
		return (x - y)
	elif z == "*":
		return (x * y)
	elif z == "/":
		return (x / y)
	else :
		return ("Invalid operation")



print (arithmetic(5, 2, '+'))
print (arithmetic(5, 2, '*'))
print (arithmetic(5, 2, '-'))
print (arithmetic(5, 2, '/'))
print (arithmetic(5, 2, 0))


