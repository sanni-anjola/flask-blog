import sys
from random import choice

random1 = list(range(1,13))
random2 = list(range(1,13))
while True:
	print("To exit this game type 'exit'")
	breakpoint()
	answer = input(f"What is {choice(random2)} times {choice(random1)}? ")

	# exit
	if answer == 'exit':
		print("Now exiting game...")
		sys.exit()

		# determine if number is correct
	elif answer == choice(random2) * choice(random1):
		print("correct")
	else:
		print("Wrong")