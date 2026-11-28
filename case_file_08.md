# Activity 08 (Case Study #48): Tuple-Based Employee Shift Conflict Detection

## 1. Problem Statement
Store employee shift schedules as tuples containing employee ID, day, start hour, and end hour, compare shift intervals, and detect overlapping assignments.

## 2. Objectives
- Represent immutable shift records using tuples and unpack their elements.
- Compare pairs of shifts belonging to the same employee on the same day.
- Detect interval overlaps using start1 < end2 and start2 < end1.

## 3. Assumptions
- Hours are represented in 24-hour integer format (0 to 24), with start < end.
- Back-to-back shifts (e.g., 9–13 and 13–17) do not overlap.

## 4. Algorithm
1. Start and load list of shift tuples (emp_id, emp_name, day, start, end).
2. Use nested loops (i from 0 to n-1, j from i+1 to n-1) to compare unique pairs of shifts.
3. Unpack both tuples; if emp_id matches and day matches, check if start1 < end2 and start2 < end1.
4. If true, record and print the conflicting shift pair.
5. Summarize all employees with scheduling conflicts and stop.

## 5. Flowchart
```
+-------------------------------------------------------+
|                        [START]                        |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|                Load Shift Tuples List                 |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|    Outer Loop i = 0..n-2; Inner Loop j = i+1..n-1     |
+-------------------------------------------------------+
            |                                   |
      (Next Pair i, j)                    (Loops Done)
            |                                   |
            v                                   |
+-----------------------+                       |
| Unpack Tuple i and    |                       |
| Tuple j               |                       |
+-----------------------+                       |
            |                                   |
            v                                   |
     /-------------\                            |
    / Same Emp &    \                           |
   /  Same Day &     \                          |
  /   Start1 < End2 & \                         |
 /    Start2 < End1?   \                        |
 \---------------------/                        |
     /             \                            |
   Yes              No                          |
   /                 \                          |
  v                   v                         |
+-------------------+ +---------------+         |
| Report Shift      | | Continue Loop |         |
| Conflict          | +---------------+         |
+-------------------+         |                 |
         \                   /                  |
          \                 /                   |
           +-------+-------+                    |
                   |                            |
                   +------> (Next j / i)        |
                                                v
                                        +---------------+
                                        |    [STOP]     |
                                        +---------------+
```

## 6. Pseudocode
```
BEGIN
  conflicts = 0
  FOR i = 0 TO len(shifts) - 2 DO
    (id1, name1, day1, s1, e1) = shifts[i]
    FOR j = i + 1 TO len(shifts) - 1 DO
      (id2, name2, day2, s2, e2) = shifts[j]
      IF id1 == id2 AND day1 == day2 THEN
        IF s1 < e2 AND s2 < e1 THEN
          PRINT "CONFLICT:", name1, day1, (s1, e1), (s2, e2)
          conflicts = conflicts + 1
        ENDIF
      ENDIF
    ENDFOR
  ENDFOR
  PRINT "Total Conflicts:", conflicts
END
```

## 7. Python Source Code (`08_Tuple_Employee_Shift_Conflict.py`)
```python
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
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: Kiran Mon (9-14) & (13-18) | 13 < 14 and 9 < 18 | Conflict flagged |
| TC2: Meera Mon (10-16) & (16-20) | Adjacent intervals (16 == 16) | No conflict |
| TC3: Rohan Tue (8-12) & (9-11) | Contained interval overlap | Conflict flagged |

## 9. Conclusion
Tuple unpacking combined with interval-intersection logic cleanly detects overlapping workforce schedules.
