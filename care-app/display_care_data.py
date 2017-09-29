import json
from datetime import datetime, timedelta
#Fetching & displaying

#**kwargs will be useful here	
#Create my data object as a class object
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

	horse = str(barn[selection])

	print "You selected " + horse
	return horse


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


def determine_due_date(horse, service):

	with open (horse + '.json') as i:
		data = json.load(i)
		
	service_history = []
	for x in data[service]:
		service_history.append(x)
	
	s = str(max(service_history))
	last_service_date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
	print "The last date of %s was %s." % (service, last_service_date)
	
barn = create_barn()
horse = select_horse(barn)
determine_due_date(horse, "shoes")
	
#def display_last_and_next(horse, due_date, last_service):


#need to string match horse with appropriate list from data
