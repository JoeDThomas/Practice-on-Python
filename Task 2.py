# Script to compare two files line by line and output the score into a new .txt file

#open file_a
file_a = open('C:/Users/kingjoethomas/Desktop/Research Project/Practice from Hannes/file_a.txt','r')

#open file_b
file_b = open('C:/Users/kingjoethomas/Desktop/Research Project/Practice from Hannes/file_b.txt','r')

#open the output file
output = open('C:/Users/kingjoethomas/Desktop/Research Project/Practice from Hannes/output.txt','w')

# going to use the readlines() function to apply all lines from file_a into a list.

list_file_a = range(sum(1 for _ in file_a))
file_a.seek(0)
list_file_a = file_a.readlines()

# This worked, but the list consists of strings. have to turn them all into floats.

float_file_a = range(len(list_file_a))

for x in range(len(list_file_a)):
	float_file_a[x] = float(list_file_a[x])
	
# float_file_a now contains the float of each line from file_a. Now to do the same with file_b.

list_file_b = range(sum(1 for _ in file_b))
file_b.seek(0)
list_file_b = file_b.readlines()
float_file_b = range(len(list_file_b))
for x in range(len(list_file_b)):
	float_file_b[x] = float(list_file_b[x])
	
# now both files are stored as floats in their own list.
# next step is to compare both lists line by line and output a 1 when file_a's value is greater than the corresponding line from file_b.

		
# for x in range(sum(1 for _ in file_a)):
#	if float_file_a[x] > float_file_b[x]:
#		output.write('1\n')
#	elif float_file_a[x] < float_file_b[x]:
#		output.write('-1\n')
#	else:
#		output.write('0\n')
		
# that didnt work..
# gunna try another loop method because the write() function works outside of the loop:

final_txt = open('C:/Users/kingjoethomas/Desktop/output file.txt','w')

for line in range(len(float_file_a)):
		if float_file_a[line] > float_file_b[line]:
			final_txt.write('1\n')
		elif float_file_a[line] < float_file_b[line]:
			final_txt.write('-1\n')
		else:
			final_txt.write('0\n')
			
final_txt.close()
file_a.close()
file_b.close()