import csv
import os
myfile = open("merged_csvs.csv", "a" )
writer = csv.writer(myfile)
counter = 0
for file in os.listdir(" "): # path to csv folder goes here
	counter += 1
	if file.endswith(".csv"):
		print(counter , file)
		with open(file, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if (row):
					writer.writerow(row)
			f.close()
myfile.close()
