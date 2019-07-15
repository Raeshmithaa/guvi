a=int(input("Enter year to be checked:"))
if(a%4==0 and a%100!=0 or a%400==0):
    print("The year is a leap year!)
else:
    print("The year isn't a leap year!)
