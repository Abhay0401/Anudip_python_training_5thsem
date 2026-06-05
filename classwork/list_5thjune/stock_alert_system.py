stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Display products that are out of stock
out_of_stock = stock.count(0)

# 2. Display products that need restocking (quantity less than 10)
restock_required = [item for item in stock if item < 10]

# 3. Count available products
available_products = len([item for item in stock if item > 0])

# 4. Create a new list containing only products with stock >= 15
healthy_stock = [item for item in stock if item >= 15]

print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)
