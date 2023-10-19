#STUDENT ID: 22038205
#Import Python Libraries
import csv
import datetime
import pytz

#import function to read the CSV file
from csv import reader
from dateutil.parser import parse
filename='crop.csv'
cleanedCSV_filename='clean.csv'

#initialise count to zero
line_count = 0
# open the cropped csv file
with open(filename,'r') as my_file:
    #pass the file object to reader
    file_reader = reader(my_file)
    head = next(file_reader)
    # check if the file is empty or not
    if head is not None:
        # Iterate over each row
        for i in file_reader:
            read_data = (i[0]).split(';')
            #read data in Site Id 
            siteId = read_data[4]
            #Find length of string
            lengthOfSiteID = len(siteId)    
            #read data in Location
            location = read_data[17]   
            
            line_count += 1
            line_count_string = str(line_count)
            #If site id is not empty
            if lengthOfSiteID != 0:
                #create an list array to store the site ids
                array_siteId = ['188', '203', '206', '209', '213', '215', '228', '270', '271', '375', '395', '452', '447', '459', '463', '481', '500', '501', '672']

                #create an list array to store locations
                array_location = ['AURN Bristol Centre', 'Brislington Depot', 'Rupert Street', 'IKEA M32', 'Old Market', 'Parson Street School', 'Temple Meads Station', 'Wells Road', 'Trailer Portway P&R',
                 'Newfoundland Road Police Station', "Shiner's Garage", 'AURN St Pauls', 'Bath Road', 'Cheltenham Road \ Station Road', 'Fishponds Road', 'CREATE Centre Roof', 'Temple Way', 'Colston Avenue', 'Marlborough Street']

                if siteId in array_siteId:
                    #get index of the retrieved site Id from the array
                    siteId_index = array_siteId.index(siteId)

                    #Use the retrieved nde to get the element from the array_location array
                    retrieved_array_location =   array_location[siteId_index]  
        
                    #if location is a string and Site id is an integer
                    if retrieved_array_location ==  location:
                        #Create a file
                        file1 = open(cleanedCSV_filename, "a")
                        # writing newline character
                        file1.write("\n")
                        file1.write(i[0]) 

                    else:
                        #message1 = "Site id is not empty but there is a mismatch on line " + line_count_string + " Site id:" + siteId + " Location:" + location
                        print("Site id is not empty but there is a mismatch on line ",line_count_string)  
                        print("Site ID:",siteId ) 
                        print("Location:",location) 
            else:
                #message2 = "Site Id is empty on line " + line_count_string
                print("Site Id is empty on line " + line_count_string) 
