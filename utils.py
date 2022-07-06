import json
import random
import requests
from classes import BasicWord


def load_random_word():
    r = requests.get('https://jsonkeeper.com/b/GUIW')
    if r.status_code == 200:
        word_list = json.loads(r.text)
    random_word = random.choice(word_list)
    game_word = BasicWord(random_word['word'], random_word['subwords'])
    return game_word