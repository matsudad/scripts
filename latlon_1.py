#! /usr/bin/env python

# Set the inout file name
# (The program must be run from within the directory that contains this data file)

# This program reads in a file containing several columns of data 
# and returns a file with decimal converted value and selected data fields.
# The process is: Read in each line of the example file, split it into 
# separate components, and write certain output to a separate file

# Load regular expression module, used by decimalat()
import re

# Functions must be defined before they used
def decimalat(DegString):
	# This function requires that the re module is loaded
	# Take a string in the format "34 56.78 N" and return decimal degree
	SearchStr = '(\d+) ([\d\.]+) (\w)'
	Result = re.search(SearchStr, DegString)
	
	# Get the captured character groups, as defined by the parenthases
	# in the recular expression, convert the numbers to floats, and
	# assign them to variables with meaningful names
	Degrees = float(Result.group(1))
	Minutes = float(Result.group(2))
	Compass = Result.group(3).upper() #make sure it is capital too
	
	# Calculate the decimal degrees
	DecimalDegree = Degrees + Minutes/60
	
	# If the compass direction indicates the coordinate is South or West,
	# make sign of the coordinate negative
	if Compass == 'S' or 'N':
		DecimalDegree = -DecimalDegree
	return DecimalDegree

# End of function decimalat() definition
 	
# Set input file name
InFileName = "Marrus_claudanielis.txt"

# Derive the output file name from the input file name
OutFileName = 'dec_' + InFileName

# Give the option to write to a file or just print to screen
WriteOutFile = True

# Open the input file for reading
InFile = open(InFileName, 'r')

HeaderLine = 'drive\tdepth\tlatitute\tlontitute\tdate\tcomment'
print HeaderLine

# Open the output file, if desired. Do this outside the loop
if WriteOutFile:
	# Open the outputfile
	OutFile = open(OutFileName, 'w') # You can append instead with 'a'
	OutFile.write(HeaderLine + '\n')
	
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
		
		# Returns a list in this format:
		Dive 	= ElementList[0]
		Date 	= ElementList[1]
		Depth 	= ElementList[4]
		Comment = ElementList[5]
		
		LatDegrees = decimalat(ElementList[2])
		LonDegrees = decimalat(ElementList[3])
		
		# Create string to 5 decimal places, padded to 10 total characters
		# using line continuation character \
		OutString = "%s\t%4s\t%10.5f\t%10.5f\t%9s\t%s" % (Dive, Depth, LatDegrees, LonDegrees, Date, Comment)
		
		#can still print to the screen then write to a file
		print OutString
		if WriteOutFile:
			OutFile.write(OutString + '\n') #remember the line feed!
	
		
	# Index the counter used to keep track of line numbers
	LineNumber = LineNumber +1
	
# After the loop is completed, close the file
InFile.close()

if WriteOutFile:
	OutFile.close()
	

