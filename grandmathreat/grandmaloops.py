#!/usr/bin/env python3

def threats():
    food = ['biscuit','broccoli', 'dirty dish']
    item = ['plate',' room']
    action = ['slap you', 'kick your butt', 'flog you']
    for ele in food:
        for location in item:
            for do in action: 
                print(f'For every {ele} I find on your {location} I am  going to {do}.')
threats()
