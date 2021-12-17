name = input ('* lotfan name ra vared konid  :')

d1 = int (input('* lotfa nomre dars 1 ra vared konid :'))

d2 = int (input('* lotfa nomre dars 2 ra vared konid :'))

d3 = int (input('* lotfa nomre dars 3 ra vared konid :'))

avg = (d1+d2+d3)/3
print ('moaddele shoma =  ' , avg)
if avg > 15 :
    print (name , 'aziz , shoma daneshjoo -e-  momtaz hastid ')
elif avg > 10 and avg < 15 :
    print (name , 'aziz , shoma daneshjoo -e- aadi hastid ')
elif avg == 10 or avg > 10 :
    print (name , 'aziz , shoma daneshjoo -e- mashrout hastid ')