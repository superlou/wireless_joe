from pprint import pprint
from player import Player

class Team(object):
    yql = None
    league_key = None
    team_key = None

    def __init__(self, yql, league_id, team_number):
        self.yql = yql
        self.league_key = "mlb.l." + str(league_id)
        self.team_key = self.league_key + ".t." + str(team_number)

    def league_name(self):
        query = 'select * from fantasysports.leagues where league_key="' + self.league_key + '"'
        result = self.yql.execute(query)
        return result.rows[0]['name']

    def name(self):
        query = 'select * from fantasysports.teams where team_key="' + self.team_key + '"'
        result = self.yql.execute(query)
        return result.rows[0]['name']

    def fix_pitching(self, days=1):
        """
        Look at today's pitching roster and:
        1. Assign SPs by starting and ERA
        2. Set RPs by ERA
        3. Set Ps by remaining ERA
        """
        print self.find_by_position("SP")

        pass

    def find_by_position(self, position="*"):
        query = "select roster.players.player"
        query += " from fantasysports.teams.roster"
        query += " where team_key='" + self.team_key + "' and roster.players.player.eligible_positions.position='" + position + "'"
        result = self.yql.execute(query)
        return result

    def players(self):
        query = "select roster.players.player from fantasysports.teams.roster"
        query += " where team_key='{0}'"
        query = query.format(self.team_key)
        result = self.yql.execute(query)

        players = []

        for row in result.rows:
            player_data = row['roster']['players']['player']
            players.append(Player(player_data))

        return players