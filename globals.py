import json

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)


prefix = config['prefix']
token = config['token']

afk = config["afk"]
afkMessage = config["message"]
afkTime = config["afkTime"]