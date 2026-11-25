# Case Study 11: Examination Result and Grace-Mark Validation

## 1. Problem Statement
Develop a system to evaluate student marks across multiple subjects, enforce subject-wise pass marks, allocate limited grace marks without exceeding maximum marks per subject, and assign final grades.

## 2. Objectives
- Process subject-wise marks stored in lists and tuples.
- Apply conditional rules to distribute up to 5 grace marks for borderline failures.
- Ensure moderated marks never exceed 100 and classify overall student performance.

## 3. Assumptions
- Maximum marks per subject = 100; pass mark = 40.
- Total grace mark pool per student = 5 marks, applicable only if it helps pass failed subjects.
- Grading on aggregate percentage: >=75 Distinction, >=60 First Class, >=50 Second Class, >=40 Pass, else Fail.

## 4. Algorithm
1. Start and load student records containing name and list of subject marks.
2. For each student, initialize available grace = 5 and check each subject.
3. If a subject mark is between 35 and 39 and sufficient grace remains, add required grace to reach 40.
4. Check if all subjects are >= 40 after grace allocation.
5. Compute aggregate percentage and assign final division/classification.
6. Display original marks, final marks, grace used, and result.
7. Stop.

## 5. Flowchart
```
[Start] --> [Load Student Marks List]
               |
               v
     [Loop Over Each Student] --> (Done) --> [Stop]
               |
               v
   [Check Subjects < 40 (35..39)]
               |
        /--(Grace >= Needed?)--      Yes                      No
       |                        |
[Add Grace to 40]        [Leave Unchanged]
       \___________ ___________/
                   |
                   v
       [All Subjects >= 40?]
            /                     Yes            No
           |              |
   [Compute Grade]   [Mark FAIL]
           \______ ______/
                  |
                  v
           [Print Report]
```

## 6. Pseudocode
```
BEGIN
  FOR EACH (name, marks) IN students DO
    grace_left = 5
    final_marks = copy of marks
    FOR i = 0 TO length(final_marks) - 1 DO
      IF final_marks[i] < 40 THEN
        needed = 40 - final_marks[i]
        IF needed <= grace_left THEN
          final_marks[i] = min(100, final_marks[i] + needed)
          grace_left = grace_left - needed
        ENDIF
      ENDIF
    ENDFOR
    IF all m >= 40 in final_marks THEN
      Compute percentage and grade
    ELSE
      grade = "Fail"
    ENDIF
    PRINT name, marks, final_marks, grade
  ENDFOR
END
```

## 7. Python Source Code (`code.py`)
```python
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
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: Ananya [78, 82, 37, 91, 68] | 37 boosted to 40 using 3 grace marks | 71.80% | First Class |
| TC2: Rahul [55, 36, 38, 62, 59] | 36->40 (4 grace), 38 cannot pass (1 left) | Fail |
| TC3: Sneha [45, 32, 60, 58, 70] | Deficit 8 > 5 max grace | Fail |

## 9. Conclusion
The solution systematically enforces subject-wise passing thresholds, distributes finite grace marks fairly without exceeding maximum limits, and classifies final results.
