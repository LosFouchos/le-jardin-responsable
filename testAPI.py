
import requests
import json
url =  "https://script.google.com/macros/s/AKfycby-TJmFFUFTfiNUbMoSIZx8LVtiskQ-bUt4xO6hmrU0XQpJS8IPUBow/exec"
data = {'cle': 'CLE-TEST-IOT', 
        'donnees' : {"id" : 'tahina.foucher@outlook.com',
                    "date" : '16/09/2022',
                    "urlRelais" :'https://github.com/LosFouchos/le-jardin-responsable',
                    "message" :'Coucou Ouivalo, j ai fais mon possible :) Hate de vous rencontrer'}}

r = requests.post(url, data=json.dumps(data))

print(r.content)



