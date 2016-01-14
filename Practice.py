# Python Pracrice from https://docs.python.org/3/tutorial/index.html
# 3rd Decemeber 2015

from sys import argv
import math

# to-do:
	# LISTS - how to define a list/add items/remove items/how to access individual items/acces range of items .
		# lists are defined via [=] . 
		# to add an item to the end of a list, you use <list.name>.append() .
		# access items via <list.name>[a] .
		# Change items via <list.name>[a] = [z] .
		# access a range of items via <list.name>[a:z] .
		# change a range of items via <list.name>[a:z] = [A:Z] .
		# to assess the length of a list, use the function, len() .
		# nest lists by creating a list of already existing lists, i.e.:
a = 'a','b','c'
b = 1,2,3
c = a,b
		
		# accessing nestred loops is a bit different, for example:
c [0]		# gives ['a','b','c']
c [0][0]	# gives ['a']
			
		# when accessing a list, you can index from the end of the list using [-1]. this will give you the last character. you can slice a list from the end using [-3:]. this will give you the last three characters .
		
			
	# lOOPS - write a loop that goes through integers 1 to 10 and prints the square value for each .
		# loops can have different function, for() runs loops for the given qualities in a previously (or currently) defined object:
values = range(0,10)

for x in range(1,10):
	values[x] = x*x
	 		
		# while() runs loops given the initial condition is true, i.e. while(b<10) . 
		
for x in range(1,10):
	output = x*x
	output < 50
	while True:
		print output   # doesnt seem to work..... ASK HANNES
	
		# body of loop is indented, or Python wont recognise it .
	
	
	# OPENING FILES - open small text file and read line by line using a for loop. Open a new file connection and write the previously defined square values into it. 
	
	
file = open(C:\Users\kingjoethomas\Desktop\Test.txt','r+')
	
		# to read this file line by line, you use file.readline()
		# the text prior to the .read function is the name of the file, which in this case, is file.
		# to read all at once, you can use file.readlines() or use a loop function:
	
for line in file:
	print line
		
		# this prints all of the lines in the file, and removes them from the original document.
	
sqvals = range(0,10)	# define a character string of 10 integers.
for x in range(1,11):
	sqvals[x-1] = x*x	# use a for loop to iterate the square values of 1 to 10.
	
		# then write these values into the Test.txt file on the desktop.
		
for x in range(1,11):
	values[-1] = x*x
	data = str(values)   # < things must be in string format when writing to a text file.

f.tell()

	# this shows the position of focus within a file, as an integer representing the number of bytes from the beginning of the file.
	# this position can be changed using the f.seek() function, and then subsequently printed using f.read(x). the x is to be replaced by the number of characters you want to print from that position. For example, f.seek(5) will take you to the fifth byte within that file. f.read(2) will display the character at byte 5, as well as the character at byte 6.
	# the arguments for the f.seek() function are (offset,from_what).
	# offset is the number of bytes to be offset from the reference point, from_what. From_what is at default, 0, meaning the beginning of the file. it may also be 1 (the current position), or 2 (the end of the file). e.g.:
	
f.seek(-3,2) # finds the third byte prior to the end of the file.
	
f.read(1) # prints only the 3rd byte prior to the end of the file.
	
f.close() # closes the file when you are finished with it.
	
		# its good practice to use the 'with' keyword when dealing eith file obects. 'With' makes it easier to execute certain contextual commands.
	
with open(C:\Users\kingjoethomas\Desktop\Test.txt','r+') as f:
	read_data = f.readlines()
		
		# this opens the file, and reads all lines into the object read_data as a list, with line breaks '\n'.
		# to remove these line breaks use the following <filename>.replace() function:
	
read_data = read_data.replace('\n','')


# READING A FILE LINE BY LINE
the_file = open('C:\Users\kingjoethomas\Desktop\Test.txt','r')
the_file.readline()	# use this repetedly to display the next line.

# writing a function to store each line in its own object.
# need a loop that checks the length of the line, then stores that entire line into an object, then iterates onto the next line and continues to repeat. 

length = sum(1 for _ in the_file)
line = range(length)
the_file.seek(0)
for x in range(0, len(line)):
	line[x] = the_file.readline()
	
	





