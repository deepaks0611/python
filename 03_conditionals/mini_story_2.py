# A local cafe wants a program that suggests a snak. if coutomer askes for cookies or samosa, it confirms the order. Otherwise, it sys it is not available.

# Task:
# - Take snack input
# - if it's cookies or samosa , confirm the order
# - Else, show unavailability

snack = input("Enter your preferred snack:").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! we'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")