#!/usr/bin/env python3
import random
import time

dogs = ['Poodle', 'Pomeranian', 'Pitbull', 'Golden Retreiver', 'Boxer', 'Pug', 'German Shepard', 'Husky', 'Corgi', "Great Dane"]

question1 = input("Do you prefer fashion or books?")
print('Woof! Calculating for you hooman...')
time.sleep(.8)
question2 = input('Do you prefer the beach or lake?')
print('Woof! Calculating for you hooman...')
time.sleep(.8)
question3 = input('Do your friends think you are goofy or serious?')
print('Woof! Calculating for you hooman...')
time.sleep(.8)
question4 = input('Would you rather go to the gym or skiing?')
print('Woof! Calculating for you hooman...')
time.sleep(.8)
question5 = input('Do you like to dance or are you more of a wallflower?')
time.sleep(.8)
print('Woof! you are a ' + random.choice(dogs))
