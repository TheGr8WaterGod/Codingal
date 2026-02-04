# Taking personal details from the user
first = input("Enter your first name: ")
last = input("Enter your last name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))
fav_subject = input("Enter your favourite subject: ")

# Storing in a tuple
personal_details = (first, last, age, height, weight, fav_subject)

print("\nTuple:", personal_details)

# Converting to list
details_list = list(personal_details)

print("List:", details_list)