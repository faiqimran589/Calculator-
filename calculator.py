a=int(input('Enter your first number:'))
b=int(input('Enter your second number:'))
c=input('Enter an arithmetic operation(+,-,*,/,%,//):')
if c == '+' :
   print('Addition of a and b is:',a+b)
elif c == '-':
   print('Subtraction of a and b is:',a-b)
elif c == '*':
   print('Multiplication of a and b is:',a*b)
elif c == '/':
   if b == 0 :
      print('Error:Division by zero generates math error')
   else:
    print('Division of a and b is:',a/b)
elif c == '%' :
   print('Modulus of a and b is :',a%b)
elif c == '//':
   if b == 0:
      print('Error: division by zero generates math error')
   else:
    print('Floor division of a and b is :', a//b)
else:
   print('unrecognized')
