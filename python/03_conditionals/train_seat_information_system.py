# You are building a ticket info system for a railway app.
# Based on seat type, show its features.

# Task:
#  - Input: "sleeper", "AC","General","Luxury"
#  - Match using match-case
#  - Unknown -> show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper/Ac/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - no AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")