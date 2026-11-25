# Case Study 27: Advanced Numeric Pattern Generator

## 1. Problem Statement
Generate a symmetric hollow numeric diamond pattern based on user-specified height/dimension, incorporating input validation and precise spacing alignment.

## 2. Objectives
- Validate dimension constraints (positive integer between 2 and 9).
- Construct upper and lower halves of a hollow numeric diamond using nested loops.
- Maintain symmetry and alignment using string spacing.

## 3. Assumptions
- Dimension N represents the middle row number (valid range: 2 <= N <= 9 so single digits keep alignment clean).
- Row i displays digit i at the left and right boundaries with hollow spaces inside.

## 4. Algorithm
1. Start and read dimension N.
2. Validate that N is an integer in [2, 9]; if invalid, display an error and exit.
3. Loop i from 1 to N for the upper half: print (N - i) leading spaces, digit i, inner spaces (2*i - 3), and digit i (if i > 1).
4. Loop i from N - 1 down to 1 for the lower half using the same spacing formula.
5. Stop.

## 5. Flowchart
```
[Start] --> [Read Dimension N]
               |
               v
       [2 <= N <= 9 ?] --(No)--> [Print Error] --> [Stop]
               | Yes
               v
   [Loop i = 1 to N (Upper Half)]
               |
               v
   [Print Leading Spaces + Edge Digits]
               |
               v
  [Loop i = N-1 down to 1 (Lower Half)]
               |
               v
   [Print Leading Spaces + Edge Digits] --> [Stop]
```

## 6. Pseudocode
```
BEGIN
  INPUT n
  IF n < 2 OR n > 9 THEN
    PRINT "Invalid dimension"
    EXIT
  ENDIF
  FOR i = 1 TO n DO
    PRINT spaces(n - i) + str(i)
    IF i > 1 THEN
      PRINT spaces(2 * i - 3) + str(i)
    ENDIF
    NEWLINE
  ENDFOR
  FOR i = n - 1 DOWNTO 1 DO
    PRINT spaces(n - i) + str(i)
    IF i > 1 THEN
      PRINT spaces(2 * i - 3) + str(i)
    ENDIF
    NEWLINE
  ENDFOR
END
```

## 7. Python Source Code (`code.py`)
```python
# Case Study 27: Advanced Numeric Pattern Generator
test_dimensions = [5, 1, 12]

for n in test_dimensions:
    print(f"Testing Dimension N = {n}:")
    if not isinstance(n, int) or n < 2 or n > 9:
        print("  [Error] Dimension must be an integer between 2 and 9.\n")
        continue

    # Upper half including middle row
    for i in range(1, n + 1):
        line = " " * (n - i) + str(i)
        if i > 1:
            line += " " * (2 * i - 3) + str(i)
        print("  " + line)

    # Lower half
    for i in range(n - 1, 0, -1):
        line = " " * (n - i) + str(i)
        if i > 1:
            line += " " * (2 * i - 3) + str(i)
        print("  " + line)
    print()
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: N = 5 | Valid dimension | 9-row symmetric hollow numeric diamond (1 to 5 to 1) |
| TC2: N = 1 | Below minimum size | Error message displayed |
| TC3: N = 12 | Exceeds single-digit limit | Error message displayed |

## 9. Conclusion
Nested iteration and mathematical spacing expressions produce aligned geometric numeric patterns while input validation prevents malformed layouts.
