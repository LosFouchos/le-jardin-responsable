import requests

r = requests.post(' https://script.google.com/macros/s/AKfycby-TJmFFUFTfiNUbMoSIZx8LVtiskQ-bUt4xO6hmrU0XQpJS8IPUBow/exec', data={'cle': 'CLE-TEST-IOT', 'donnees' : ['tahina.foucher@outlook.com','16/09/2022','https://github.com/LosFouchos/le-jardin-responsable','Coucou Ouivalo, j ai fais mon possible :)']})
r.status_code
print(r.text)
r.json()

