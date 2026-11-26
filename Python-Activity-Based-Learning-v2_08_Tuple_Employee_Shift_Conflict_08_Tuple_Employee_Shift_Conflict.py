# Activity 08 (Case Study #48): Tuple-Based Employee Shift Conflict Detection
shifts = [
    ("E101", "Kiran", "Mon", 9, 14),
    ("E102", "Meera", "Mon", 10, 16),
    ("E101", "Kiran", "Mon", 13, 18),   # Overlaps with E101 Mon 9-14
    ("E102", "Meera", "Mon", 16, 20),   # Adjacent (16 == 16), valid
    ("E103", "Rohan", "Tue", 8, 12),
    ("E103", "Rohan", "Tue", 9, 11)     # Overlaps inside E103 Tue 8-12
]

conflicted_employees = []
print("--- SHIFT CONFLICT AUDIT ---")

for i in range(len(shifts)):
    id1, name1, day1, s1, e1 = shifts[i]
    for j in range(i + 1, len(shifts)):
        id2, name2, day2, s2, e2 = shifts[j]
        if id1 == id2 and day1 == day2:
            if s1 < e2 and s2 < e1:
                print(f"[CONFLICT] {name1} ({id1}) on {day1}: ({s1}:00-{e1}:00) overlaps with ({s2}:00-{e2}:00)")
                if name1 not in conflicted_employees:
                    conflicted_employees.append(name1)

print("\nEmployees with Conflicting Schedules:", conflicted_employees)
