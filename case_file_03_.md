# Case Study 03: ATM Transaction Sequence Simulation

## 1. Problem Statement
Simulate a sequence of ATM deposits and withdrawals while maintaining account balance, enforcing per-transaction and daily withdrawal limits, rejecting invalid operations, and generating a transaction summary.

## 2. Objectives
- Iterate through a tuple/list of transaction instructions using loops.
- Validate positive amounts, multiples of 100, sufficient funds, and withdrawal caps.
- Summarize total deposits, total withdrawals, rejected operations, and closing balance.

## 3. Assumptions
- Initial account balance = Rs. 15,000.
- Per-transaction withdrawal limit = Rs. 10,000; daily withdrawal limit = Rs. 20,000.
- All transactions must be positive multiples of Rs. 100.

## 4. Algorithm
1. Start with initial balance = 15000, daily_withdrawn = 0, and counters for accepted/rejected transactions.
2. Read each transaction tuple (type, amount) from the sequence.
3. Check if amount > 0 and amount % 100 == 0; otherwise reject.
4. If type is 'DEPOSIT', add amount to balance.
5. If type is 'WITHDRAW', verify amount <= 10000, daily_withdrawn + amount <= 20000, and amount <= balance; otherwise reject.
6. Log transaction outcome and update totals.
7. Print final ATM summary and stop.

## 5. Flowchart
```
+-------------------------------------------------------+
|                        [START]                        |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|             Init Balance = 15000, Daily = 0           |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|             Next Transaction (Type, Amt)              |
+-------------------------------------------------------+
            |                                   |
     (Transaction)                          (None)
            |                                   |
            v                                   v
     /-------------\                    +---------------+
    / Amt > 0 &     \                   | Print Summary |
   /  Amt % 100 == 0?\                  +---------------+
   \-----------------/                          |
     /             \                            v
   Yes              No                  +---------------+
   /                 \                  |    [STOP]     |
  v                   v                 +---------------+
+---------------+ +-------------------+
| Type ==       | | Reject: Invalid   |
| DEPOSIT?      | | Amt               |
+---------------+ +-------------------+
     /       \          |
   Yes        No        |
   /           \        |
  v             v       |
+-----------+ /---------------------------------\
| Balance +=| | Amt <= 10k & Daily + Amt <= 20k |
| Amt       | | & Amt <= Balance?               |
+-----------+ \---------------------------------/
     |          /               \
     |        Yes                No
     |        /                   \
     |       v                     v
     | +-----------------------+ +-------------------+
     | | Balance -= Amt,       | | Reject: Limit /   |
     | | Daily += Amt          | | Funds             |
     | +-----------------------+ +-------------------+
     |       |                           |
     +-------+---------------------------+
             |
             +------> (Back to Next Transaction)
```

## 6. Pseudocode
```
BEGIN
  balance = 15000
  daily_withdrawn = 0
  FOR EACH (txn_type, amount) IN transactions DO
    IF amount <= 0 OR amount MOD 100 != 0 THEN
      PRINT "REJECTED: Invalid denomination"
    ELSE IF txn_type == "DEPOSIT" THEN
      balance = balance + amount
      PRINT "APPROVED: Deposit"
    ELSE IF txn_type == "WITHDRAW" THEN
      IF amount > 10000 OR daily_withdrawn + amount > 20000 OR amount > balance THEN
        PRINT "REJECTED: Limit or balance exceeded"
      ELSE
        balance = balance - amount
        daily_withdrawn = daily_withdrawn + amount
        PRINT "APPROVED: Withdrawal"
      ENDIF
    ENDIF
  ENDFOR
  PRINT balance, daily_withdrawn
END
```

## 7. Python Source Code (`code.py`)
```python
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
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: WITHDRAW 5000 | Valid multiple of 100, within limits | APPROVED -> Balance Rs.10000 |
| TC2: WITHDRAW 12000 | Exceeds Rs.10,000 single cap | REJECTED -> Exceeds single limit |
| TC3: WITHDRAW 7000 (after 14000) | Cumulative 21000 > Rs.20,000 daily cap | REJECTED -> Exceeds daily limit |

## 9. Conclusion
The simulation enforces banking rules across sequential transactions, accurately guarding against invalid denominations, overdrafts, and daily withdrawal limits.
