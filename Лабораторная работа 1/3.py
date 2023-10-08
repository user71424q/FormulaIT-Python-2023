list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num_players_in_team = len(list_players) // 2
team1 = list_players[0:num_players_in_team]
team2 = list_players[num_players_in_team:]
print(team1)
print(team2)
