import time

# from espeak import espeak
from subprocess import call
from random import randint

# Set the following
# 	True when running on a Raspberry Pi
# 	False when running on Mac OSX
running_on_pi = False

# Amount of matches being followed
amount_matches = randint(1, 5)

# Declare empty array for followed matches, to be filled later on
followed_matches = []

# Match evens according to a match id
match_events = {
	0: [
		"The match Feyenoord - AZ is starting soon",
		"Feyenoord - AZ has started",
		"Goal! 1 to 0 for Feyenoord",
		"Good chance, but off-side from Dirk Kuyt",
		"AZ shot against the post"
	],
	1: [
		"The match FC Utrecht - Ajax has started",
		"Yellow card for Ramselaar",
		"Milik seems to be injured",
		"Goal! FC Utrecht opens the score with 1 to 0",
		"The coach decides to make a change, Ramselaar off, Ayoub in"
	],
	2: [
		"The match Real Madrid - Barcelona is being played at Camp Nou",
		"Zidane has not put on Karim Benzema, instead he plays Isco up front",
		"Ronaldo has done some crazy tricks so far, but has not found the goal yet",
		"Penalty! Pepe got red for a dirty tackle on Messi in the box",
		"Goal! Messi scores from a penalty to make it 1 to 0 for Barcelona"
	],
	3: [
		"Athletico Madrid against Bayern Munchen has started, whoever wins will\
		advance to the Champions League final!",
		"Close match so far, but neither have found the goal",
		"Yellow card for Lewandowski",
		"Neuer with a great save, shot by Torres",
		"Both teams have yet to score, it is now half-time with a score of 0 to 0"
	],
	4: [
		"Manchester United against Liverpool will start shortly",
		"Manchester United has kicked off the match against Liverpool",
		"Rooney is not playing today, as he is injured from last match",
		"Goal! Rashford scores with a free kick to make it 1 to 0 for Manchester",
		"Goal! Only 2 minutes since Rashford scored, Depay scores to make it 2 to 0"
	]
}


# This will cause the application to convert text to speech
# It checks whether the application is ran on Pi or MacOS, and
# will speak according to it.
def say(text):
	if running_on_pi:
		espeak.set_parameter(espeak.Parameter.Rate, 120)
		espeak.synth(text)
		while espeak.is_playing():
			time.sleep(0.1)
	else:
		call('say ' + text, shell=True)

# I am following
say('I am following {} matches.'.format(amount_matches))


# What matches are being followed are decided randomly
for i in range(amount_matches):

	# Get a random number between 0 and 4
	new_match = randint(0, 4)

	# Is the random number (match id) not yet followed?
	if new_match not in followed_matches:

		# Put the random number (match id) in the list with followed matches
		followed_matches.append(new_match)


# Loop 5 times
for i in range(5):

	# The system will sleep for a random between 0-9 seconds,
	# causing the application to appear more natural
	time.sleep(randint(1, 4))

	# For every match in our followed matches
	for match in followed_matches:

		# Wait a little bit
		time.sleep(randint(1, 9))

		# Say the latest event for this match
		say('{}'.format(match_events[match][i]))
