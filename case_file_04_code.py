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
