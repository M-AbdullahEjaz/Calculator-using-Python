print("Calculator using Python")
print("What operation do you want to perform?\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Exponential")
choice=input("Enter your choice (1,2,3,4,5)")
if choice=='1' :
   print("we are adding two numbers:")
   num1=float(input("enter first number:"))
   num2=float(input("enter second number:"))
   ans=num1+num2
   print("result : ",ans)
elif choice == '2':
   print("we are subtracting")
   num1=float(input("enter first number:"))
   num2=float(input("enter second number:"))
   ans=num1-num2
   print("result : ",ans)   
elif choice == '3':
   print("we are Multiplying")
   num1=float(input("enter first number:"))
   num2=float(input("enter second number:"))
   ans=num1*num2
   print("result : ",ans)  
elif choice == '4':
   print("we are Dividing")
   num1=float(input("enter first number:"))
   num2=float(input("enter second number:"))
   ans=num1/num2
   print("result : ",ans)   
elif choice == '5':
   print("we are taking Exponent")
   num1=float(input("enter base number:"))
   num2=float(input("enter exponent power:"))        
   ans=num1**num2
   print("result : ",ans)      