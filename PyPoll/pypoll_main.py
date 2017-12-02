#pypoll seperate
#import modules
import os
import csv
import operator
import collections
fileName=input("Enter the csv File Name::")
#set path for  csv file
filePath1=os.path.join("raw_data",fileName)
#set winner vote as zero
Winner=0
totalVotes=0
#open first csv file
try:
	with open(filePath1) as fileOpen1:
		#read file
		readFile1=csv.reader(fileOpen1,delimiter=',')
		#skip header
		header1=next(readFile1)
		noOfCol1=len(header1)
		#declare counts dictionary as counter object
		counts = collections.Counter()
		#read each row in file
		for row1 in readFile1:
			for i in range(0,noOfCol1):
				if header1[i]=="Candidate":
					#set count as value for keys in the dictionary
					counts[row1[i]]+=1
					#count total votes
					totalVotes+=1


	#*********Print to Terminal    	
	print("Election Results")		
	print("--------------------------------")
	print("Total Votes: ",totalVotes)

	print("--------------------------------")
	#print contents of dictionary
	for showItems,showKeys in counts.items():
		#calculate the percentage vote
		percentageVote=(showKeys/totalVotes)*100
		print(showItems, " : ","%.1f" %percentageVote,"%  (",showKeys,")")
		#find the winner
		if showKeys>Winner:
			Winner=showKeys
			winnerName=showItems

	print("--------------------------------")
	print("Winner: ",winnerName)
	print("--------------------------------")

#************Print to File
	
	#seperate filename and extension
	newFile,ext=fileName.split(".")
	#create text file based on csv files
	
	fileWritePath=os.path.join("raw_data",newFile+"_Analysis_Report.txt")
	

	#open file in write mode
	fileWriter=open(fileWritePath,"w")
	#Write Contents. \n will write each result on new line.
	fileWriter.write("Election Results\n")
	fileWriter.write("--------------------------------\n")
	fileWriter.writelines("Total Votes: "+str(totalVotes)+"\n")
	fileWriter.write("--------------------------------\n")
	for showItems,showKeys in counts.items():
		percentageVote=(showKeys/totalVotes)*100
		fileWriter.writelines(showItems + " : "+"%.1f" %percentageVote +"%  ("+str(showKeys)+")")
		fileWriter.write("\n")
	fileWriter.write("--------------------------------\n")
	fileWriter.write("Winner: "+winnerName)
	fileWriter.write("\n")
	fileWriter.write("--------------------------------\n")
	#Close File
	fileWriter.close()
except IOError:
		print("Error: Sorry "+fileName+ "  does not exist.")



