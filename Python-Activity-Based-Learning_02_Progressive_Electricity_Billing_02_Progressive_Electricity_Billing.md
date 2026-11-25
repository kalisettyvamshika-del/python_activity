# Case Study 02: Progressive Electricity Billing

## 1. Problem Statement
Design a Python program that calculates monthly household electricity bills using progressive consumption slabs, fixed charges, surcharges, and rebates, and compares bills across multiple months to flag unusual consumption increases.

## 2. Objectives
- Implement progressive slab-based billing calculations using conditional statements.
- Track monthly consumption and bill amounts using lists.
- Detect unusual month-over-month spikes (>25% increase) using loops and arithmetic operators.

## 3. Assumptions
- Slabs: 0–100 units @ Rs. 3/unit, 101–200 units @ Rs. 5/unit, 201–400 units @ Rs. 7/unit, >400 units @ Rs. 9/unit.
- Fixed meter charge is Rs. 100 per month.
- A 5% rebate applies if units <= 100; a 10% surcharge applies if units > 400.
- An increase > 25% compared to the previous month is flagged as unusual.

## 4. Algorithm
1. Start and initialize the list of monthly unit readings.
2. For each month, validate that units >= 0.
3. Calculate energy charge across progressive slabs.
4. Add fixed charge (100), then apply rebate (5% if units <= 100) or surcharge (10% if units > 400).
5. Store the final bill in a list and compare with the previous month's bill.
6. If percentage increase > 25%, flag as an unusual increase.
7. Display the monthly summary table and stop.

## 5. Flowchart
```
[Start] --> [Input Monthly Units List]
               |
               v
       [Loop Through Months] --> (End of List) --> [Display Summary] --> [Stop]
               |
               v
     [Compute Slab Energy Cost]
               |
               v
  [Add Fixed Charge + Rebate/Surcharge]
               |
               v
    [Compare With Previous Month]
               |
        /-----(>25%?)-----      Yes                 No
       |                   |
[Flag Unusual Spike]  [Mark Normal]
       \________ _________/
                |
                v
         [Next Month]
```

## 6. Pseudocode
```
BEGIN
  SET monthly_units = [95, 180, 260, 420]
  SET prev_bill = 0
  FOR i = 0 TO length(monthly_units) - 1 DO
    units = monthly_units[i]
    COMPUTE slab_cost based on slabs (100, 200, 400)
    bill = slab_cost + 100
    IF units <= 100 THEN bill = bill * 0.95
    ELSE IF units > 400 THEN bill = bill * 1.10
    ENDIF
    IF i > 0 AND ((bill - prev_bill) / prev_bill) * 100 > 25 THEN
      status = "UNUSUAL INCREASE"
    ELSE
      status = "NORMAL"
    ENDIF
    PRINT month, units, bill, status
    prev_bill = bill
  ENDFOR
END
```

## 7. Python Source Code (`code.py`)
```python
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
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: Low usage (95 units) | Slab 1 + Rs. 100 fixed - 5% rebate | Rs. 365.75 (Baseline) |
| TC2: Spike to 180 units | Slab 2 + Rs. 100 fixed | Rs. 800.00 (UNUSUAL +118.7%) |
| TC3: High usage (430 units) | All slabs + fixed + 10% surcharge | Rs. 2827.00 (UNUSUAL +119.1%) |

## 9. Conclusion
The program accurately computes progressive slab-based electricity tariffs, applies rebates and surcharges, and flags abnormal month-over-month spikes using basic Python lists, loops, and conditional logic.
