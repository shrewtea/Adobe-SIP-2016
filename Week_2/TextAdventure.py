print ("Let\'s start this story")
right_left = input("Right or Left?")
while (right_left != "Right" and right_left != "Left"):
		print("You must pick one of the choices. Try again")
		right_left = input("Right or Left?")
if right_left == "Right":
	print("You have to fight against a dragon ")	
	path1 = input("Do you want to use a sword or walk into a different path ")
	while (path1 != "sword" and path1 != "different path"):
		print("You must pick one of the choices. Try again")
		path1 = input("Do you want to use a sword or walk into a different path ")
	if path1 == "sword": 
		print ("Good choice. You kill the dragon")
		path3 = input("Do you want to walk or swim to the final destination? ")
		while path3 != ("walk" or "swim"):
			print("You must pick one of the choices. Try again")
			path3 = input("Do you want to walk or swim to the final destination?")
		if path3 == "walk":
			print ("You are tired but alive. Congrats! ")
			print ("The End")
		elif path3 == "swim":
			print ("The mermaids drown you. Choose wisely next time")
			print ("The End")
	elif path1 == "different path":
		print ("Bravery would have served you well.")
		path4 = input("Now quickly choose between a bowl of sand or gold")
		while (path4 != "gold" and path4 != "sand"):
			print("You must pick one of the choices. Try again")
			path4 = input("Now quickly choose between a bowl of sand or gold")
		if path4 == "sand":
				print ("Good choice. A monster comes toward you but you pour sand on him and you escape")
				print ("The End")
		elif path4 == "gold":
					print ("Greed will lead you to ruins. You die at the hands of the monster")
					print ("The End")

elif right_left == "Left":
	print ("You have to climb up a tower")
	path2 = input("Do you want to climb or go down dark road")
	while (path2 != "climb" and path2 != "dark road"):
		print("You must pick one of the choices. Try again")
		path2 = input("Do you want to climb or go down the dark road")
	if path2 == "climb":
			print ("Easy decisions lead to bad consquences.")
			path5 = input ("Choose between a ruby necklace or diamond bracelet.")
			while path5 != ("ruby necklace" or "diamond bracelet"):
				print("You must pick one of the choices. Try again")
				path5 = input ("Choose between a ruby necklace or diamond bracelet")
			if path5 == "ruby necklace": 
				print("The red in your necklace brightens. It burns you up. Better luck next time.")
				print("The End")
			elif path5 == "diamond bracelet":
				print("Water from bracelet drown you. Better luck next time.")
				print("The End")

	elif path2 == "dark road":
			print ("Good decision. Bravery will always be rewarded")
			path6 = input("Do you want to go through the flower pass or candy island?")
			while path6 != ("flower pass" or "candy island"):
				print("You must pick one of the choices. Try again")
				path6 = input ("Do you want to go through the flower pass or candy island?")
			if path6 == "flower pass":
				print("You walk through safe and happy. Congrats!")
				print("The End")
			elif path6 == "candy island":
				print("Greed blinds your decisions. You eat too many candies and eventually die. Better luck next time.")
				print("The End")