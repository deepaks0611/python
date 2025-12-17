# You're preparing an order summary with customer names and their total bill.

# Task:
#  - Use two lists:one for names and one for bills.
#  - Print: "[Name] paid $[amount]"

names = ["Deepak","Adarsh","Ankit","Priyanshu"]
bills = [50, 60, 100, 66]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
