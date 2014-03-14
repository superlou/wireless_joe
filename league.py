class League:
    yql = None
    league_key = None
    team_key = None

    def __init__(self, yql, league_id):
        self.yql = yql
        self.league_key = "mlb.l." + str(league_id)


    def league_name(self):
        query = 'select * from fantasysports.leagues where league_key="' + self.league_key + '"'
        result = self.yql.execute(query)
        return result.rows[0]['name']
