def convertToBin(n):
	if n > 1:
		convertToBin(n//2)
	print(n % 2, end = '')

# decimal number
dec = int(input("Decimal number: "))

convertToBin(dec)