# Case Study 29: Password Policy Validation Engine

## 1. Problem Statement
Evaluate candidate password strings against length, uppercase, lowercase, digit, special character, consecutive repetition, and prohibited substring rules, reporting every failed condition.

## 2. Objectives
- Inspect strings character-by-character using loops and string methods.
- Detect consecutive repeated characters (e.g., 'aaa') and forbidden substrings.
- Provide clear diagnostic feedback listing all unmet policy rules.

## 3. Assumptions
- Minimum password length is 8 characters.
- Must contain at least 1 uppercase, 1 lowercase, 1 digit, and 1 special character from '@#$%&*!'.
- No character may repeat 3 or more times consecutively.
- Must not contain forbidden words ('password', '1234', 'admin') case-insensitively.

## 4. Algorithm
1. Start and load list of test passwords and prohibited substrings.
2. For each password, initialize an empty list of errors.
3. Check length >= 8; if false, record error.
4. Iterate through characters to count uppercase, lowercase, digits, special chars, and check if ch == prev1 == prev2.
5. Check if any prohibited substring exists in password.lower().
6. If errors list is empty, mark VALID; otherwise print all error reasons.
7. Stop.

## 5. Flowchart
```
[Start] --> [Read Password String]
               |
               v
       [Check Length >= 8]
               |
               v
  [Scan Chars: Upper/Lower/Digit/Special/Repeat]
               |
               v
   [Check Forbidden Substrings]
               |
               v
       [Errors Empty?]
         /                Yes          No
        |            |
 [Print VALID]  [Print All Failed Rules]
        \_____ _____/
              |
              v
           [Stop]
```

## 6. Pseudocode
```
BEGIN
  FOR EACH pwd IN passwords DO
    errors = []
    IF len(pwd) < 8 THEN APPEND "Min length 8" TO errors
    Scan pwd for has_upper, has_lower, has_digit, has_special, triple_repeat
    IF NOT has_upper THEN APPEND "Missing uppercase" TO errors
    IF NOT has_lower THEN APPEND "Missing lowercase" TO errors
    IF NOT has_digit THEN APPEND "Missing digit" TO errors
    IF NOT has_special THEN APPEND "Missing special char" TO errors
    IF triple_repeat THEN APPEND "3+ consecutive identical chars" TO errors
    IF any forbidden word in lower(pwd) THEN APPEND "Contains forbidden word" TO errors
    IF errors is empty THEN PRINT "VALID" ELSE PRINT errors
  ENDFOR
END
```

## 7. Python Source Code (`code.py`)
```python
# Case Study 29: Password Policy Validation Engine
passwords = [
    "Secur3@Home",
    "pass1234",
    "AAAbbb111@",
    "Admin@2026"
]

forbidden = ["password", "1234", "admin", "qwerty"]
special_chars = "@#$%&*!"

for pwd in passwords:
    errors = []
    if len(pwd) < 8:
        errors.append("Must be at least 8 characters long.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_triple_repeat = False

    for i in range(len(pwd)):
        ch = pwd[i]
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

        if i >= 2 and pwd[i] == pwd[i - 1] == pwd[i - 2]:
            has_triple_repeat = True

    if not has_upper:
        errors.append("Missing at least one uppercase letter.")
    if not has_lower:
        errors.append("Missing at least one lowercase letter.")
    if not has_digit:
        errors.append("Missing at least one numeric digit.")
    if not has_special:
        errors.append(f"Missing a special character ({special_chars}).")
    if has_triple_repeat:
        errors.append("Contains 3 or more consecutive identical characters.")

    lower_pwd = pwd.lower()
    for word in forbidden:
        if word in lower_pwd:
            errors.append(f"Contains prohibited substring '{word}'.")

    print(f"Password: '{pwd}'")
    if not errors:
        print("  Status: VALID\n")
    else:
        print("  Status: INVALID")
        for err in errors:
            print(f"   - {err}")
        print()
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: 'Secur3@Home' | Meets all complexity and length rules | VALID |
| TC2: 'pass1234' | No upper, no special, contains '1234' | INVALID (3 errors reported) |
| TC3: 'AAAbbb111@' | Has triple consecutive characters | INVALID (triple repeat reported) |

## 9. Conclusion
The string-based validator thoroughly inspects password structure without external regex libraries, providing actionable security feedback.
