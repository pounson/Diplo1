import requests
TOKEN = "2619421814940190"

urls = "https://superheroapi.com/api/2619421814940190/search/"
superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

for hero in superheroes:
    hero01 = requests.get(urls + hero['name'])
    hero['intelligence'] = int(hero01.json()['results'][0]['powerstats']['intelligence'])

print(sorted(superheroes, key=lambda hero: -hero['intelligence'])[0]['name'])