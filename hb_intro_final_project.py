"""WORDLY WORD ASSOCIATION GAME:

DIRECTIONS: For each word that pops up, enter the corresponding country name."""


# modules needed:

import sys
# for exiting the game

import random
# for choosing random values from dictionaries

from Tkinter import *
# for GUI


WORLD_DICT_EASY = {"Australia": ["Vegemite - delicious yeast extract", "Crocodile Dundee", "The Great Barrier Reef"], \
"India": ["Bollywood - Hollywood but not", "Masala Chai - what dreams are made of, also you drink it", "The Taj Mahal"], \
"Peru": ["Lima - a capital city", "Machu Picchu - there are llamas"], "Italy": ["The Leaning Tower of Pisa", "Limoncello - a lemon liqueur", \
"Gelato - a creamy dessert"], "New Zealand": ["Kiwi - a flightless bird", "Auckland - home to the iconic Sky Tower", \
"Hobbiton - a magical movie set"], "Scotland": ["Kilt - a traditional garment", "The Loch Ness Monster - it's real!"], \
"China": ["Shanghai - a global financial hub", "The Great Wall - it's pretty great, over 13,000 miles long"],  \
"Ireland": ["Guinness - you drink it", "The 'Emerald Isle' - a ridiculously green place", "Colin Farrell"], \
"Germany": ["Karl Marx - a philosopher, economist, sociologist, and more things", "Berlin - a capital city"], \
"Japan": ["Tokyo", "Samurai - noble warriors"], "Greece": ["Zeus - God of the Sky", "Aphrodite - Goddess of Love"], \
"Russia": ["The Kremlin - means 'fortress inside a city'\n(or a place that Tom Cruise and Simon Pegg broke into)", "Leo Tolstoy - a writer"], \
"UK": ["The Beatles - they're a band", "London - home of 'Big Ben'"], "Egypt": ["Cairo - there are mummies", "The Pyramids"], \
"France": ["Macaroons", "Champagne - a region, also you drink it"], "Spain": ["Barcelona - an artsy city", "Tapas - sophisticated appetizers"], \
"Canada": ["Ryan Gosling", "Maple Syrup"], "USA": ["Zion National Park", "The Golden Gate Bridge", "Donald Trump"], \
"Thailand": ["Bangkok", "Pad Thai - yum"]}


WORLD_DICT_MEDIUM = {"Australia": ["Vegemite", "Tim Tams", "Uluru / Ayers Rock", "Anzac Day"], "India": ["Dosa", "Kolam"], \
"Nicaragua": ["Nacatamales", "Granada"], "Peru": ["Ceviche", "Machu Picchu"], "Italy": ["Leonardo da Vinci", "The Colosseum", \
"Gucci, Armani, & Prada"], "Brazil": ["Rio de Janeiro", "The Christ Redeemer Statue"], "Egypt": ["The Sphinx of Giza", \
"The Book of the Dead"], "New Zealand": ["Waitomo Glowworm Caves", "Wellington", "Middle Earth"], \
"Scotland": ["Haggis", "Isle of Sky", "'Nessie'"], "Ireland": ["The Giant's Causeway", "The Blarney Stone"], \
"Germany": ["Spaetzle - egg noodle dumpling", "Berlin"], "Israel": ["Tel Aviv", "Jerusalem"], "Japan": ["Okonomiyaki - a savory pancake", \
"Ikebana - an art of flower arrangement"], "Portugal": ["Fado - a folk music genre", "Bertrand Bookstore - the oldest bookstore in the world"], \
"Singapore": ["The Merlion - half lion, half fish", "'The Garden City' - the world's only island city state country"], "Greece": \
["The Parthenon", "Aristotle"], "Russia": ["Vladimir Putin", "Leo Tolstoy"], \
"France": ["Macaroons", "Champagne"], "Spain": ["La Tomatina Festival - it's a big food fight", "Seville", "Canary Islands"], "Canada": \
["SNOLAB - deepest physics lab on earth", "Ryan Gosling", "Maple Syrup"], "USA": ["Zion National Park", "Golden Gate Bridge", \
"Statue of Liberty"], "Thailand": ["Ko Tapu - James Bond Island", "Tom Yum Soup"]}


WORLD_DICT_DIFFICULT = {"Australia": ["Quokka - a small rodent found on Rottnest Island", "Uluru", "Numbat", "Waltzing Matilda"], \
"India": ["Dosa - a thin crepe", "Kolam - a form of drawing practiced by female family members", "Jodhpur - the blue city", "Goa"], \
"Italy": ["Cinema Paradiso - 1988 film", "'Abbiocco' - feeling tired after a big meal", "'Gattara' - an elderly 'cat lady'"], "Jordan": ["Petra - 'Lost City'", \
"Hashemite"], "Zimbabwe": ["Victoria Falls", "Mount Nyangani"], "New Zealand": ["Milford Sound", "Maori people"], \
"Scotland": ["Haggis", "Isle of Sky", "'Nessie'"], "Ireland": ["Giant's Causeway", "Galway", "Temple Bar"], "Germany": ["Spatzle", \
"Berlin"], "Japan": ["Okonomiyaki", "Ikebana"], "Portugal": ["Belem Tower", "Bertrand Bookstore - the oldest bookstore in the world"], \
"Singapore": ["Sentosa Island Resort", "Changi Airport - there's a waterfall inside"], "Greece": ["The Parthenon", "Aristotle"], \
"France": ["Coco Chanel", "Champs-Elysees"], "Spain": ["Pan's Labyrinth", "Seville", "Canary Islands"], "Canada": ["Della Falls", \
"SNOLAB - deepest physics lab on earth"], "USA": ["Zion National Park", "Golden Gate Bridge", \
"Craters of the Moon - National Monument and Preserve", "Statue of Liberty", "Space Needle"], "Thailand": ["Ko Tapu - James Bond Island", \
"Tom Yum Soup"]}


