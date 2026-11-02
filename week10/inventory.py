# Reflection 1: I didn't expect list methods like append(), remove(), and sort() to change the same list in place.
# That means later code sees the updated inventory without needing to create another list.
#
# Reflection 2: In a class inventory exercise, I could keep product names and quantities in lists and filter for items
# below their reorder points. That would produce a reorder list quickly instead of sorting and filtering a spreadsheet by hand.

print("Exercise 1: Build the list")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("\nExercise 2: Index practice")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

print("\nExercise 3: Slicing")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("\nExercise 4: Modify")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("\nExercise 5: Tuple comparison")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples are immutable, so they help keep coordinate values from being changed accidentally.")
print(coords)

print("\nExercise 6: Average of a list of sales")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total} | Count: {count} | Average: {average}")
print(f"Best: {max(sales)} | Worst: {min(sales)}")

print("\nExercise 7: Accumulator pattern")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print("Original prices:", prices)
print("Discounted prices:", discounted)

print("\nExercise 8: Filter above threshold")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day_sales in sales:
    if day_sales > 300:
        high_sales.append(day_sales)
high_sales_count = len(high_sales)
high_sales_average = sum(high_sales) / high_sales_count
print(high_sales)
print(f"Count: {high_sales_count} | Average: {high_sales_average:.2f}")
