import os
import sys
import csv

# code to analyse the budget data
budget_data = os.path.join(".", "budget_data.csv")
financial_analysis = os.path.join(".", "financial_analysis.txt")

with open (budget_data, "r", newline="") as filehandle:
    # skip first line
    next(filehandle)
    # read in with csv reader
    csvreader = csv.reader(filehandle)
    
    # loop through all lines of the csv reader
    total_months = 0 # count total number of months
    total_net_amount = 0 # count total profit/losses
    monthly_changes = 0 # the change month to month
    prev_month_amount = 0 # amount of the previous month
    current_month_amount = 0 # amount of the current month
    diff_current_prev = 0  # difference between two months
    greatest_increase = 0 # greatest increase month by month
    greatest_decrease = 0 # greatest decrease month by month
    current_month = ""
    greatest_increase_month = ""
    greatest_decrease_month = ""
    for row in csvreader:
        total_months += 1
        current_month = row[0]
        current_month_amount = float(row[1])
        total_net_amount += current_month_amount
        diff_current_prev = current_month_amount - prev_month_amount
        # skip first line because there's no change
        if (csvreader.line_num != 1):
            monthly_changes += diff_current_prev
        if (diff_current_prev > greatest_increase):
            greatest_increase = diff_current_prev
            greatest_increase_month = current_month
        if (diff_current_prev < greatest_decrease):
            greatest_decrease = diff_current_prev
            greatest_decrease_month = current_month
        # at the end of the line, update previous month amount for next loop
        prev_month_amount = current_month_amount
    
#loop finished, time to calculate average change
average_change = monthly_changes/(total_months-1)
#print to file
with open(financial_analysis, "w+") as filehandle:
    filehandle.write("Finalcial Analysis\n")
    filehandle.write("-" *32 + "\n")
    filehandle.write(f"Total Months: {total_months: .0f}\n")
    filehandle.write(f"Total: ${total_net_amount: .0f}\n")
    filehandle.write(f"Average Change: ${average_change: .2f}\n")
    filehandle.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase: .0f})\n")
    filehandle.write(f"Greatest Decreast in Profits: {greatest_decrease_month} (${greatest_decrease: .0f})\n")
    
# print to screen
with open(financial_analysis, "r") as filehandle:
    print(filehandle.read())
