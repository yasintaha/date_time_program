from datetime import date
from datetime import time
import datetime

# class of datedata
class Datedata():
    def display(self):
        today=date.today()
        print("todyas date is :",today)

    def display2(self):
        today=datetime.datetime.now().time()
        print("time is :",today.strftime("%H:%M"))

    def display3(self):
        today=datetime.datetime.now()
        print("Current date and time:",today)

    def display4(self):
        today=datetime.datetime.now()
        print("Formatted date and time",today.strftime("%a,%d,%B,%y"))
    def display5(self):
        today=datetime.datetime.now()
        print(today.strftime("%x"))

    def display6(self):
        today = datetime.datetime.now()
        print(today.strftime("%X"))

    def display7(self):
        today = datetime.datetime.now()
        print(today.strftime("%c"))
# end of an datedata class

# start of main function
def main():
    print("1.date")
    print("2.time")
    print("3.Current date and time")
    print("4.formatted date and time")
    print("5.local date")
    print("6.local time")
    print("7.local date and time")
    choice=int(input("Enter the date format choice:"))
    if choice == 1:
         s=Datedata()
         s.display()

    elif choice == 2:
        s = Datedata()
        s.display2()

    elif choice == 3:
        s = Datedata()
        s.display3()
    elif choice == 4:
        s = Datedata()
        s.display4()
    elif choice == 5:
        s = Datedata()
        s.display5()
    elif choice == 6:
        s = Datedata()
        s.display6()
    elif choice == 7:
        s = Datedata()
        s.display7()
#end of main function

# calling of main function
if __name__== "__main__":
    main()
