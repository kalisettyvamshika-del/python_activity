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
