#   _____      _ _           _   _                 
#  / ____|    | | |         | | (_)                
# | |     ___ | | | ___  ___| |_ _  ___  _ __  ___ 
# | |    / _ \| | |/ _ \/ __| __| |/ _ \| '_ \/ __|
# | |___| (_) | | |  __/ (__| |_| | (_) | | | \__ \
#  \_____\___/|_|_|\___|\___|\__|_|\___/|_| |_|___/
print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| A collection can be a set of complexes objects named dictionaries:                                                          |")
print("|                                                                                                                             |")
print("| Assuming this collection:                                                                                                   |")
print("|                                                                                                                             |")
print("|  soccer_teams = [{\"team_name\":\"Sport Club Internacional\",                                                                   |")
print("|                   \"team_notable_players\":[\"Branco\", \"Gamarra\", \"D'ALessandro\",                                              |")
print("|                                           \"Falcão\", \"Taffarel\", \"Dunga\",                                                    |")
print("|                                           \"Figueroa\", \"Valdomiro\"],                                                         |")
print("|                   \"team_notable_titles\": [\"FIFA Club World Cup in 2006\",                                                    |")
print("|                                           \"Copa Libertadores da América in 2006 and 2010\",                                  |")
print("|                                           \"Brazilian Football Championship in 1975, 1976 e 1979\"]},                         |")
print("|                  {\"team_name\":\"Futbol Club Barcelona\",                                                                      |")
print("|                   \"team_notable_players\":[\"Ronaldinho\", \"Ronaldo\",  \"Rivaldo\",  \"Romário\",  \"Messi\"],                       |")
print("|                   \"team_notable_titles\": [\"FIFA Club World Cup in 2009, 2011 and 2015\",                                     |")
print("|                                           \"Liga dos Campeões da UEFA in 1991/92, 2005/06 2008/09, 2010/11 e 2014/15\"]}]     |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
soccer_teams = [{"team_name":"Sport Club Internacional", 
                 "team_notable_players":["Branco", "Gamarra", "D'ALessandro", "Falcão", "Taffarel", "Dunga", 
                                         "Figueroa", "Valdomiro"],
                 "team_notable_titles": ["FIFA Club World Cup in 2006", 
                                         "Copa Libertadores da América in 2006 and 2010", 
                                         "Brazilian Football Championship in 1975, 1976 e 1979"]},
                {"team_name":"Futbol Club Barcelona", 
                 "team_notable_players":["Ronaldinho", "Ronaldo",  "Rivaldo",  "Romário",  "Messi"],
                 "team_notable_titles": ["FIFA Club World Cup in 2009, 2011 and 2015", 
                                         "Liga dos Campeões da UEFA in 1991/92, 2005/06 2008/09, 2010/11 e 2014/15"]}]

print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| Printing all elements and his details:                                                                                      |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
for team in soccer_teams:
    print("Team: {0}".format(team["team_name"]))
    print("  Notable players:")
    for notable_players in team["team_notable_players"]:
        print("    {0}".format(notable_players))
    print("  Notable titles:")
    for notable_titles in team["team_notable_titles"]:
        print("    {0}".format(notable_titles))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| Python is zero based, you can access an array element with element's index:                                                 |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("Team at index {0} is: {1}".format(0, soccer_teams[0]["team_name"]))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| You can list all keys of a collection:                                                                                      |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("Collection's keys: {0}".format(soccer_teams[0].keys()))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| You can list all values of a collection:                                                                                    |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("Collection's values: {0}".format(soccer_teams[0].values()))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| Deleting an element of a collection:                                                                                        |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("Before: {0}".format(soccer_teams[1]["team_notable_players"]))
del soccer_teams[1]["team_notable_players"][4]
print("After: {0}".format(soccer_teams[1]["team_notable_players"]))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| Appending an element of a collection:                                                                                       |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("Before: {0}".format(soccer_teams[1]["team_notable_players"]))
soccer_teams[1]["team_notable_players"].append("Iniesta")
print("After: {0}".format(soccer_teams[1]["team_notable_players"]))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| Length of a collection:                                                                                                     |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("There are {0} big players in {1}.".format(len(soccer_teams[0]["team_notable_players"]), soccer_teams[0]["team_name"]))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| Checking if an collection contains an element:                                                                              |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("Has {0} ever won a Gauchão championship? Answer: {1}".format(soccer_teams[1]["team_name"], 
                                                                    soccer_teams[1]["team_notable_titles"].__contains__("Gauchão")))
print("Is Taffarel a famous player of Inter? Answer: {0}".format( soccer_teams[0]["team_notable_players"].__contains__("Taffarel")))

print("")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print("| Is possible return a range of elements in a collection doing:                                                               |")
print("|                                                                                                                             |")
print("|   soccer_teams[0][\"team_notable_players\"][1:]   # Return all elements after index 0 (1 or higher)                           |")
print("|   soccer_teams[0][\"team_notable_players\"][:-1]  # Return all elements before the last index (len -1)                        |")
print("|   soccer_teams[0][\"team_notable_players\"][2:-2] # Return all elements between the indexs                                    |")
print("+-----------------------------------------------------------------------------------------------------------------------------+")
print(soccer_teams[0]["team_notable_players"][1:])
print(soccer_teams[0]["team_notable_players"][:-1])
print(soccer_teams[0]["team_notable_players"][2:-2])
