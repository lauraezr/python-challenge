#import modules
import os
import csv

# csv path
budget_data = os.path.join("Resources", "PyBank_budget_data.csv")

#variables
total_profit = 0
total_date = 0
counter = 0

row_index_profit = 1
total_change = 0
changes = []

#read csv file
with open(budget_data, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #csv file has a header row, skip
    csv_header = next(csv_file)

    #loop variables
    previous_row = 0
    change = 0
    
    
    #loop through each row to add profits/changes
    for row in csv_reader:
        
        total_profit += int(row[1])
        total_date = total_date + 1
        counter += 1
        profit = int(row[1])
        date = row[0]

        if counter > 1:
            change = int(row[1]) - previous_row
            
            changes.append(change)
        
            max_profit = max(changes)
            min_profit = min(changes)
            
            total_change += change

        previous_row = int(row[1])

output_path = os.path.join("Analysis", "Analysis.txt")       
with open(output_path, 'w') as txt_file:

    csvwriter = csv.writer(txt_file)
    
    csvwriter.writerow([(
        "Financial Analysis\n"
        "--------------------------------\n"
        f"Total Months: {counter}\n"
        f"Total: $ {total_profit}\n"
        f"Average Changes: {total_change/(counter-1)}\n"
        f"Greatest Increase in Profits: {date} (${max_profit})\n"
        f"Greatest Decrease in Profits: {date} (${min_profit})\n"
    )])


    #print out statements
    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {counter}")
    print(f"Total: $ {total_profit}")
    print(f"Average Changes: {total_change/(counter-1)}")
    print(f"Greatest Increase in Profits: {date} (${max_profit})")
    print(f"Greatest Decrease in Profits: {date} (${min_profit})")
