import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '342401c47a962a78625e2413e97362e0'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_TOKEN = TOKEN
ID = '233167' 
body_create = {
    "name": "Питон",
    "photo_id": 7}
body_rename = {
    "pokemon_id": ID,
    "name": "Горыныч"}
body_add_pokeball = {
    "pokemon_id": ID
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

response_rename = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print (response_rename.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print (response_add_pokeball.text)
