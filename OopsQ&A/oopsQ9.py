'''
12.
Martin wants to create a ticket booking application for a
movie theater. The application should ask the user for his
choice, whether he wants to book the tickets or not. The
application should also ask the user for the total number of
tickets to be booked. While booking the tickets if the total
number of booked tickets exceeds the available tickets, the
application should raise an exception.
Assume the total number of available tickets is 15.
'''

class Ticket:
    def __init__(self,name,ticket,date):
        self.name = name
        self.ticket = ticket
        self.date = date
    def display(self):
        print("-----YOUR DETAILS------")
        print("Your name: ",self.name)
        print("Your number of tickets: ",self.ticket)
        print("Date for watch movie: ",self.date)

print("WELCOME TO SMART-XTECH!")
print("IF YOU WANT TO BOOK TICKET;\ncode = yes - 1 | no - 2")

try:
    inputx = int(input("Enter your code(1/2):"))
    if inputx == 1:
        print("PLEASE FILL DETAILS:")
        name = input("Enter your name:")
        ticket = int(input("Enter your no of tickets:"))
        date = input("Enter a date when you will watch:")
        if ticket <=15:
            obj = Ticket(name,ticket,date)
            obj.display()
        else:
            print("Sorry out of tickets; available ONLY 15.")            
    elif inputx == 2:
        print("THANK YOU.")
except:
    print("Something went wrong! Enter properly.")