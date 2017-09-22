#Initiates a session with user.
#import display_care_data.py

#class InitiateCareSession:

def begin_dialogue():
	print "Hi User!  Hope the horses are doing well.  What would you like to do?\n"

	option = raw_input("Enter 1 if you'd like to see a horses's history.\n"
		"Enter 2 if you'd like to record a care service.\n"
		"Enter 3 if you'd like to add a new horse to your barn.\n"
		"Enter 4 if you'd like to add a new service type to the database.\n")
		
	return option

def select_option(option):
	if option == "1":
		print "Ok, we'll display a pet's history.  Would be great if you made a method to do this."
	elif option == "2":
		print "Ok, let's record a care service.  You better make a method that does this."
	elif option == "3":
		print "Wow, a new horse!  Hope you got a good paycheck from your coding skills that you'll need to write this method."
	elif option == "4":
		print "More services?  How about you get to work finishing this app instead."
	else:
		print "I didn't understand that.  Let's try again."
		initiate()
		
def initiate():
	option = begin_dialogue()
	select_option(option)

initiate()