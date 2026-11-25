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
