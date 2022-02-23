# Author: JD 02/23/2022

grades = {"HW_9-1":100, "HW_9-2":100, "Mid-Year_Project_Proposal": 100, "Cycle_10_practice_quiz": 100, "Cycle_10_qioz": 96}

# By using a .values() mathod, the print() statement will print all the values of the dictionary, which are the grades
print(list(grades.values()))
# By using a for loop, the loop will iterate through each key of the dictionary and print it
for x in grades:
    print(x)

# By using a for loop with a .items() mathod, the loop will iterate through each item in the dictionary, and check if the value is greater or equal to 70.
# If it is, then the key and the value will be printed.
for k, v in grades.items():
    if v >= 70:
        print(k, v)
# By using a for loop with a .items() mathod, the loop will iterate through each item in the dictionary, and check if the value is less or equal to 50.
# If it is, then the key and the value will be printed.
for k, v in grades.items():
    if v <= 50:
        print(k, v)

