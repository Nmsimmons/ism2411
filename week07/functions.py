#1. The first bug I spotted was the missing colon after the for sale in sales statement. I noticed it by running the code and seeing the error indicator. This tells me i can catch simple errors by running the code instead of using AI.
#2. apply_discount(price, tier) takes a price and a discount tier as inputs. It uses the tier to determine what discount should be applied to price and then returns price after the discount. A colleague could use this without reading the body function as long as the function is named clearly. 
#3. I used AI to help with number 5 and see what neededto be fxed. Since thecode worked i was confused. It deepened my undertsanding on what needed to be fixed.  

# Exercise 1

# Defining the function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold'): ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")


# Exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale    # Change to total += sale, this adds each sale to the total instead of replacing it each time. 
print(f"Total: ${total}")

count = 0
for sale in sales: # There is a missing colon here
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):     # Use < only because the last valid index is one less than the length of the list.
    print(sales[i])
    i += 1



# Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)
