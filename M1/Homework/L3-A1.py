
total = int(input("Enter total number of working days: "))
absent = int(input("Enter total number of days absent: "))


attended = total - absent
attendance_percentage = (attended / total) * 100


if attendance_percentage < 75:
    print("You are not eligible to sit in the exam.")
else:
    print("You are eligible to sit in the exam.")
