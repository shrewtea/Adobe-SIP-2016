adjective_list=["Spicy","Sweet","Creamy","Salty","Sour","Soggy","Mild","Fire","Tangy","Slimy"]
place_list=["African","Indian","Thai","Chinese","American","Brazilian","Hawaiian","Indonesian","Mexican","Filipino"]
dish_list=["Burger","Pasta","Pizza","Noodles","Burrito","Rice","Curry","Salad","Lasagna", "Soup"]

import random
def Menu():
	for i in range (10):
		RandomNumber=random.randint(0,9)
		rn=random.randint(0,9)
		print(adjective_list[RandomNumber],place_list[rn],dish_list[RandomNumber])
		print("  ")
print("Menu")
Menu()
print("    ")

Articles=["The","A","Some","An"]
Adjectives=["Rolling","Spinning","Jumping","Flying"]
Noun=["Stones","Cows","Dragons","Chairs"]

def BandName():
	for x in range(4):
		random_number=random.randint(0,3)
		rn=random.randint(0,3)
		print(Articles[random_number], Adjectives[rn], Noun[random_number])
		print("  ")
print("Band Names")
BandName()
print("    ")

five_syllables=["The sky is orange |","Flowers in the park |","Ice cream and cherries |","Clouds are in the sky |","The sky is not blue |","Over the wintry |","I am somebody |", "To rain in mountains |", "Winter seclusion |", "follow the river |"]
seven_syllables=["Harry Potter is the best |","I like to eat apple pie |","Chipotle is so awesome |","Puppies are very fluffy |", "Not as easy as playdough |", "Next to a gingerbread house |", "White blanket of snow did fall |", "Enjoying still darkness |", "Venus takes her place in time |", 
"From a little drop of paint |"]

def haiku():
	for z in range(3):
		random_num=random.randint(0,9)
		rn=random.randint(0,9)
		RN=random.randint(0,9)
		print(five_syllables[random_num], seven_syllables[RN], five_syllables[rn])
		print("  ")
print("Haiku")
haiku()
print("    ")
