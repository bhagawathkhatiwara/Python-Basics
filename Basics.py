num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)
    
# The code above is a simple program that compares two numbers.

num3 = int(input("enter number to print multiplication table: "))

i=1
while i<=num3:
    product=num3*i
    print(f"{num3} x {i} = {product}")
    i += 1

 # The code above is a simple program that prints the multiplication table of a number.