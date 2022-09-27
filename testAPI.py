
import requests
import json
#import django
#from django.forms import ModelForm

#from django.urls import include, path
#from django.views.generic import TemplateView

#from django_contact_form.views import ContactFormView

#Ressources
#https://django-contact-form.readthedocs.io/en/2.0.1/quickstart.html
#https://www.univ-orleans.fr/iut-orleans/informatique/intra/tuto/django/django-forms.html
#https://docs.djangoproject.com/fr/4.1/ref/forms/api/
#https://docs.djangoproject.com/fr/4.1/topics/forms/
##


url =  "https://script.google.com/macros/s/AKfycby-TJmFFUFTfiNUbMoSIZx8LVtiskQ-bUt4xO6hmrU0XQpJS8IPUBow/exec"
data = {'cle': 'CLE-TEST-IOT', 
        'donnees' : {"id" : 'tahina.foucher@outlook.com',
                    "date" : '16/09/2022',
                    "urlRelais" :'https://github.com/LosFouchos/le-jardin-responsable',
                    "message" :'Coucou Ouivalo, j ai fais mon possible :) Hate de vous rencontrer'}}

#contact_form = ContactForm()
#f = ContactForm(data)
r = requests.post(url, data=json.dumps(data))

print(r.content)



