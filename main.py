b =int(input ("enter a number"))
a =input ("enter * / - + ")
c = int(input("enter a second number"))

if a == "*":
  print (b * c)
elif a == "/":
  print (b / c)
elif a == "-":
  print (b - c)
elif a == "+":
  print (b + c)
else:
  print ("wrong input")