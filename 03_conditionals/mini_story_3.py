# A tea stall offers different cup sizes.
# write a program that calculates the price based on size.

# Task:
# Input: "small","medium","large"
# Small -> $ 10, medium -> $ 15, large -> $20
# If invalid:show "Unknown cup size"

cup = input("Choose you cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees ")
else:
    print("Unknown cup size")