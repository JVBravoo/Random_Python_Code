import Cloudant
username = 'João Victor Montarroios'
account = cloudant.Account(João Victor Montarroios)

login = account.login('João Victor Montarroios', 'wUmdov-9hydva-cokvyn')
assert login.status_code == 200

db = account.database('Hermes')