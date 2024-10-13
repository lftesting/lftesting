# Experimenting with nba_api. Not really defined where this is going, we will see how it goes 

from nba_api.stats.endpoints import FranchiseLeaders
from nba_api.stats.static import teams

def main():
    # collect input from user (nba team that they choose)
    team = input("Which is your favourite NBA team? ")
    # get team id to proceed with franchise leaders or remprompt user for another team if not found
    id_team = check_team(team)
    player = get_leading_scorer(id_team)
    print(f"{player[0]} is the leading scorer for the {team} with {player[1]} points.")

# check input against nba teams list
def check_team(team_name):
    for team in nba_teams:
        if team["full_name"].lower() == team_name.lower():
            return team["id"]
    return None

# fetch data for selected team
def get_leading_scorer(id_team):
    franchise_leaders = FranchiseLeaders(team_id=id_team)
    team_data = franchise_leaders.get_data_frames()[0]
    if not team_data.empty:
        leading_scorer = team_data.iloc[0]
        return leading_scorer["PTS_PLAYER"], leading_scorer["PTS"]
    else:
        return None, None


# create list of nba teams
nba_teams = teams.get_teams()




if __name__=="__main__":
    main()