USED_VALUES = []

TOTAL_SCORE = 0

POINTS = {"easy": 5, "medium": 10, "difficult": 20}


def main():
	# main menu, questions correspond to level of difficulty
	
	response = {1: {"text": "\n\nStop whining. Let's see what you've got!", "dict": WORLD_DICT_DIFFICULT, "level": "difficult"}, \
	2: {"text": "\n\nWhat does the moon have to do with it? Try again", "dict": "main()", "level": None}, \
	3: {"text": "\n\nThat is just pathetic but good luck anyways!", "dict": WORLD_DICT_EASY, "level": "easy"}, \
	4: {"text": "\n\nWow do you have WiFi under there? \nWell nevermind it's time to test your knowledge!", "dict": WORLD_DICT_MEDIUM, "level": "medium"}, \
	5: {"text": "\n\nOh dear. Ok. Please proceed with caution.", "dict": WORLD_DICT_EASY, "level": "easy"}, \
	6: {"text": "\n\nExcellent a normal person! Go time!", "dict": WORLD_DICT_DIFFICULT, "level": "difficult"}}

	while True:
		
		print "\n--- Welcome to The Worldly Word Association Game! ---\n"
		
		intro_choice = int(raw_input("How would you rate your worldly-ness??\n\n> Choose a number:\n\n\
  1 - I have been to all places of this earth and I am le tired.\n\
  2 - I have been to the moon!\n\
  3 - I have never been outside my house and I am le sad.\n\
  4 - I live under a rock. I am le flat.\n\
  5 - There's a world out there??!!?\n\
  6 - Whatever. Let's do this!!!!!!\n\
		\n* Type 0 anytime to Exit *\n"))

		if intro_choice in response.keys():
			
			print response[intro_choice]["text"]
			
			dictionary = response[intro_choice]["dict"]
			level = response[intro_choice]["level"]
			
			if dictionary == "main()":
				continue
			
			if dictionary != "main()":
				game(dictionary, level)
		
		elif intro_choice == 0:
			print "Goodbye thanks for playing!"
			sys.exit()
		
		else:
			print "Oops try again"



def game(dictionary, level):
	# main game function, uses random value to prompt user and check if answer is correct
	retry = False
	# retry will remain False until user answers incorrectly
	global USED_VALUES

	while True:
	# loop to keep game running continuously
		if retry == False:
			random_results = get_random_value(dictionary)
			
			if random_results[0] in USED_VALUES:
			# if word has already been used, pick another one
				random_results = get_random_value(dictionary)

		player_input = (raw_input("\n1 - Main Menu\n0 - Exit\n\nQUESTION:\
			\n----------------------------------------------------------\nWhat country do I belong to?\n--> "\
			 + random_results[0] + "\n----------------------------------------------------------\nANSWER: ")).lower()

		if player_input == "1" or player_input == "0":
			exit_menu(player_input)
		
		if player_input == (random_results[1]).lower():
		# check if answer is correct	
			print "\n\n\n--> Yay you're smart! Keep going!"
			
			retry = False
			# no need to retry, move on to next random value from dictionary
			USED_VALUES.append(random_results[0])
			# add already used value to USED_VALUES list
			get_score(level)
		
		else:
			retry = True
			# must supply same random value in order for user to retry
			print "\n--> TRY AGAIN"


def get_random_value(dictionary):

	random_country = random.choice(dictionary.keys())
	# choose a random key from dictionary
	values = dictionary.get(random_country)
	# get the values for that key
	random_value = random.choice(values)
	# choose a random value from that key
	
	return (random_value, random_country)


def get_score(level):

	global TOTAL_SCORE

	TOTAL_SCORE += POINTS[level]
	# increases score based on level

	print "--> TOTAL SCORE: ", TOTAL_SCORE
	return TOTAL_SCORE


def exit_menu(player_input):

	if player_input == "1":
		main()
	
	if player_input == "0":
		end_graphic()
		print "\nGoodbye, see you next time!\n"
		sys.exit()


def end_graphic():
	
	canvas_width = 800
	canvas_height = 571

	master = Tk()

	canvas = Canvas(master, bg="black", 
           		width=canvas_width, 
           		height=canvas_height)
	canvas.pack()

	img = PhotoImage(file="hb_gui_worldmap_medium.pbm")
	canvas.create_image(20,20, anchor=NW, image=img)

	mainloop()



if __name__ == '__main__':
	main()




