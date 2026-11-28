# Activity 07 (Case Study #42): Student Marks Matrix Analysis

## 1. Problem Statement
Analyze a 2D nested list (matrix) of student marks across multiple subjects to compute student-wise totals/averages, subject-wise averages, top performers, and weak subjects.

## 2. Objectives
- Traverse rows and columns of a nested list matrix.
- Compute student averages (row-wise) and subject averages (column-wise).
- Identify the highest-scoring student and subjects averaging below 60.

## 3. Assumptions
- Rows represent students; columns represent subjects.
- A subject average < 60 is flagged as low-performing.

## 4. Algorithm
1. Start with lists of student names, subject names, and a 2D marks matrix.
2. Loop through each row to compute student total and average; track the highest total.
3. Loop through each column index to sum subject marks across all students and compute subject average.
4. Flag any subject whose average < 60.
5. Display row stats, column stats, top performer, and weak subjects.
6. Stop.

## 5. Flowchart
```
+-------------------------------------------------------+
|                        [START]                        |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|            Load Names, Subjects, 2D Matrix            |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|        Row Loop: Compute Student Totals & Topper      |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|      Col Loop: Compute Subject Avgs & Weak List       |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|             Display Complete Matrix Report            |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|                        [STOP]                         |
+-------------------------------------------------------+
```

## 6. Pseudocode
```
BEGIN
  top_total = -1
  FOR i = 0 TO num_students - 1 DO
    row_sum = sum(matrix[i])
    PRINT students[i], row_sum, row_sum / num_subjects
    IF row_sum > top_total THEN
      top_total = row_sum
      topper = students[i]
    ENDIF
  ENDFOR
  FOR j = 0 TO num_subjects - 1 DO
    col_sum = 0
    FOR i = 0 TO num_students - 1 DO
      col_sum = col_sum + matrix[i][j]
    ENDFOR
    avg = col_sum / num_students
    IF avg < 60 THEN APPEND subjects[j] TO weak_subjects
  ENDFOR
  PRINT topper, weak_subjects
END
```

## 7. Python Source Code (`07_Student_Marks_Matrix.py`)
```python
# Activity 07 (Case Study #42): Student Marks Matrix Analysis
students = ["Aarav", "Bhavna", "Charan", "Divya"]
subjects = ["Math", "Physics", "CS", "English"]
marks_matrix = [
    [85, 72, 90, 78],
    [62, 54, 70, 68],
    [92, 88, 95, 84],
    [48, 42, 65, 60]
]

num_students = len(students)
num_subjects = len(subjects)

print("--- STUDENT-WISE PERFORMANCE ---")
top_score = -1
top_student = ""

for i in range(num_students):
    total = sum(marks_matrix[i])
    avg = total / num_subjects
    print(f"{students[i]:<10} | Total: {total:<4} | Avg: {avg:.2f}")
    if total > top_score:
        top_score = total
        top_student = students[i]

print(f"\nTop Performer: {top_student} ({top_score}/{num_subjects * 100})")

print("\n--- SUBJECT-WISE PERFORMANCE ---")
weak_subjects = []
for j in range(num_subjects):
    col_total = 0
    for i in range(num_students):
        col_total += marks_matrix[i][j]
    sub_avg = col_total / num_students
    flag = " [LOW PERFORMANCE]" if sub_avg < 60 else ""
    if sub_avg < 60:
        weak_subjects.append(subjects[j])
    print(f"{subjects[j]:<10} | Avg: {sub_avg:.2f}{flag}")

print("\nSubjects Needing Attention:", weak_subjects if weak_subjects else "None")
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: Row-wise aggregation | Charan [92, 88, 95, 84] | Total 359, Avg 89.75 (Top Performer) |
| TC2: Column-wise aggregation | Physics [72, 54, 88, 42] | Avg 64.00 (Normal) |
| TC3: Low performance detection | If Physics scores drop below 60 avg | Flagged in weak_subjects |

## 9. Conclusion
Nested list traversal enables simultaneous row-wise student evaluation and column-wise subject diagnostics.
