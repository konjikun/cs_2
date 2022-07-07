def count_chars(s):
    result = {}
    for c in s:
        if c in result:
            result[c] +=1
        else:
            result[c] = 1
    return result

def draw_graph(counts):
    result =''
    for x , y in counts.items() :
        print(x, 'l', '#' * y)
draw_graph(count_chars('enemies enter from east'))