fib1 = 1
fib2 = 1

n =int(input("enter number Fibonachi: "))

i=0
while i < n - 2:
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
    i += 1

print(fib2)


