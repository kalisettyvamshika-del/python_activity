# Activity 06 (Case Study #37): Nested Loop Calendar Generator

## 1. Problem Statement
Generate a cleanly aligned monthly calendar given the starting weekday index and total number of days in the month, validating inputs first.

## 2. Objectives
- Validate month day count (28–31) and starting weekday index (0=Sun to 6=Sat).
- Align initial blank slots before day 1 using loops.
- Break lines after every 7 columns (Saturday) using modulo arithmetic.

## 3. Assumptions
- Week starts on Sunday (0 = Sun, 1 = Mon, ..., 6 = Sat).
- Valid month lengths are 28, 29, 30, or 31.

## 4. Algorithm
1. Start and read month_name, start_day (0..6), and num_days (28..31).
2. Validate start_day and num_days; print error if out of bounds.
3. Print weekday headers: Sun Mon Tue Wed Thu Fri Sat.
4. Print leading blank spaces for columns 0 to start_day - 1.
5. Loop day from 1 to num_days: print formatted day number, and print a newline whenever (start_day + day) % 7 == 0.
6. Stop.

## 5. Flowchart
```
[Start] --> [Input Start_Day, Num_Days]
               |
               v
  [Valid Start(0..6) & Days(28..31)?] --(No)--> [Print Error] --> [Stop]
               | Yes
               v
      [Print Weekday Header]
               |
               v
   [Print Leading Empty Slots]
               |
               v
     [Loop Day = 1 to Num_Days]
               |
               v
 [Print Day; If (Start+Day)%7==0 -> Newline] --> [Stop]
```

## 6. Pseudocode
```
BEGIN
  IF start_day < 0 OR start_day > 6 OR num_days < 28 OR num_days > 31 THEN
    PRINT "Invalid inputs"
    EXIT
  ENDIF
  PRINT "Sun Mon Tue Wed Thu Fri Sat"
  FOR s = 0 TO start_day - 1 DO
    PRINT "    "
  ENDFOR
  FOR day = 1 TO num_days DO
    PRINT format(day, 3) + " "
    IF (start_day + day) MOD 7 == 0 THEN
      NEWLINE
    ENDIF
  ENDFOR
END
```

## 7. Python Source Code (`06_Nested_Loop_Calendar.py`)
```python
# Activity 06 (Case Study #37): Nested Loop Calendar Generator
test_months = [
    ("October 2026", 4, 31),   # Starts on Thursday (4), 31 days
    ("February 2024", 4, 29),  # Leap year February
    ("Invalid Month", 8, 32)   # Invalid parameters
]

for title, start_day, num_days in test_months:
    print(f"=== {title} ===")
    if start_day < 0 or start_day > 6 or num_days < 28 or num_days > 31:
        print("Error: Invalid start weekday (0-6) or days in month (28-31).\n")
        continue

    print("Sun Mon Tue Wed Thu Fri Sat")
    # Leading spaces for first week
    for _ in range(start_day):
        print("    ", end="")

    for day in range(1, num_days + 1):
        print(f"{day:>3} ", end="")
        if (start_day + day) % 7 == 0:
            print()
    print("\n")
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: start_day=4, num_days=31 | 1st falls under Thu, wraps after Sat | Properly aligned 5-week calendar |
| TC2: start_day=4, num_days=29 | Leap year validation | 29 days aligned accurately |
| TC3: start_day=8, num_days=32 | Invalid range check | Error message printed |

## 9. Conclusion
Using nested/sequential loops and modulo arithmetic, the program constructs formatted monthly calendars without relying on external calendar modules.
