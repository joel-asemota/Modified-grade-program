def english_grades(test_1, test_2):
    result = test_1 + test_2 / 2
    if result >= 64:
        grade = "C"
    elif result >= 84:
        grade = "B"
    elif result >= 104:
        grade = "A"
    total = test_1 + test_2
    return grade, total

def math_grades(test_1, test_2, test_3):
    result = test_1 + test_2 + test_3 / 3
    if result >= 56:
        grade = "C"
    elif result >= 64:
        grade = "B"
    elif result >= 78:
        grade = "A"
    total = test_1 + test_2 + test_3
    return grade, total

def science_grades(test_1, test_2, test_3):
    result = test_1 + test_2 + test_3 / 3
    if result >= 96:
        grade = "C"
    elif result >= 113:
        grade = "B"
    elif result >= 128:
        grade = "A"
    total = test_1 + test_2 + test_3
    return grade, total

choice = input("what would you like to work out 1. english 2. maths 3. science")
if choice == "1":
    while True:
        try:
            test_1 = int(input("input first test result"))
            test_2 = int(input("input second test result"))
            break
        except ValueError:
            print("please try again")
    grade, total = english_grades(test_1, test_2)
    print(f"your grade is {grade} your total score is {total}")
elif choice == "2":
    while True:
        try:
            test_1 = int(input("input first test result"))
            test_2 = int(input("input second test result"))
            test_3 = int(input("input third test result"))
            break
        except ValueError:
            print("please try again")
    grade, total = math_grades(test_1, test_2, test_3)
    print(f"you grade is {grade} your total score is {total}")
elif choice == "3":
    while True:
        try:
            test_1 = int(input("input the first test result"))
            test_2 = int(input("input second test result"))
            test_3 = int(input("input third test result"))
            break
        except ValueError:
            print("please try again")
    
    grade, total = science_grades(test_1, test_2, test_3)
    print(f"you grade is {grade} your total score is {total}")
    

  






