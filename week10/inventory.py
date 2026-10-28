# Reflection 1: The most suprising thing about lists in python is how easy it is to chage, add and remove items without having to create a new list. I didnt realize how many built in functions Python has for lists.
# Reflection 2: In an accounting class, a Python list could save time when working with sales data. Instead of manually calculating totals and averages in Excel, I could use pyhton to quickly calculate them for a large amount of data. 

# Exercise 1: build a list
print(" --- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice 

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) #always grabs first item
print(inventory[-1]) #always grabs last item

middle = len(inventory) // 2
print(inventory[middle]) #grabs middle item

# Exercise 3: List Slicing

print("--- Exercise 3: List Slicing ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Exercise 4: List Methods
print("--- Exercise 4: List Methods ---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5: Tuple Comparison
print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)


try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")


# Exercise 6: 
print("--- Exercise 6: List Average Sales---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

# Exercise 7: 
print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

# Exercise 8:
print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")

