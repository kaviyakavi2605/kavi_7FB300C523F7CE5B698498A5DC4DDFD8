num=int(input("please enter the number your wish:"))
if(num%4==0):
  if(num%100==0):
    if(num%400==0):
      print("%d is a leap year"%num)
    else:
      print("%d is not "%num)
  else:
    print("%d is a leap year"%num)
else:
  print("%d is not"%num)