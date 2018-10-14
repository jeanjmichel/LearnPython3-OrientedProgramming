# _____       _                    
#|  __ \     (_)                   
#| |  | |_ __ ___   _____ _ __ ___ 
#| |  | | '__| \ \ / / _ \ '__/ __|
#| |__| | |  | |\ V /  __/ |  \__ \
#|_____/|_|  |_| \_/ \___|_|  |___/
class Driver:
    def __init__(self, driver_name):
        self.driver_name = driver_name

    def __str__(self):
        return "class Driver[driver_name: {0}]".format(self.driver_name)
