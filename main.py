num1 =int(input ("enter a number"))
operator =input ("enter * / - + ")
num2 = int(input("enter a second number"))

if operator == "*":
  print (num1 * num2)
elif operator == "/":
  print (num1 / num2)
elif operator == "-":
  print (num1 - num2)
elif operator == "+":
  print (num1 + num2)
else:
  print ("wrong input")