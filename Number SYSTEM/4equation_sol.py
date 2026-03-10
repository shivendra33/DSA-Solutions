sem = int(input("Enter semesters: "))

for i in range(sem):
    subjects = int(input("Enter subjects: "))
    marks = list(map(int,input().split()))

    for m in marks:
        if m < 0 or m > 100:
            print("Invalid mark")
            exit()

    print("Maximum mark:",max(marks))