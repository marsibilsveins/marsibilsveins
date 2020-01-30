num1 = int(input("Input number: "))
op = str(input("Input operation: "))
num2 = int(input("Input number: "))

if op == "+":
    print(num1,op,num2, "=", int(num1+num2))
elif op == "-":
    print(num1, op, num2, "=", int(num1-num2))
elif op == "/":
    print(num1,op,num2, "=", int(num1/num2))
elif op == "*":
    print(num1,op,num2, "=", int(num1*num2))
else:
    print(num1,op,num2, "=" "None")
#print(num1,op,num2)




