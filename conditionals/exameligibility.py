total = int(input("Enter total number of working days:"))
print("Total number of working days is:", total)
absent= int(input("Enter number of absent days:"))
print ("total number of absent days is:", absent)
present= total - absent
percentage = (present/total)*100
print(f"Attendance percentage:{percentage}")

if percentage < 75:
    print("You are not eligible to write this exam")
else:
    print("You are eligible to write this exam")
