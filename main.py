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
#firstMenu() 
#remove above comment to see the firstMenu function. 
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

firstMenu() #where firstMenu belongs. Cannot print yet because error thrown from classes (line 23-32)