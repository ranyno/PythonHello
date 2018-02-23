def factor(num):
    product = 1
    for i in range(1, num+1):
        product = product * i
    return product

print("Hello world")
value = input("Please Enter a positive integer -> ")
print("Factorial of " + value + " is " + str(factor(int(value))))

