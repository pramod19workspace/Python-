""" 
snake water gun
This is a fun game which most of them would have played in their childhood
so lets create the game using python :)
"""
import random

def game(comp,player):
    if comp=='s' and player=='s':
        print("Both selected snake\nReplay")
    elif comp=='s' and player=='w':
        print(f'Comp selected snake and player selected water\nSo Comp is the winner')
    elif comp=='s' and player=='g':
        print(f'Comp selected snake and player selected gun\nSo Player is the winner')
    if comp=='w' and player=='w':   
        print("Both selected water\nReplay")
    elif comp=='w' and player=='s':
        print(f'Comp selected water and player selected snake\nSo player is the winner')
    elif comp=='w' and player=='g':
        print(f'Comp selected water and player selected gun\nSo comp is the winner')
    if comp=='g' and player=='g':
        print("Both selected gun\nReplay")
    elif comp=='g' and player=='s':
        print(f'Comp selected gun and player selected snake\nSo Comp is the winner')
    elif comp=='g' and player=='w':
        print(f'Comp selected gun and player selected water\nSo Player is the winner')


print("Computer turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
# print(randNo)
if randNo==1:
    comp='s'
if randNo==2:
    comp='w'
if randNo==3:
    comp='g'

player=input("your turn: Snake(s) Water(w) or Gun(g)?\n")

game(comp,player)
