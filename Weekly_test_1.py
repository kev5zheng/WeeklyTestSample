"""CIS 1348 Weekly Test 1"""

# This code collects information about the user and then displays it
# This code is not working. Please fix it.
# Rename the variables using the conventions learned in the course
# and add useful comments

# Asking for user input
print("\n")

# Collecting User Details
first_name = input("1) First name: ")
last_name = input("2) Last name:\b")
phone_prefix = input("3) Prefix of phone number (e.g., 123): ")
street_number = input("4) Street Number of your residence : ")
street_name = input("5) Street name : ")

city = input("6) City: ")
state= input("7) State: ")
zip_code = input("8) Zip code: ")

# Constructing the required return values
full_name = first_name + " " + last_name
phone_number = phone_prefix+"-xxx-xxxx"
full_address = street_number + " " + street_name
city_state_zip = city + ", " + state + " " + zip_code # Fixes conversion issue

# Display the collected information 
print("Collected Information:")
print("Full Name: ",full_name)
print("Phone Number: ",phone_number)
print("Full Address: ")
print(full_address)
print(city_state_zip) # Fixes duplicate full address print issue

