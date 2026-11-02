# Self-Assessment
# 1. First you get a a syntax error which tells you it is expection ":" and the you have to ad a "+" which ai     # explained to me. After the first one I caught the missing semi colon and the extra "="
# 2. apply_discount(price, tier) takes a price and a tier string
#    ("gold", "silver", "bronze", or anything else). It returns
#    the price after the matching discount (15%, 10%, 5%, or 0%).
#    Yes, a colleague could use it without reading the body.
# 3. Ai was use in exercise 5 and it shortcutted the process of me figuring out the problem but it ended up giving # me a deeper understanding and the ability to recognize it at later times.
# why is the total $90 instead of $715


# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")
print()

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")
print()

# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

print(f"After gold discount: ${apply_discount(200, 'gold'):.2f}")
print(f"After tax: ${final_price(200, 'gold', 0.07):.2f}")
print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")
print()

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
print()

# --- Exercise 5 ---
# Fixed version of broken_sales.py

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale          # was: total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:         # was missing colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):      # was: i <= len(sales) (caused IndexError)
    print(sales[i])
    i += 1

# --- Exercise 6 ---
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # prints 100 (global x is unchanged)
print(double_it()) # prints 1998 (uses the local x)
print(x)           # still prints 100 (global x was never modified)

# Scope comment:
# The x inside double_it() is a local variable. It does not
# affect the global x, so the outer x stays 100 the whole time.
