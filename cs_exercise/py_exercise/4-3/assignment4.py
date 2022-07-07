def sutoro(text):
    sunuki =''
    for i in text:
        if i != 'す':
            sunuki += i
    return sunuki

text = """すぱいすそんつすかいこすなすすしてえすらいす
すそのちょすうしですこすれからすもすとりすくすもう
すこすこからすまたどすんどすんすむずすかしくす
なするすからすふくすしゃすうをすしっかすりすやすろうすね"""
print( sutoro(text) )