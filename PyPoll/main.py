import os
import csv

#csv path
csv_path = os.path.join("Resources", "PyPoll_election_data.csv")

# variables
total_votes = 0
candidate_votes = 0
candidate_list = []

#read csv file
with open (csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)

    print("Election Results")
    print("------------------------------")

    previous_row = 0 
    for row in csv_reader:
        total_votes += 1
        candidate = (row[2])
        
        if candidate != candidate_list:
            candidate_list.append(candidate)
            candidate_votes += 1

    print(f"Total Votes: {total_votes}")
    print("------------------------------")

    # for candidate in csv_reader:
        
        
        

    #print(f"{candidate_list} {total_votes}")
        
        #candidate_list.append(names)

        # candidate = str(row[3])
        
    #     if candidate != previous_row:
    #         candidate_list.append(row[3])
    # previous_row = str(row[3])

# def elections(poll_data):
#     candidate = str(poll_data[3])
#     total_candidate_votes = 
#     percentage_votes =

    # print(f"{candidate_list} {total_votes}")

    # print(f"{winner}")