from DecryptLogin import login
lg = login.Login()
infos_return, session = lg.toutiao(username, password, 'mobile')
print(infos_return, session)
