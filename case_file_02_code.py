# Case Study 11: Examination Result and Grace-Mark Validation
students = [
    ("Ananya", [78, 82, 37, 91, 68]),
    ("Rahul", [55, 36, 38, 62, 59]),
    ("Sneha", [45, 32, 60, 58, 70]),
    ("Vikram", [88, 92, 85, 90, 94])
]

MAX_MARKS = 100
PASS_MARKS = 40
MAX_GRACE = 5

for name, marks in students:
    grace_pool = MAX_GRACE
    updated_marks = list(marks)

    for i in range(len(updated_marks)):
        if updated_marks[i] < PASS_MARKS:
            deficit = PASS_MARKS - updated_marks[i]
            if deficit <= grace_pool:
                updated_marks[i] = min(MAX_MARKS, updated_marks[i] + deficit)
                grace_pool -= deficit

    passed_all = True
    for m in updated_marks:
        if m < PASS_MARKS:
            passed_all = False
            break

    total = sum(updated_marks)
    pct = total / len(updated_marks)

    if not passed_all:
        grade = "Fail"
    elif pct >= 75:
        grade = "Distinction"
    elif pct >= 60:
        grade = "First Class"
    elif pct >= 50:
        grade = "Second Class"
    else:
        grade = "Pass"

    print(f"Student: {name}")
    print(f"  Original Marks : {marks}")
    print(f"  Moderated Marks: {updated_marks} (Grace Used: {MAX_GRACE - grace_pool})")
    print(f"  Percentage     : {pct:.2f}% | Result: {grade}\n")
