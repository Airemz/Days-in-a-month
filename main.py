number=int(input("Enter a number from 1-12: "))
 
if (number > 0 and number <13):
 if (number ==1) or (number ==3) or (number ==5) or (number ==7) or (number ==8) or (number ==10) or (number ==12):
   print("Therefore, the month has 31 days")
 
 elif (number==4) or (number==6) or (number==9) or (number==11):
   print("Therefore, the month has 30 days")
 
 else:
   print("The month has 28 days in a common year and 29 in leap years")
 
else:
 print("That is not a number between 1-12")
