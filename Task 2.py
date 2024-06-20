num1=int(input("Enter first number:"))
num2=int(input("Enter second number"))
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
operation=int(input("Enter the type of operation:"))
if operation==1:
    print("The Addition of two numbers is:",(num1+num2))
elif operation==2:
    print("The Subtraction of two numbers is:",(num1-num2))    
elif operation==3:
    print("The Multiplication of two numbers is:",(num1*num2))
elif operation==4:
    print("The Division of two numbers is",(num1/num2))
else:
    print("Select a valid operation")