#Uncomment if testing on Pi
#from espeak import espeak

#Uncomment if testing on MacOS
#from subprocess import call

import requests
import time

def say(text):
	#Uncomment if testing on Pi
	#espeak.set_parameter(espeak.Parameter.Rate, 120)
	#espeak.synth(text)
	#while espeak.is_playing():
	#	time.sleep(0.1)

	#Uncomment if testing on MacOS
	#call('say ' + text, shell=True)

devthisapi = 'http://devthisapi.jordibeen.nl/api/v1/matches'
footballstreamapi = 'http://footballstream-api.jordibeen.nl/api/v1/matches'

r = requests.get(devthisapi)

json_response = r.json()

if 'match' not in json_response:
	say('Please select matches')
	exit

match_ids = json_response['match']['match_ids']

for match_id in match_ids.split(","):
	say('i am following match with id {}'.format(match_id))
	r = requests.get('{}/{}'.format(footballstreamapi, match_id))
	json_response = r.json()
    	
	if 'match' in json_response:
        	match = json_response['match']
		ft_score = match['ft_score'].replace('[', '').replace(']', '').replace('-', ' to ')
        	say('This game is {}'.format(match['matchup']))
        	say('This game ended with {}'.format(ft_score))
