import random
import requests



try:
	while True:

		xpos = random.randrange(20, 50, 3)
		ypos = random.randrange(20, 50, 3)
		rotation = random.randrange(20, 50, 3)

		print(xpos)
		print(ypos)
		print(rotation)

		data = {
    			"character_name": "dood",
    			"flower_status": "plucked",
    			"character_rotation": rotation,
    			"characters_position": { "x":xpos , "y":ypos }
		}

		requests.post('https://c6xrszj8oa.execute-api.eu-west-2.amazonaws.com/dev', json=data)

		x = requests.get('https://91788rpir7.execute-api.eu-west-2.amazonaws.com/dev')
		print(x.status_code)
		print(x.text)

except KeyboardInterrupt:
    pass