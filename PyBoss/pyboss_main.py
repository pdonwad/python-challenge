#import packages
import os
import csv
#import operator
#import collections
import datetime
abbreState=""
#importing directory for state abbreviations

from us_state_abbreviations import us_state_abbrev
try:
	fileName=input("Enter the csv File Name::")
	#set path for  csv file
	filePath=os.path.join("raw_data",fileName)
	newFile,ext=fileName.split(".")
	#set file path for write
	fileWritePath=os.path.join("raw_data",newFile+"_modified.csv")
	#open file in write mode
	csvfile= open(fileWritePath, 'w', newline='') 
	#creating writer object
	csvWriter = csv.writer(csvfile, delimiter=',')
	#set header for csv
	csvWriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
	with open(filePath) as fileOpen:
		#read file
		readFile1=csv.reader(fileOpen,delimiter=',')
		#get  header values
		header=next(readFile1)
		#get no of columns
		noofColumns=len(header)
		#iterate through all rows
		for row in readFile1:
			#iterate 
			for x in range(0,noofColumns):
				#split name  for Name column
				if header[x]=="Name":		
					first_name,last_name=row[x].split(' ')
				#change format of DOB to mm/dd/yyyy
				elif header[x]=="DOB":
					readDate=datetime.datetime.strptime(row[x], '%Y-%m-%d')
					convertedDate=datetime.date.strftime(readDate, "%m/%d/%Y")
				#mask ssn
				elif header[x]=="SSN":
					firstSSN,middleSSN,lastSSN=row[i].split('-')
					maskedSSN="*"*len(firstSSN)+"-"+"*"*len(middleSSN)+"-"+lastSSN
				#get abbreviations of STATE
				elif header[x]=="State":
					abbreState=us_state_abbrev[row[i]]
				elif header[x]=="Emp ID":
					empID=row[x]
			#write the rows to csv file
			csvWriter.writerow([empID,first_name,last_name,convertedDate,maskedSSN,abbreState])

	#close file
	print("Data written to "+newFile+"_modified.csv Successfully")
	csvfile.close()
except IOError:
		print("Error: Sorry "+fileName+ "  Not Found! ")



