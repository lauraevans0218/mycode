#!/usr/bin/env python3
count = 1
result = 0

while count < 6:
    print('Woof!...Calculating for you hooman...')
else:
    question1 = input("Do you prefer fashion or books?")
if question1 == 'fashion':
    count += 1
    result +=1
else:
    result -= 1

    question2 = input('Do you prefer the beach or lake?')
if question2 == 'beach':
    count += 1
    result += 1
else:
    result -= 1

    print(count)
