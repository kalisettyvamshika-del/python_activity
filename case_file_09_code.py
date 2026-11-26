# Activity 09 (Case Study #57): Smart Canteen Order and Stock Management
menu = ["Idli", "Dosa", "Coffee", "Sandwich"]
prices = [30, 50, 20, 60]
stock = [20, 15, 30, 10]

orders = [
    ("Order-1", [("Idli", 4), ("Coffee", 2)]),
    ("Order-2", [("Dosa", 10), ("Sandwich", 6)]),
    ("Order-3", [("Dosa", 8), ("Sandwich", 4)])  # Dosa only has 5 left -> rejected
]

total_revenue = 0

print("--- CANTEEN ORDER PROCESSING ---")
for order_id, items in orders:
    order_total = 0
    print(f"Processing {order_id}:")
    for item_name, qty in items:
        if item_name not in menu:
            print(f"  [REJECTED] {item_name}: Not on menu.")
            continue
        idx = menu.index(item_name)
        if qty <= stock[idx]:
            stock[idx] -= qty
            cost = qty * prices[idx]
            order_total += cost
            print(f"  [FULFILLED] {item_name} x{qty} = Rs.{cost}")
        else:
            print(f"  [REJECTED] {item_name} x{qty} (Only {stock[idx]} available)")
    total_revenue += order_total
    print(f"  Order Bill: Rs.{order_total}\n")

print("--- DAILY SUMMARY ---")
print(f"Total Sales Revenue: Rs.{total_revenue}")
print("Remaining Stock:")
for i in range(len(menu)):
    print(f"  {menu[i]:<10}: {stock[i]} units")
