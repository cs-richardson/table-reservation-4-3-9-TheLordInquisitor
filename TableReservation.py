# This program prompt the user for an input string and check if it matches 
# another string to output a response based on that condition

# Program written by Son Nguyen

name = input("Please input a name: ")
reservation_name = "Son"
if(name == reservation_name):
    print ("Name:", name)
    print ("Right this way")
else:
    print ("Name:", name)
    print ("Sorry, we don't have a reservation under that name")
