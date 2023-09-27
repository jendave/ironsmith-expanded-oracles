#!/usr/bin/env python

import json

original_data_file="ironsmith-expanded-oracles.json"
# output_data_file="ironsmith-expanded-oracles.txt"
table = ["(1 - 2)", "(3 - 4)", "(5 - 6)"]

# reading `JSON file`
with open(original_data_file,"r") as file:
   ironsmith_oracles = json.load(file)

# Updating JSON Data
print("Ironsmith Expanded Oracles\n")

for oracle in ironsmith_oracles['Oracles']:
    oracle_name = (oracle['Name'])
    die = (oracle['d'])
    if die == "200":
        table_num = 0
        print("d100 "+ oracle_name + " " + table[table_num])
        range_upper = None
        print_title = True
        for result in oracle['Oracle Table']:
            if range_upper is None:
                range_upper = 0
            if range_upper >= 100 and range_upper <= 200:
                table_num = 1
                if print_title:
                    print("\nd100 "+ oracle_name + " " + table[table_num])
                    print_title = False
                range_lower = range_upper + 1 
                range_upper = result['Chance']
                description = result['Description']
                print(str(range_lower - 100) + "-" + str(range_upper - 100) + " " + description)
            else:
                range_lower = range_upper + 1
                range_upper = result['Chance']
                description = result['Description']
                print(str(range_lower) + "-" + str(range_upper) + " " + description)
    elif die == "300":
        table_num = 0
        print("d100 "+ oracle_name + " " + table[table_num])
        range_upper = None
        for result in oracle['Oracle Table']:
            if range_upper is None:
                range_upper = 0
            range_lower = range_upper + 1
            range_upper = result['Chance']
            description = result['Description']
            print(str(range_lower) + "-" + str(range_upper) + " " + description)
    else:
        print("d" + die + " " + oracle_name)

        range_upper = None
        for result in oracle['Oracle Table']:
            if range_upper is None:
                range_upper = 0
            range_lower = range_upper + 1
            range_upper = result['Chance']
            description = result['Description']
            print(str(range_lower) + "-" + str(range_upper) + " " + description)
    print()

# Saving updated data into a new file
# with open(output_data_file,"w") as file:

