sports = ['cricket','lacrosse']
n_players = [11,10,11,7,7,8]

sports = ['cricket','lacrosse','hockey','water_polo','kabaddi','tug_of_war']
n_players = [11,10,11,7,7,8]
sp_players= {}

for people, exercise in zip(n_players, sports):
    sp_players[exercise] = people
