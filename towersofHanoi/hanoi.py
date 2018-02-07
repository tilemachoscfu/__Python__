#Towers of Hanoi using recursion
def hanoi(n, start, target, spare):
    if (n == 1):
        print("From", start, "to", target)
    else:
        hanoi(n-1, start, spare, target)
        hanoi(1, start, target, spare)
        hanoi(n-1, spare, target, start)

hanoi(5, 1, 3, 2)