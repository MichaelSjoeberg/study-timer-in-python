# import dependencies
import sys, traceback
from timeit import default_timer
import time

# import config
from config import *

# import function for diagram
import diagram

subject_dict = {
		'1'	: 'Mathematics',
		'2'	: 'Programming (Python)',
		'3'	: 'Programming (Java)',
		'4'	: 'Programming (Other)',
		'5'	: 'Web Development',
		'6'	: 'Finance (MS Excel)',
		'7'	: 'Finance (General)',
		'8'	: 'Languages (German)',
		'9'	: 'Languages (Norwegian)', 
		'10': 'Languages (Other)'}

# function for stopping and recording time
def stopTimer(s,t):
	"Take a snapshot of system time and write total time to file."

	stop = raw_input("\nEnter 'stop' to stop timer.\n\n" + ">\t")

	if stop == "stop" or stop == "Stop" or stop == "STOP":
	    duration = default_timer() - t

	    # create new txt-file and store the data
	    file = open(time.strftime("%B:%Y") + ".txt", "a")
	    file.write(subject_dict[s] + ": " + str(duration / 60) + "\n")
	    file.close()

	    print "\nGood job! You studied " + subject_dict[s] + " for a total of " + str(int(duration / 60)) + " minutes."

	again = raw_input("\nPress ENTER to continue.\n\n" + ">\t")
	if again == "" or len(again) > 0:
		query()

# function for displaying subjects and getting input 
def query():
	"Display subjects and ask user for input, then validate input."

	try:
		print "\n\n------------------- Study Timer -------------------\n" + "Subjects:\n"

		# display all subjects in imported subject dictionnary
		n = 1
		for s in subject_dict:
			print "\t" + str(n) + ". " + subject_dict[str(n)] + "\n"
			n = n + 1
		print "---------------- By Michael Sjoeberg ----------------\n"

		subject = raw_input("What are we studying today (press ENTER for Diagram)?\n\n" + ">\t")

		# validate input
		checkQuery(subject)

	except KeyboardInterrupt:
		print "\n\nExiting...  See you!\n"

	except Exception:
		traceback.print_exc(file=sys.stdout)

	sys.exit(0)

# function for validating input from 'query()'
def checkQuery(s):
	"Display diagram if input is blank, start timer if input is correct."

	try:
		# display diagram if input is blank
		if s == '':
			diagram.createDiagram(subject_dict)
			query()

		# validate input and act accordingly
		elif int(s) > 0 and int(s) <= len(subject_dict):
			check = raw_input("\nYou're studying " + subject_dict[str(s)] + "." + " Is that correct? (Y/N)" + ">\t")
			
			# start timer if correct
			if check == "Y" or check == "y":
				start = default_timer()
				print "\nOK! Good luck!"
				stopTimer(s,start)

			# ask for subject again if incorrect
			if check == "N" or check == "n":
				print "Let's try again..."
				query()

			# ask again if none of above
			else:
				"Please enter Y or N."
				checkQuery(s)

	except Exception:
		print "\n\nNot a valid input, please try again.\n"
		query()

# initialise program
query()
