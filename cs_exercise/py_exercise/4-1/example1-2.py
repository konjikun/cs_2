while True:
    e_mail = input('E-mailアドレス')
    if e_mail.endswith('@iniad.org'):
        break
    else:
        print('再入力してください。')
print('あなたのe_mailアドレスは',e_mail,'です。')

