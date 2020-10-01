#!/usr/bin/python3
import requests


def api_slice():
    choice = input('What pokemon would you like to see: ')
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon-form/{choice}/')
    poke_pic = r[1].sprites.front_default.json()
    return poke_pic


if __name__ == '__main__':
    print(api_slice())

