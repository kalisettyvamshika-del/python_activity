# Activity 09 (Case Study #57): Smart Canteen Order and Stock Management

## 1. Problem Statement
Process sequential canteen customer orders, calculate bills, deduct ordered quantities from live inventory, reject items exceeding available stock, and output a daily revenue and inventory summary.

## 2. Objectives
- Maintain menu prices and stock counts using parallel lists.
- Validate stock availability before fulfilling order line items.
- Track total daily sales and remaining stock across multiple customer orders.

## 3. Assumptions
- Partial order fulfillment is allowed: available items in an order are billed while out-of-stock items are rejected.
- Menu items, prices, and initial stock are stored in parallel lists.

## 4. Algorithm
1. Start with parallel lists: items, prices, stock, and a list of customer orders.
2. Initialize total_revenue = 0.
3. For each order, initialize order_bill = 0 and iterate through requested (item_name, qty).
4. Find item_name in items list; check if qty <= stock[idx].
5. If available, deduct stock[idx] -= qty and add qty * prices[idx] to order_bill; otherwise print rejection notice.
6. Add order_bill to total_revenue and display remaining stock at the end.
7. Stop.

## 5. Flowchart
```
+-------------------------------------------------------+
|                        [START]                        |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|       Init Menu, Prices, Stock, Revenue = 0           |
+-------------------------------------------------------+
                            |
                            v
+-------------------------------------------------------+
|                 Next Customer Order                   |
+-------------------------------------------------------+
            |                                   |
        (Order)                              (None)
            |                                   |
            v                                   v
+---------------------------------------+ +-------------+
|         Loop Item, Qty in Order       | | Print Daily |
+---------------------------------------+ | Summary     |
            |                   |         +-------------+
     (Next Item, Qty)     (Order Done)          |
            |                   |               v
            v                   |         +-----------+
     /-------------\            |         |  [STOP]   |
    / Qty <=        \           |         +-----------+
   /  Stock[Item]?   \          |
   \-----------------/          |
     /             \            |
   Yes              No          |
   /                 \          |
  v                   v         |
+-------------------+ +---------------+
| Deduct Stock,     | | Reject Item   |
| Add to Bill       | +---------------+
+-------------------+         |
         \                   /
          \                 /
           v               v
+---------------------------------------+
|         Update Total Revenue          |
+---------------------------------------+
            |
            +------> (Back to Next Customer Order)
```

## 6. Pseudocode
```
BEGIN
  total_revenue = 0
  FOR EACH (cust_id, order_items) IN orders DO
    bill = 0
    FOR EACH (item, qty) IN order_items DO
      idx = index of item in menu
      IF qty <= stock[idx] THEN
        stock[idx] = stock[idx] - qty
        bill = bill + qty * prices[idx]
      ELSE
        PRINT "Unavailable:", item
      ENDIF
    ENDFOR
    total_revenue = total_revenue + bill
    PRINT cust_id, bill
  ENDFOR
  PRINT total_revenue, stock
END
```

## 7. Python Source Code (`09_Smart_Canteen_Order_Stock.py`)
```python
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
```

## 8. Test Cases
| Test Case | Input / Scenario | Expected Output |
| :--- | :--- | :--- |
| TC1: Order-1 (4 Idli, 2 Coffee) | Sufficient stock (20, 30) | Bill Rs.160; stock becomes 16, 28 |
| TC2: Order-2 (10 Dosa, 6 Sandwich) | Sufficient stock (15, 10) | Bill Rs.860; stock becomes 5, 4 |
| TC3: Order-3 (8 Dosa, 4 Sandwich) | Dosa has 5 < 8; Sandwich has 4 | Dosa rejected, Sandwich fulfilled (Bill Rs.240) |

## 9. Conclusion
Real-time inventory decrements prevent overselling while maintaining accurate order billing and end-of-day stock visibility.
