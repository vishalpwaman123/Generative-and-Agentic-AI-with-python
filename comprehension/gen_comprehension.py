daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(cup for cup in daily_sales if cup > 5)
print("Total cups : ", total_cups)

min_cups = min(cup for cup in daily_sales if cup > 5)
print("Min cups : ",min_cups)