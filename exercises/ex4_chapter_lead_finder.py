# Import the csv library
import csv
# Open the 'llc-chapters.csv' file
# Convert it to a csv_data structure
# Loop through each of the rows
for row in csv.DictReader(open('./llc-chapters.csv')):
    # Compare the 'City' in the row with your city
    # Print "Thank you [[Chapter Lead(s)]]!"
    if row['City'] == "Nanaimo":print("Thanks to "+row['Chapter Lead(s)'])



"""
import csv

# Open the 'llc-chapters.csv' file
with open('./llc-chapters.csv') as csv_file:
    # Convert it to a csv_data structure
    # AND Loop through each of the rows
    for row in csv.DictReader(csv_file):
        # Compare the 'City' in the row with your city
        if row['City'] == "Nanaimo":
            # Print "Thank you [[Chapter Lead(s)]]!"
            print("Thanks to "+row['Chapter Lead(s)'])
"""





"""
import csv

# Open the 'llc-chapters.csv' file
csv_file = open('../exercises/llc-chapters.csv')

# Convert it to a csv_data structure
csv_data = csv.DictReader(csv_file)

# Loop through each of the rows
for row in csv_data:
    # Compare the 'City' in the row with your city
    if (row['City'] == 'Vancouver'):
        # Print "Thank you [[Chapter Lead(s)]]!"
        print("Thank you " + row['Chapter Lead(s)'] + "!")
"""