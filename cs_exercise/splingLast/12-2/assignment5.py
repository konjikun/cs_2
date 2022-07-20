sports = ['cricket','lacrosse','hockey','water_polo','kabaddi','tug_of_war']
n_players = [11,10,11,7,7,8]
sp_players= {}
a =0
for i in sports:
    sp_players[sports[a]] = n_players[a]
    a+=1

print(sp_players['hockey'])