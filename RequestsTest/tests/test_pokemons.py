import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '342401c47a962a78625e2413e97362e0'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '18362'
TRAINER_NAME = 'Guru'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'Guru'

