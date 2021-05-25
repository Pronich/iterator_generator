from iterate import IterateCountry
from generate import generate
import os
from pprint import pprint
import json

if __name__ == '__main__':
    filepath = os.getcwd()
    with open(os.path.join(filepath, 'countries.json'), 'r') as f:
        data = json.load(f)

    with open(os.path.join(filepath, 'country_dict.txt'), 'a') as nf:
        for item in IterateCountry(data):
            nf.write(f'{item[0]} - {item[1]}\n')

    for hash in generate('country_dict.txt'):
        pprint(hash)