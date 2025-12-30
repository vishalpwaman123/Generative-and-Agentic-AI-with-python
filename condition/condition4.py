seat_type = input("Enter seat type (sleeper/AC/general/luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("general - cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seat with meals")
    case _:
        print("Invalid Seat type")