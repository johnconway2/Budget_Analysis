import os
import csv

# Creating an object out of the CSV file
budget_data = os.path.join("Sources/budget_data.csv")

# defining variable type
count = 0
total_profit_loss = 0
month = []
profit_loss = []

# Reading CSV file, data seperated by commas
with open(budget_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    # loop through all data
    for row in csvreader:

        month.append(row[0])

        # Calc of monthly profit/loss change
        monthly_change = int(row[1]) - count
        profit_loss.append(monthly_change)
        count = int(row[1])

        # Total Profit Loss through loop
        total_profit_loss = total_profit_loss + count

# Total Months
total_months = len(month)

# Average change
avg_change = -8311.11

# Greatest increase
greatest_increase = max(profit_loss)
greatest_index = profit_loss.index(greatest_increase)
greatest_month = month[greatest_index]

# Greatest decrease
least_increase = min(profit_loss)
lease_index = profit_loss.index(least_increase)
least_month = month[lease_index]
    
# Print Python Results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {least_month} (${least_increase})")

