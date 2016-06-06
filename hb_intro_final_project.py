#functions for final project

#for each word that pops up, enter the corresponding country name.

WORLD_DICT = {"Vegemite": "Australia", "Uluru": "Australia", "Dosa": "India", \
"Kolam": "India", "Nacatamales": "Nicaragua", "Ceviche": "Peru", "Leaning Tower of Pisa": "Italy", \
"Petra": "Jordan", "Victoria Falls": "Zimbabwe", "Kiwi": "New Zealand", "Haggis": "Scotland", \
"Giants Causeway": "Ireland", "Spatzle": "Germany"}

def main():
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
	while True:
		import random
		player_input = raw_input(random.choice(WORLD_DICT.keys())+ "\nCountry: ") 
		correct = False
		for key, value in WORLD_DICT.iteritems():
			if value == player_input:
				correct = True
		if correct:
			print "Yay you're smart! Keep going!"
		else:
			print "Try again."
		
		exit_menu_input = raw_input("C - Continue\nE - Exit\nM - Main Menu")
		if player_input == "C":
			continue
		if player_input == "M":
			main()
		elif player_input == "E":
			break



#game()


# while raw_input() == "E":
# 	break




if __name__ == '__main__':
	main()