import os
import sys
from characters import *
from menus import *

#START OF MAIN MENU
mainMenu()
selectionNum = input()
if selectionNum == 2:
    quit()
else:
    #os.system('clear')
    nameMenu()
#INPUT PLAYER NAME
playerName = input()

#PICK YOUR CLASS
#os.system('clear')
classMenu() 
selectionNum = input()
if selectionNum == '1':
    playerClass = BME()
if selectionNum == '2':
    playerClass = Chemical()
if selectionNum == '3':
    playerClass = CompSci()
if selectionNum == '4':
    playerClass = ECE()
if selectionNum == '5':
    playerClass = Mechanical()

#BEGIN GAME SEQUENCE
#os.system('clear')
firstMenu()
input()
#os.system('clear')
secondMenu()

#BEGIN MINI BOSS FIGHT
annoyingStudent = MiniBoss()
while annoyingStudent.hp > 0:
    #os.system('clear')
    miniBossFight(playerClass.hp,annoyingStudent.hp,playerClass.level)
    selectionNum = input()
    if selectionNum == '1':
        annoyingStudent.hp = annoyingStudent.hp - playerClass.attack
    playerClass.hp = playerClass.hp - annoyingStudent.attack
    if playerClass.hp <= 0:
        #os.system('clear')
        #lostToMiniBoss()
        quit()
playerClass.level += 1
victoryMiniBoss()

#BEGIN TRANSITION TO BOSS FIGHT