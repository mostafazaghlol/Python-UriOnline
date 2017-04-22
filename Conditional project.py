num1=float(input("Enter number1"))
num2=float(input("Enter number2"))
op=input("Enter the operation")
if(op=="+"):
    print(num1+num2)
elif(op=="-"):
    print(num1-num2)
elif(op=="*"):
    print(num2*num1)
elif(op=="/"):
    print(num1/num2)
else:
    print("invaled operator")