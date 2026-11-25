# Case Study 02: Progressive Electricity Billing
monthly_units = [95, 180, 250, 430, 390]
months = ["Jan", "Feb", "Mar", "Apr", "May"]

bills = []
print(f"{'Month':<8}{'Units':<10}{'Bill (Rs.)':<15}{'Status'}")
print("-" * 50)

for i in range(len(monthly_units)):
    units = monthly_units[i]
    if units < 0:
        print(f"{months[i]:<8}Invalid reading")
        continue

    # Progressive slab calculation
    if units <= 100:
        energy_cost = units * 3.0
    elif units <= 200:
        energy_cost = (100 * 3.0) + (units - 100) * 5.0
    elif units <= 400:
        energy_cost = (100 * 3.0) + (100 * 5.0) + (units - 200) * 7.0
    else:
        energy_cost = (100 * 3.0) + (100 * 5.0) + (200 * 7.0) + (units - 400) * 9.0

    fixed_charge = 100.0
    total = energy_cost + fixed_charge

    # Rebate or Surcharge
    if units <= 100:
        total -= total * 0.05  # 5% rebate
    elif units > 400:
        total += total * 0.10  # 10% surcharge

    bills.append(round(total, 2))

    # Month-over-month comparison
    status = "Baseline"
    if i > 0:
        pct_change = ((bills[i] - bills[i - 1]) / bills[i - 1]) * 100
        if pct_change > 25:
            status = f"UNUSUAL (+{pct_change:.1f}%)"
        else:
            status = f"Normal ({pct_change:+.1f}%)"

    print(f"{months[i]:<8}{units:<10}{bills[i]:<15.2f}{status}")
