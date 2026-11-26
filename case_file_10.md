# Activity 10 (Case Study #88): Multi-Branch Retail Inventory Transfer

## 1. Problem Statement
Compare current stock levels across retail branches against target stock levels, calculate surpluses and shortages, and generate inter-branch stock transfers subject to maximum transfer batch limits.

## 2. Objectives
- Compute branch surpluses and shortages using parallel lists.
- Match surplus branches with shortage branches iteratively.
- Respect a maximum single-transfer cap per shipment.

## 3. Assumptions
- Single product tracked across 4 branches.
- Maximum units allowed per single inter-branch transfer = 25 units.
- Branches only transfer excess stock above their target level.

## 4. Algorithm
1. Start with lists of branches, current_stock, and target_stock, plus MAX_TRANSFER = 25.
2. Compute diff[i] = current_stock[i] - target_stock[i] for each branch (positive = surplus, negative = shortage).
3. Loop over branches with shortages (diff[i] < 0).
4. For each shortage branch, loop over branches with surpluses (diff[j] > 0) and transfer min(needed, available, MAX_TRANSFER).
5. Update current_stock and diff lists, and record each transfer.
6. Print transfer manifest and final stock levels; stop.

## 5. Flowchart
```
[Start] --> [Compute Diff = Current - Target]
               |
               v
     [Loop Shortage Branches (Diff < 0)] --> (None) --> [Print Final Stock] --> [Stop]
               |
               v
     [Loop Surplus Branches (Diff > 0)]
               |
               v
 [Qty = min(Shortage, Surplus, Max_Cap)]
               |
               v
 [Update Stocks & Record Transfer]
```

## 6. Pseudocode
```
BEGIN
  MAX_CAP = 25
  FOR i = 0 TO n - 1 DO diff[i] = current[i] - target[i]
  FOR i = 0 TO n - 1 DO
    WHILE diff[i] < 0 AND exists j with diff[j] > 0 DO
      qty = min(-diff[i], diff[j], MAX_CAP)
      diff[i] = diff[i] + qty
      diff[j] = diff[j] - qty
      current[i] = current[i] + qty
      current[j] = current[j] - qty
      PRINT "Transfer", qty, "from", branch[j], "to", branch[i]
    ENDWHILE
  ENDFOR
  PRINT current
END
```

## 7. Python Source Code (`10_Multi_Branch_Inventory_Transfer.py`)
```python
# Activity 10 (Case Study #88): Multi-Branch Retail Inventory Transfer
branches = ["North", "South", "East", "West"]
current_stock = [120, 45, 30, 105]
target_stock = [80, 80, 70, 70]
MAX_TRANSFER = 25

diff = [current_stock[i] - target_stock[i] for i in range(len(branches))]

print("Initial Stock :", list(zip(branches, current_stock)))
print("Target Stock  :", list(zip(branches, target_stock)))
print("\n--- GENERATED TRANSFER PLAN (Max 25/shipment) ---")

for i in range(len(branches)):
    if diff[i] < 0:  # Branch i has a shortage
        for j in range(len(branches)):
            while diff[i] < 0 and diff[j] > 0:
                transfer_qty = min(-diff[i], diff[j], MAX_TRANSFER)
                diff[i] += transfer_qty
                diff[j] -= transfer_qty
                current_stock[i] += transfer_qty
                current_stock[j] -= transfer_qty
                print(f"Transfer {transfer_qty:>2} units: {branches[j]} -> {branches[i]}")

print("\nFinal Stock   :", list(zip(branches, current_stock)))
for i in range(len(branches)):
    if diff[i] < 0:
        print(f"Unmet Shortage at {branches[i]}: {-diff[i]} units")
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: North surplus (40) -> South shortage (35) | Capped at 25 per transfer | Two shipments: 25 + 10 units |
| TC2: West surplus (35) -> East shortage (40) | North has 5 left, West has 35 | 5 from North + 25 + 10 from West |
| TC3: Post-transfer balance check | Total stock = 300, total target = 300 | All branches reach exact target |

## 9. Conclusion
The balancing algorithm redistributes surplus inventory to deficit branches while respecting per-shipment capacity constraints.
