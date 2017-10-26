def fib(n):

  if n == 0:
        return 0
  elif n == 1:
        return 1
  else:
        return fib(n-1) + fib(n-2)

# User input
nterms = int(input("How many terms?: "))

if nterms <= 0:
	print("Please enter a positive number")
else:
	print("Fibonacci sequence: ")
	for i in range(nterms):
		print(fib(i))
