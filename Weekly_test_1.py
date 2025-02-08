"""CIS 1348 Weekly Test 1"""

# This code collects information about the user and then displays it
# This code is not working. Please fix it.
# Rename the variables using the conventions learned in the course
# and add useful comments

# Asking for user input
print("\n")
f = input("1) First name: ")
l = input("2) Last name:\b")
pp = input("3) Prefix of phone number (e.g., 123): ")
n = input("5) Street Number of your residence : ")
sn = input("5) Street name : ")

A1 = input("6) City: ")
A2 = input("7) State: ")
A3 = input("8) Zip code: ")

# Constructing the required return values
fullname = f + " " + l
phonenumber = pp+"-xxx-xxxx"
fulladdress1 = n + " " + sn
fulladdress2 = A1 + ", " + str(A2) + " " + int(A3)

# Display the results
print("\n")
print("Collected Information:")
print("\n")
print("Full Name: ",fullname)
print("Phone Number: ",phonenumber)
print("Full Address: ")
print(fulladdress1)
print(fulladdress1)

