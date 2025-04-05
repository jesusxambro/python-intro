car_inventory = ["bmw", "subaru", "gm", "gm"]
#del

del car_inventory[-1]

print(car_inventory)

sales = [3,4,12,3,20]
amount_of_sales_per_weekday = [7000, 9000, 15000, 4000, 24000]

#Matress store sales example
total_week_sales = sum(sales)
total_weekly_sales_amount = sum(amount_of_sales_per_weekday)
average_weekly_sales = total_weekly_sales_amount/total_week_sales
print(f"Average weekly sales was: ${average_weekly_sales}")

max_sales_day = max(sales)
#If we have the max sales, how do we get the day of the week from M-F?
index_of_max_sales = sales.index(max_sales_day)
monday_friday = ["Mon", "Tue", "Wed", "Thu", "Fri" ]

most_sales_on_weekday = monday_friday[index_of_max_sales]

print(f"The most sales was on {most_sales_on_weekday}")