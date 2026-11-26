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
