device_status = input("Enter your device status (active/inactive) : ").lower()

if device_status == "active":
    temperature = float(input("Enter your room temperature : "))
    if temperature > 35:
        print("high temperature alert!")
    else:
        print("temperature is normal")
else:
    print("Device is offline")