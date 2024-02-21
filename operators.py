a=int(input("Enter the first number"))
for i in range(3):
    operator = input("Enter the operator")
    b=int(input("Enter the next number: "))
    if operator == "+":
        cal = a+b
    elif operator == "-":
        cal = a-b
    elif operator == "*":
        cal = a*b
    elif operator == "/":
        cal = a/b
    else:
        print("Enter a valid operator")
    a = cal
print(cal)    
