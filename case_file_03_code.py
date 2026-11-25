# Case Study 13: ATM Transaction Sequence Simulation
transactions = [
    ("WITHDRAW", 5000),
    ("DEPOSIT", 3000),
    ("WITHDRAW", 12000),   # Exceeds single txn limit (10,000)
    ("WITHDRAW", 250),     # Not multiple of 100
    ("WITHDRAW", 9000),
    ("WITHDRAW", 7000),    # Exceeds daily limit (5000+9000+7000 = 21000 > 20000)
    ("DEPOSIT", -500)      # Invalid negative amount
]

balance = 15000
daily_withdrawn = 0
total_deposited = 0
approved_count = 0
rejected_count = 0

SINGLE_LIMIT = 10000
DAILY_LIMIT = 20000

print("--- ATM TRANSACTION LOG ---")
for txn_type, amount in transactions:
    if amount <= 0 or amount % 100 != 0:
        print(f"[REJECTED] {txn_type:<10} Rs.{amount:<7} -> Amount must be positive multiple of 100")
        rejected_count += 1
        continue

    if txn_type == "DEPOSIT":
        balance += amount
        total_deposited += amount
        approved_count += 1
        print(f"[APPROVED] {txn_type:<10} Rs.{amount:<7} -> Balance: Rs.{balance}")

    elif txn_type == "WITHDRAW":
        if amount > SINGLE_LIMIT:
            print(f"[REJECTED] {txn_type:<10} Rs.{amount:<7} -> Exceeds single limit (Rs.{SINGLE_LIMIT})")
            rejected_count += 1
        elif daily_withdrawn + amount > DAILY_LIMIT:
            print(f"[REJECTED] {txn_type:<10} Rs.{amount:<7} -> Exceeds daily limit (Rs.{DAILY_LIMIT})")
            rejected_count += 1
        elif amount > balance:
            print(f"[REJECTED] {txn_type:<10} Rs.{amount:<7} -> Insufficient balance")
            rejected_count += 1
        else:
            balance -= amount
            daily_withdrawn += amount
            approved_count += 1
            print(f"[APPROVED] {txn_type:<10} Rs.{amount:<7} -> Balance: Rs.{balance}")
    else:
        print(f"[REJECTED] Unknown operation: {txn_type}")
        rejected_count += 1

print("\n--- SUMMARY ---")
print(f"Approved Transactions : {approved_count}")
print(f"Rejected Transactions : {rejected_count}")
print(f"Total Deposited       : Rs.{total_deposited}")
print(f"Total Withdrawn       : Rs.{daily_withdrawn}")
print(f"Closing Balance       : Rs.{balance}")
