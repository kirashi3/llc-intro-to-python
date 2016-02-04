# Import the csv library
import csv
# Create necessary variables
coleadCount = 0
# Open the 'llc-chapters.csv' file
with open('./llc-chapters.csv') as csv_file:
    # Convert it to a csv_data structure
    # Loop through each of the rows
    for row in csv.DictReader(csv_file):
        # Print 'City' of 'Chapter Lead(s)' with ampersands
        # Increase coleadCount for each city hit
        if row['Chapter Lead(s)'].find("&") >= 0:
            print(row['City']+" has co-leads")
            coleadCount += 1
    # Print a blank line and number of co-lead cities
    print("\n"+str(coleadCount)+" cities have co-leads.")
# Check that file is closed
if csv_file.closed:print("\n\nFILE CLOSED FOR THE EVENING\nWE WILL REOPEN TOMMORROW AT 9AM")