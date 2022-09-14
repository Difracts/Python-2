a = int(input("INPUT THE MONTH : "))
n = int(input("INPUT THE DAY : "))
def toseason(a,n):
    month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    if a==2 and n>=30:
        print("That is impossible,enter correct data")
    else:
        if a==12 or a==1 or a==2:
            print("{}, {}. Season is {}. ".format(month[a],n,"winter"))
        elif a==3 or a==5 or a==4:
            print("{}, {}. Season is {}. ".format(month[a],n,"spring"))
        elif a==6 or a==7 or a==8:
            print("{}, {}. Season is {}. ".format(month[a],n,"summer"))
        else:
            print("{}, {}. Season is {}. ".format(month[a],n,"autumn"))
toseason(a,n)