import math
    
a = int(input('num1 : '))
b = int(input('num2 : '))
op =input ('op : ')

if op == '+' :
    print(a+b)
elif op == '-' :
    print(a-b)
elif op == '*' :
    print(a*b)
elif op == '/' : 
    if b == 0 :
        print(' num2 can not be 0 ')
    else :
        print (a/b)
elif op == 'radical' :
    print ('radical ', a , '= ', math.sqrt(a))
elif op == 'sin' :
    print ('sin ', a , '= ', math.sin(a))
elif op == 'cos' :
    print ('cos ', a , '= ', math.cos(a))
elif op == 'tan' :
    print ('tan ', a , '= ', math.tan(a))
elif op == "factorial" :
    print ('factorial ', a , '= ', math.factorial(a))