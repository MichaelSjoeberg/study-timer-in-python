# timer for recording study times to a txt-file.

from timeit import default_timer
from pylab import *
import time

###### FUNCTIONS ######

def stopTimer(s,t):
	"take snapshot of system time when entering 'stop' in terminal"

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

def query():
	"ask user for input"

	print "\n\n------------------- Study Timer -------------------\n" + "Subjects:\n"

	n = 1
	for s in subject_dict:
		print "\t" + str(n) + ". " + subject_dict[str(n)] + "\n"
		n = n + 1
	print "---------------- By Michael Sjoeberg ----------------\n"

	subject = raw_input("What are we studying today (press ENTER for Diagram)?\n\n" + ">\t")

	checkQuery(subject)

def checkQuery(s):
	"check user input"

	# show diagram when empty input
	if s == '':
		createDiagram()

	elif int(s) > 0 and int(s) < 8:
		check = raw_input("\nYou're studying " + subject_dict[str(s)] + "." + " Is that correct? (Y/N)" + ">\t")
		if check == "Y" or check == "y":
			start = default_timer()
			print "\nOK! Good luck!"
			stopTimer(s,start)
		if check == "N" or check == "n":
			print "Let's try again..."
			query()
		else:
			"Please enter Y or N."
			checkQuery(s)

	return

def createDiagram():
	"collect data and create a diagram"

	total_time = 0

	# empty dictionary
	data_dict = {}

	for s in subject_dict:

		# initialise total for key
		data_dict[s] = 0

		# open txt-file
		timer_file = open(time.strftime("%B:%Y") + ".txt", "r")

		# split lines into sections
		for line in timer_file:

			# find and add math times
			if line.startswith(subject_dict[str(s)]):
				section = line.split(":")
				t = section[1]
				t = t[:-2]
				
				# add to total
				data_dict[s] = float(data_dict[s]) + float(t)
				total_time = total_time + float(t)

	# make a square figure and axes
	figure(1, figsize=(10,8))
	ax = axes([0.1, 0.1, 0.8, 0.8])
	ax.set_aspect('equal')

	# The slices will be ordered and plotted counter-clockwise.
	labels = ()
	fracs = ()

	for s in data_dict:
		if data_dict[str(s)] == 0:
			continue
		else:
			labels = labels + (subject_dict[str(s)],)
			fracs = fracs + (data_dict[str(s)] / total_time,)

	# colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
	# explode = (0, 0, 0, 0, 0, 0, 0)

	pie(fracs, labels=labels,
	                autopct='%1.1f%%', shadow=False, startangle=90)
	                # The default startangle is 0, which would start
	                # the Frogs slice on the x-axis.  With startangle=90,
	                # everything is rotated counter-clockwise by 90 degrees,
	                # so the plotting starts on the positive y-axis.

	title('Study time distribution', bbox={'facecolor':'1', 'pad':28})
	show()
	query()

##### END FUNCTIONS #####

subject_dict = {
	'1': 'Mathematics',
	'2': 'Programming (Python)',
	'3': 'Programming (Java)',
	'4': 'Programming (Other)',
	'5': 'Web Development',
	'6': 'Finance (MS Excel)',
	'7': 'Finance (General)'}

query()
