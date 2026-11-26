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
