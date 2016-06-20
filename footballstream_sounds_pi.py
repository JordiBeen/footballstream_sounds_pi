#Uncomment if testing on Pi
from espeak import espeak

#Uncomment if testing on MacOS
#from subprocess import call

import requests
import time

def say(text):
	#Uncomment if testing on Pi
	espeak.set_parameter(espeak.Parameter.Rate, 120)
	espeak.synth(text)
	while espeak.is_playing():
		time.sleep(0.1)

	#Uncomment if testing on MacOS
	#call('say ' + text, shell=True)

devthisapi = 'http://devthisapi.jordibeen.nl/api/v1/matches'
footballstreamapi = 'http://footballstream-api.jordibeen.nl/api/v1/matches'

while True:
	time.sleep(5)


	r = requests.get(devthisapi)

	json_response = r.json()

	if 'match' not in json_response:
		say('Please select matches')
		continue

	match_ids = json_response['match']['match_ids']

	if not match_ids:
		say('No matches selected')

	for match_id in match_ids.split(","):
		say('i am following match with id {}'.format(match_id))
		r = requests.get('{}/{}'.format(footballstreamapi, match_id))
		json_response = r.json()
    	
		if 'match' in json_response:
	        	match = json_response['match']
        		say('This game is {}'.format(match['matchup']))
