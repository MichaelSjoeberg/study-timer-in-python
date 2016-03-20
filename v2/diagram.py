# import dependencies
import sys, traceback
from timeit import default_timer
import time
from pylab import *

# function for creating diagram
def createDiagram(subject_dict):
	"Collect data from file and create a diagram."

	total_time = 0

	# empty dictionary
	data_dict = {}

	for s in subject_dict:

		# initialise total for key
		data_dict[s] = 0

		# open txt-file based on time, requires time plugins
		timer_file = open(time.strftime("%B:%Y") + ".txt", "r")

		# open demo txt-file
		# timer_file = open("demo" + ".txt", "r")

		# split lines into sections
		for line in timer_file:

			# find and add math times
			if subject_dict[str(s)] in line:
				section = line.split(":")
				t = section[1]
				t = t[:-2]
				
				# add to total
				data_dict[s] = float(data_dict[s]) + float(t)
				total_time = total_time + float(t)

		timer_file.close()

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

	colors = ['yellowgreen', 'lightskyblue', 'lightcoral', 'aliceblue', 'seagreen', 'turquoise' ,'papayawhip', 'saddlebrown', 'powderblue', 'plum']
	# explode = (0, 0, 0, 0, 0, 0, 0)

	pie(fracs, labels=labels, colors=colors,
	                autopct='%1.1f%%', shadow=False, startangle=90)
	                # The default startangle is 0, which would start
	                # the Frogs slice on the x-axis.  With startangle=90,
	                # everything is rotated counter-clockwise by 90 degrees,
	                # so the plotting starts on the positive y-axis.

	title("Study timer for " + time.strftime("%B %Y"), bbox={'facecolor':'1', 'pad':28})
	show()

	return