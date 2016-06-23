import requests
import time

from espeak import espeak
from subprocess import call


# DECLARING GLOBAL VARIABLES #

# Set the following
# 	True when running on a Raspberry Pi
# 	False when running on Mac OSX
running_on_pi = False

# API URl's
devthisapi = 'http://devthisapi.jordibeen.nl/api/v1/matches'
footballstreamapi = 'http://footballstream-api.jordibeen.nl/api/v1/matches'


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


# Function to perform a request to api given
# as param, and return the json response
def json_request(api):
	r = requests.get(api)
	json_response = r.json()
	return json_response


# Continuous loop starts here
while True:
	# Let the application rest for 5 seconds
	time.sleep(5)

	# Perform a request to the D3VTH1S API
	devthisapi_json_response = json_request(devthisapi)

	# If there are no matches
	if 'match' not in devthisapi_json_response:
		# Tell the user to select matches
		say('Please select matches')
		continue

	# Get the matchid's that the user has selected
	match_ids = devthisapi_json_response['match']['match_ids']

	# If there are no match_ids given
	if not match_ids:
		# Tell the user no matches are selected
		say('No matches selected')

	# For every match_id that the user has selected
	for match_id in match_ids.split(","):
		# Tell the user I am following the match
		say('i am following match with ID {}'.format(match_id))

		# Perform a request to the FootballStream API
		# with the match_id as parameter
		footballstreamapi_json_response = json_request('{}/{}'.format(
			footballstreamapi, match_id))

		# If there is a match found for the ID
		if 'match' in footballstreamapi_json_response:
			match = footballstreamapi_json_response['match']
			# Tell the use the matchup he has selected
			say('This game is {}'.format(match['matchup']))
