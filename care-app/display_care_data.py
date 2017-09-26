import json
from datetime import datetime, timedelta
#Fetching & displaying

#**kwargs will be useful here	

def create_barn():
	with open ('care_data.json') as i:
		data = json.load(i)

	barn = []

	for x in data['horses']:
		barn.append(x)

	return barn

def select_horse(barn):
	for x in barn:
		print str(barn.index(x)) + " - " + x

	selection = int(raw_input("These horses are currently in your barn.  Enter the number next to the name of the \
	horse's data you would like to see."))

	if selection > len(barn)-1:
		print "That wasn't a valid selection"

	print "You selected " + str(barn[selection])
	return selection


def get_history(selection):
	horse = str(barn[selection])

	horse_file = horse + '.json'

	with open (horse_file) as i:
		data = json.load(i)

	shoeing_history = []
	worming_history = []
	
	for x in data['shoes']:
		shoeing_history.append(x)
	
	for y in data['worming']:
		worming_history.append(y)
	
	
	
	print "Shoeing History: " + str(shoeing_history)
	print "Worming History: " + str(worming_history)

barn = create_barn()
selection = select_horse(barn)
get_history(selection)

#def determine_due_date(horse):

#def display_last_and_next(horse, due_date, last_service):


#need to string match horse with appropriate list from data
