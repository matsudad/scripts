#! /usr/bin/env python

# Set the inout file name
# (The program must be run from within the directory that contains this data file)
InFileName = "Marrus_claudanielis.txt"

# Open the input file for reading
InFile = open(InFileName, 'r')

# Initialize the counter used to keep track of line numbers
LineNumber = 0

# Loop through each line in the file 
for Line in InFile:
	if LineNumber > 0:
	
		# Remove the line-ending characters
		Line = Line.strip('\n').strip('\r')
		
		# Separate the line number in a list of its tab-delimited components
		# This method takes a string and splits it according to a delimitter, thereby 
		# producing a list of strings
		ElementList = Line.split('\t')
		
		# Print the line
		print LineNumber, ':', ElementList
		print "Depth: %s\tLat: %s\tLon: %s" % (ElementList[4], ElementList[2], ElementList[3])
	
	# Index the counter used to keep track of line numbers
	LineNumber = LineNumber +1
	
# After the loop is completed, close the file
InFile.close()
