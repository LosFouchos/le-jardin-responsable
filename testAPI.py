
import requests
import json
url =  "https://script.google.com/macros/s/AKfycby-TJmFFUFTfiNUbMoSIZx8LVtiskQ-bUt4xO6hmrU0XQpJS8IPUBow/exec"
data = {'cle': 'CLE-TEST-IOT', 'donnees' : ['tahina.foucher@outlook.com','16/09/2022','https://github.com/LosFouchos/le-jardin-responsable','Coucou Ouivalo, j ai fais mon possible :) Hate de vous rencontrer']}

r = requests.post(url, data=json.dumps(data))

print(r.content)


