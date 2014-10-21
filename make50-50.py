#This script takes a csv datafile and creates a balanced subset
#of the data based on some binary field.  That means that the
#resultant file will contain the specified number of rows with 0 and 1 for
#that field.  This is a common task in data mining, for example, when
#you want to "stratify" a data set by class.
import random
import sys
file_to_save = "new_data.csv"
filename = "mailing_hw3.csv"
balance_field = 4 # the field to balance the data on; could be different for a different data set

# Take the desired number of rows of each class as an input on the command line.
# If it is not specified, or is too large (there aren't enough of one class), we will just make
# the largest balanced subset possible (see below).
command_line=sys.argv  # get the command-line arguments 
#print command_line

#sys.exit()
file_write = open (file_to_save, "w")
file = open(filename, 'r')

total = file.read().split('\r')
heading = total[0]
data = total[1:]


random.shuffle(data)

# Read in all the records into a record dataset.  Count the numbers of positives and negatives while
#  we're at it.  Also, we're going to save the actual line, so we can print it back out later.  
pos_count = 0
neg_count = 0
records = list()
lines = list()
for line in data:
    # process the csv file "manually" rather than use the csv reader, to show
    # how simple it is.  This code can be reused whenever you need to read in a csv-like file
    line = line.strip()  # strip the newline from the end of each line
    #print line
    record = line.split(',')  # split the line into individual fields
    #print record
    records.append(record) # build up a list of records
    lines.append(line)     # and a corresponding list of the original lines
    # Count the pos and neg records
    if record[balance_field] == '1':
        pos_count += 1
    elif record[balance_field] == '0':
        neg_count += 1
   
print "Num pos: ", pos_count
print "Num neg: ", neg_count
print "Total: ", pos_count + neg_count, len(records)
   
#What will be the maximum balanced file we can create?
total_of_each = min(pos_count, neg_count)  # that many of each class
   
# Now, get the number of each class from the command line
# use total_of_each as default or if the command-line argument is infeasible
if (len(command_line)>=2) and (int(command_line[1])<total_of_each):  #presuming the only command line option is num of each
    total_of_each = int(command_line[1])
   
# Now -- just run through the file and print the first lines of each class until enough are printed.
num_neg=0
num_pos=0
file_write.write(heading+"\n")
print lines[0] # This prints the field names out first
for i in range(len(records)): 
    if records[i][balance_field] == '0':
        num_neg += 1
        if num_neg <= total_of_each:
            #print records[i]
            #print lines[i]
            file_write.write(lines[i]+"\n")
    elif records[i][balance_field]=='1':
        num_pos += 1
        if num_pos <= total_of_each:
            #print records[i]
            file_write.write(lines[i]+"\n")
            #print lines[i]
   
# One could instead print a random set of num_of_each lines instead of the first lines
#  IMO it would be better to write another script that randomizes the file.
#  Then we could run that script and then run this script on the result.  THere would be
#  two benefits.  (1) This script as-is is much simpler.  (2) Randomizing a file is a common
#  task -- why not create a utility script for that.  Then you could use it whenever you want. 
   
file.close()
