year =int(input("Enter the year"))
if year%4==0:
    if year %100!=0:
        print ("Leap Year")
    else:
        if year % 400==0:
           print("Not Leap year")
         
