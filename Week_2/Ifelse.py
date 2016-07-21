number = 79
user_guess = input ("Guess my lucky number")

while number != int(user_guest):
	if number < int(user_guest):
		print ("Too low")
		guess = input("Try again")
	else:
		print ("Too high")
		guess = input("Try again")

if number == int(user_guest):
	print ("You guessed the right number")

print ("Game Over")