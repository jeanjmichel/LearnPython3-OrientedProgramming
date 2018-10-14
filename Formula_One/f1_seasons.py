# ______ __    _____                                
#|  ____/_ |  / ____|                               
#| |__   | | | (___   ___  __ _ ___  ___  _ __  ___ 
#|  __|  | |  \___ \ / _ \/ _` / __|/ _ \| '_ \/ __|
#| |     | |  ____) |  __/ (_| \__ \ (_) | | | \__ \
#|_|     |_| |_____/ \___|\__,_|___/\___/|_| |_|___/
import f1_team
import f1_driver
import f1_season

class F1_Seasons:
    def __init__(self, f1_seasons):
        self.f1_seasons = f1_seasons

    def __str__(self):
        return "F1 seasons"

    def print_seasons_details(self, f1_seasons):
        for season in f1_seasons.f1_seasons:
            season.print_season_details(season)

f1_season_2017_teams = []
f1_season_2017_teams.append(f1_team.F1_Team("Scuderia Ferrari", ["Kimi Raikkonen", "Sebastian Vettel"]))
f1_season_2017_teams.append(f1_team.F1_Team("McLaren F1 Team", ["Fernando Alonso", "Jenson Button"]))
f1_season_2017_teams.append(f1_team.F1_Team("Mercedes AMG Petronas Motorsport", ["Lewis Hamilton", "Valtteri Bottas"]))
f1_season_2017 = f1_season.F1_Season(2017, f1_season_2017_teams)

f1_season_2018_teams = []
f1_season_2018_teams.append(f1_team.F1_Team("Scuderia Ferrari", ["Kimi Raikkonen", "Sebastian Vettel"]))
f1_season_2018_teams.append(f1_team.F1_Team("McLaren F1 Team", ["Fernando Alonso", "Stoffel Vandoorne"]))
f1_season_2018_teams.append(f1_team.F1_Team("Mercedes AMG Petronas Motorsport", ["Lewis Hamilton", "Valtteri Bottas"]))
f1_season_2018 = f1_season.F1_Season(2018, f1_season_2018_teams)

seasons = []
seasons.append(f1_season_2017)
seasons.append(f1_season_2018)

f1_seasons = F1_Seasons(seasons)
f1_seasons.print_seasons_details(f1_seasons)