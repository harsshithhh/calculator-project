print("Enter a number")
x = int(input())
print("Enter another number")
y = int(input())
z = input("Enter an operation (+, -, /, *)")

if z == "*":
    print(x*y)
elif z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "/":
    if y != 0:
        print(x/y)
    else:
        print("You can't divide by 0, you moron.")
else:
    print("Invalid operation")

