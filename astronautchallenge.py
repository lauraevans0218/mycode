#!/usr/bin/env python3

import requests

def main():
    r = requests.get('http://api.open-notify.org/astros.json')
    amount = r.json().get('number')
    print('People in space: ' + str( amount))
    people = r.json().get('people')
    for person in people: 
        print(person + ' on the ')

main()
