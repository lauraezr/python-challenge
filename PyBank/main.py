import os
import csv

budget_data = os.path.join("Resources", "PyBank_budget_data.csv")

total_profit = 0
months = 0
#DATE = []
row_index_profit = 1
total_change = 0
changes = []


with open(budget_data, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    
    print("Financial Analysis")
    print("------------------------------")

    previous_row = 0
    change = 0
    

    for row in csv_reader:
        total_profit += int(row[1])
        months += 1
        #date = [str(row[0])]
        # changes2 =[(row[0])]
        # final_changes = [changes, changes2]

        if months > 1:
            change = int(row[1]) - previous_row
            #date += 1
            #changes2 = next()
            changes.append(change)
            #changes2.append(date)
            max_profit = max(changes)
            min_profit = min(changes)
            total_change += change
            # if changes == max_profit:
            #     print(f"Greatest Increase in Profits: {row[0]} (${row[1]})")
        
        previous_row = int(row[1])

    print(f"Total Months: {months}")
    print(f"Total: $ {total_profit}")
    print(f"Average Changes: {total_change/(months-1)}")
    print(f"Greatest Increase in Profits: {months} (${max_profit})")
    print(f"Greatest Decrease in Profits: {months} (${min_profit})")