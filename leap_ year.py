year = input("please give me a year's name: ")
year = int(year)
if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(year,"yes")
      else:
        print( year,"No")
    else:
      print(year,"yes")
else:
  print(year,"no")
