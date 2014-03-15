# Dependencies
# yql

from yql_auth import YqlAuth
from team import Team
import pprint
import json


pp = pprint.PrettyPrinter()

config = json.load(open('config.json'))
yql = YqlAuth('myToken', config['api_key'], config['api_secret'])

team = Team(yql, config["league_id"], config["team_number"])
print "Team:\t", team.name()
print "League:\t", team.league_name()

print team.players()

# cmd = ""
# while cmd != "exit":
# 	cmd = raw_input("> ")

# 	if cmd == "p":
# 		print team.players()