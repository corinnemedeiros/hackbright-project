"""Worldly Word Association Game"""

#functions for final project
import random

#directions: for each word that pops up, enter the corresponding country name.

WORLD_DICT_TEST = {"Australia": ["Vegemite", "Uluru / Ayers Rock", "Numbat"], "India": ["Dosa", "Kolam", "Saree / Sari"], \
"Nicaragua": ["Nacatamales", "Granada"], "Peru": ["Ceviche", "Machu Picchu"], "Italy": \
["Leaning Tower of Pisa", "Abbiocco", "Gattara - an elderly 'cat lady'"], "Jordan": ["Petra", "Hashemite"], "Zimbabwe": \
["Victoria Falls", "Mount Nyangani"], "New Zealand": ["Kiwi", "Maroi"], "Scotland": ["Haggis", "'Nessie'"], \
"Ireland": ["Giant's Causeway", "Guinness", "Emerald Isle"], "Germany": ["Spatzle", "Berlin"], "Japan": ["Okonomiyaki", \
"Ikebana"], "Portugal": ["Fado - a folk music genre", "Lisbon", "Bertrand Bookstore - the oldest bookstore in the world"], \
"Singapore": ["Merlion", "chicken rice"], "Greece": ["The Parthenon", "Aristotle"], "Russia": ["Kremlin", "Tolstoy"], \
"France": ["Macaroons", "Champagne"], "Spain": ["La Tomatina Festival", "Seville", "Canary Islands"], "Canada": ["Della Falls", \
"SNOLAB - deepest physics lab on earth", "Ryan Gosling", "Maple Syrup"], "USA": ["Zion National Park", "Golden Gate Bridge", \
"Statue of Liberty"], "Thailand": ["Ko Tapu - James Bond Island", "Bangkok", "Tom Yum Soup"]}



def main():
	#main menu, questions correspond to level of difficulty
	while True:
		
		print "\nWelcome to the worldly word association game!\n"
		intro_choice = int(raw_input("How would you rate your worldly-ness?? Choose a number:\n\
	1 - I have been to all places of this earth I am le tired.\n\
	2 - I have been to the moon!\n\
	3 - I have never been outside my house I am le sad.\n\
	4 - I live under a rock, I am le flat.\n\
	5 - There's a world out there??!!?\n\
	6 - Whatever. Let's do this!!!!!!\n\
		\nType 0 to Exit\n"))
		
		if intro_choice == 1:
			print "Stop whining. Let's see what you've got!"
			game()
		elif intro_choice == 2:
			print "What does the moon have to do with it? Try again."
		elif intro_choice == 3:
			print "That is just pathetic but good luck anyways!"
			game()
		elif intro_choice == 4:
			print "Um. Do you have WiFi under there? Well nevermind it's time to test your knowledge!!"
			game()
		elif intro_choice == 5:
			print "Oh dear. Ok. Please proceed with caution."
			game()
		elif intro_choice == 6:
			print "Excellent. A normal person! Go time!"
			game()
		elif intro_choice == 0:
			break
		else:
			print "Oops try again"
		
	print "Goodbye thanks for playing!"



def game():
	#main game function
	retry = False

	while True:
	#loop to keep choosing random words from dictionary	
		if retry == False:
			random_country = random.choice(WORLD_DICT_TEST.keys())
			#choose a random key from dictionary
			values = WORLD_DICT_TEST.get(random_country)
			#get the values for that key
			random_value = random.choice(values)
			#choose a random value from that key

		player_input = raw_input(random_value + "\nWhat country do I belong to?\nAnswer: ")
		
		if player_input == random_country:
		#check if answer is correct	
			print "Yay you're smart! Keep going!"
			retry = False
		else:
			print "Try again."
			retry = True
		
		exit_menu_input = raw_input("C - Continue\nE - Exit\nM - Main Menu\n")
		#options for user to continue, return to main menu, or exit
		if exit_menu_input == "C":
			continue
		elif exit_menu_input == "M":
			main()
		elif exit_menu_input == "E":
			break



if __name__ == '__main__':
	main()