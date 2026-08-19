# ==========================================
# TASK 6: DICTIONARY
# ==========================================


# ------------------------------------------
# 1. Friends' Names and Name Length
# ------------------------------------------

friends = [
    "Rahul",
    "Aditya",
    "Priya",
    "Arjun",
    "Sneha"
]

name_length = []

for friend in friends:
    name_length.append((friend, len(friend)))

print("Friends and their name lengths:")
print(name_length)


# ------------------------------------------
# 2. Trip Expenses
# ------------------------------------------

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}


# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expenses:", your_total)
print("Partner's total expenses:", partner_total)


# Determine who spent more
if your_total > partner_total:
    print("You spent more money.")

elif partner_total > your_total:
    print("Your partner spent more money.")

else:
    print("Both spent the same amount.")


# Find category with biggest difference
max_difference = 0
difference_category = ""

for category in your_expenses:

    difference = abs(
        your_expenses[category] - partner_expenses[category]
    )

    if difference > max_difference:
        max_difference = difference
        difference_category = category


print("Category with the biggest difference:", difference_category)
print("Difference:", max_difference)