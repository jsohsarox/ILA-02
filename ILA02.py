# ILA-02
#ILA 02 for CS2
#This is a simple calculator made by Josh Roxas
#8 - Adelfa
#April 1, 2026

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)

