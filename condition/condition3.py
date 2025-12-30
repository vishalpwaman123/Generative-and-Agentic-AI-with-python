order_amount = float(input("Enter the order amount : "))
delivery_fees = 0 if order_amount > 300 else 30

# if order_amount > 300:
#     pass
# else:
#     delivery_fees = 30

print(f"delivery fees is : {delivery_fees}")