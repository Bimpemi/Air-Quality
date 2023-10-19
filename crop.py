#STUDENT ID:22038205
# Import Python libraries
import csv
import datetime
import pytz

#import function to read the CSV file
from csv import reader
#import parse from library function dateutil for changing thge string date format 
from dateutil.parser import parse
from datetime import datetime

# Assign the CSV file 
filename='air-quality-data-continuous.csv'
#create the csv file
cropped_filename='crop.csv'

#Use pytz library to create a UTC- Coordinated Universal Time Zone
utc = pytz.UTC

# open file the csv file air-quality-data-continuous.csv
with open(filename,'r') as my_file:
    #pass the file object to reader()
    file_reader = reader(my_file)
    head = next(file_reader)
    # check if the file is empty or not
    if head is not None:
        #Parse the string to datetime
        dateToCompare = parse('00:00 1 Jan 2010')
        #Convert the date given to compare to timezone aware format
        compareWith = dateToCompare.replace(tzinfo=utc)
        
        # Iterate over each row
        for i in file_reader:
            #read the data starting from the first column seperated by delimiter ';'
            rowData = (i[0]).split(';')

            #check if the dateime column is not empty or start with delimiter ';'
            if rowData[0] != ";" and  rowData[0] != "":
                readDate = parse(rowData[0])
                if readDate >= compareWith:
                    print(i[0]) 
                    #write the output into the cropped csv file
                    cropped_csv= open(cropped_filename, "a")
                    #writing newline character
                    cropped_csv.write("\n")
                    cropped_csv.write(i[0])
         