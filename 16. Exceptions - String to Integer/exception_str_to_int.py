#!/bin/python3


S = input().strip()
### My Code Here ###
try:
    print(int(S))
except Exception:
    print('Bad String')