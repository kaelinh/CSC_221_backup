##removeCsvHeader.py - Removes header from CSV files in pwd.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in pwd
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    ##Read the CSV file in (skipping 1st row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip 1st row
        csvRows.append(row)
    csvFileObj.close()

    ##Write out file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
