import datetime
"""
    Mr. Ashok like to create a flight ticket booking application. To book a
    flight, user should enter his / her name, DOB, address and passport
    number followed by Start city, destination city and date of travel. Here are
    the constraints -
        1. Name should be all in upper case and it should be free from special
        characters or numbers. His application only allow names of length
        ranges from 5 to 30 max.
        2. DOB should be in a format of DD-MM-YYYY. Other formats not
        allowed.
        3. Passport number is only of 8 digits and should start with ‘P’
        followed by numbers.
        4. Start city and destination city should NOT be same. Here are the
        constraints -
        1. Start city / End city should be any one of these [ “Paris”,
        “Japan”, “China”]
        5. Date of travel should be in format [DD-MM-YYYY]
        Write functions to validate all those above constraints and if all validations
        successful, return “Flight Ticket Booked”, else return respective error
        message.
        (Example: Invalid Passport number if passport number validation fails etc….)
"""
def name_check():
    name = input("Name: ")
    if(30>len(name)>=5):
        for _ in range(len(name)):
            if(name[_]>='A'and name[_]<='Z'):
                return name
            else:
                print("letters should be in uppercase!")
    else:
        print("length should u be 5<=x<30!")


def dob():
    d_ob = input("DOB [DD-MM-YYYY]: ")
    try:
        dt = datetime.datetime.strptime(d_ob, "%d-%m-%Y")
        dbirth = datetime.datetime.strftime(dt,"%d-%m-%Y")
        return dbirth
    except ValueError:
        print("Incorrect format")

def pass_check():
    pass_no = input("Passport Number: ")
    if(pass_no[0]=='p'):
        if(len(pass_no)==8):
            return pass_no
    else:
        print("Invalid Passport Number!")
def city_check(s_city,d_city,city):

    if(s_city != d_city):
        for i in range(len(city)):
            if(city[i]==s_city):
                return s_city,d_city
    else:
        print("Start & Destination City is Same please check.")

def booking_date_check():
    bd = input("Enter Booking Date [DD-MM-YYYY]: ")
    try:
        b_cing = datetime.datetime.strptime(bd,"%d-%m-%Y")
        b_c = datetime.datetime.strftime(b_cing,"%d-%m-%Y")
        return b_c
    except ValueError:
        print("Incorrect format")

def all_check(n,d,pc,sc,bdc):
    if(n!=None and d!=None and bdc!=None and pc!=None):
        return "Flight Ticket Booked"
    else:
        return "Verify your Details...Again!"

city = ["Paris","Japan","China"]
n = name_check()
d = dob()
pc = pass_check()
s_city = input("enter Start City: ")
d_city = input("enter Destination City: ")
sc = city_check(s_city,d_city,city)
Add = input("enter address: ")
bdc = booking_date_check()
print(n,d,pc,Add,bdc,sc)
print(all_check(n,d,pc,sc,bdc))
