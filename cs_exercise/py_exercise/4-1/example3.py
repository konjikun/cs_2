def message (name, venue, id):
    msg = '''{0} さま

    あなたの受験番号は以下の通りです：
    ・受験番号：{2}
    ・受験会場：{1}

    ４月１日　１３：００に間に合うよう、余裕をもって会場にお越しください。'''
    return msg.format(name,venue,id)
   
print(message('東洋　太郎','4201教室','00001'))