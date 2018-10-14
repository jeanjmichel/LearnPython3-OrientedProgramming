# _______                      
#|__   __|                     
#  | | ___  __ _ _ __ ___  
#  | |/ _ \/ _` | '_ ` _ \
#  | |  __/ (_| | | | | | \
#  |_|\___|\__,_|_| |_| |_|
class F1_Team:
    
    def __init__(self, team_name, drivers):
        self.team_name = team_name
        self.team_drivers = drivers

    def __str__(self):
        return "class F1_Team[team_name: {0}, team_drivers: {1}]".format(self.team_name, self.team_drivers)
