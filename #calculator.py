#calculator

Num1 = float(input("please input a number: "))
Num2 = float(input("please input a number: "))
Op = (input("please input an operation: "))

if Op == "/":
    print(Num1/Num2)
elif Op == "*":
    print(Num1*Num2)
elif Op == "+":
    print(Num1+Num2)
elif Op == "-":
    print(Num1-Num2)