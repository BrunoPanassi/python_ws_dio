import requests 
from bs4 import BeautifulSoup
import json

res = requests.get('https://digitalinnovation.one')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

section = soup.find(class_ = 'study-free-with-inovators-professionals')
professionalsTags = section.find_all(class_ = 'col-md-3')

ourProfessionals = []
for professional in professionalsTags:
    name    = professional.h3.text
    job     = professional.h4.text
    company = professional.h5.text
    ourProfessionals.append(
        {'name':name,
         'job':job,
         'company':company})

with open('professionals_json.json', 'w', encoding='utf-8') as json_file:
    json.dump(ourProfessionals, json_file, ensure_ascii=False)
    