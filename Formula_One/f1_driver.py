# _____       _                    
#|  __ \     (_)                   
#| |  | |_ __ ___   _____ _ __ 
#| |  | | '__| \ \ / / _ \ '__/ 
#| |__| | |  | |\ V /  __/ |
#|_____/|_|  |_| \_/ \___|_|
class F1_Driver:
    def __init__(self, driver_name):
        self.driver_name = driver_name

    def __str__(self):
        return "class F1_Driver[driver_name: {0}]".format(self.driver_name)
