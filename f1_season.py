#  ______ __    _____                            
# |  ____/_ |  / ____|                           
# | |__   | | | (___   ___  __ _ ___  ___  _ __  
# |  __|  | |  \___ \ / _ \/ _` / __|/ _ \| '_ \ 
# | |     | |  ____) |  __/ (_| \__ \ (_) | | | |
# |_|     |_| |_____/ \___|\__,_|___/\___/|_| |_|
import team
import driver

class F1_Season:
    def __init__(self, season, teams):
        self.season = season
        self.teams = teams

    def __str__(self):
        return "F1 season #{0}".format(self.season)

    def print_season_details(self, f1_season):
        print("F1 season #{0}".format(f1_season.season))
        for team in f1_season.teams:
            print("  Team: {0}".format(team.team_name))
            for driver in team.team_drivers:
                print("    Driver: {0}".format(driver))