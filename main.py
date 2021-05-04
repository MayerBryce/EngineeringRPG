import os
import sys
import random
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


#BEGIN MINI BOSS FIGHT          (maybe??) change naming conventions (academic advisor is the mini boss) OR we can have every enemy encounter except for the final boss be considered a mini boss; would be easier than changing the name of each variables
annoyingStudent = MiniBoss()
while annoyingStudent.hp > 0:
    #os.system('clear')
    playerClass.attack = playerClass.level * randrange(5,9)
    annoyingStudent.attack = randrange(0,2)
    miniBossFight(playerClass.hp,annoyingStudent.hp,playerClass.level)
    selectionNum = input()
    if selectionNum == '1':
        annoyingStudent.hp = annoyingStudent.hp - playerClass.attack
    playerClass.hp = playerClass.hp - annoyingStudent.attack
    if selectionNum == '2':
                annoyingStudent.hp = annoyingStudent.hp - playerClass.attack * 2
                playerClass.diningDollars -= 50
    #os.system('clear')
    enemyAttacked()
    input()
    if playerClass.hp <= 0:
        #os.system('clear')
        lostToMiniBoss()
        quit()
playerClass.level += 1
victoryMiniBoss()
playerClass.hp = 100

#BEGIN CLEANING JANITOR FIGHT
cleaningJanitor = MiniBoss()
while cleaningJanitor.hp > 0:
    #os.system('clear')
    playerClass.attack = playerClass.level * randrange(5,9)
    cleaningJanitor.attack = randrange(0,2)
    miniBossFight2(playerClass.hp,cleaningJanitor.hp,playerClass.level)
    selectionNum = input()
    if selectionNum == '1':
        cleaningJanitor.hp = cleaningJanitor.hp - playerClass.attack
    playerClass.hp = playerClass.hp - cleaningJanitor.attack
    if selectionNum == '2':
                cleaningJanitor.hp = cleaningJanitor.hp - playerClass.attack * 2
                playerClass.diningDollars -= 50
    #os.system('clear')
    enemyAttacked()
    input()
    if playerClass.hp <= 0:
        #os.system('clear')
        lostToMiniBoss()
        quit()
playerClass.level += 1
victoryMiniBoss()
playerClass.hp = 100

#BEGIN ACADEMIC ADVISOR FIGHT
academicAdvisor = MiniBoss()
while academicAdvisor.hp > 0:
    #os.system('clear')
    playerClass.attack = playerClass.level * randrange(5,9)
    academicAdvisor.attack = randrange(0,2)
    miniBossFight3(playerClass.hp,academicAdvisor.hp,playerClass.level)
    selectionNum = input()
    if selectionNum == '1':
        academicAdvisor.hp = academicAdvisor.hp - playerClass.attack
    playerClass.hp = playerClass.hp - academicAdvisor.attack
    if selectionNum == '2':
                MiniBoss.hp = MiniBoss.hp - playerClass.attack * 2
                playerClass.diningDollars -= 50
    #os.system('clear')
    enemyAttacked()
    input()
    if playerClass.hp <= 0:
        #os.system('clear')
        lostToMiniBoss()
        quit()
playerClass.level += 1
victoryMiniBoss()
playerClass.hp = 100

#BEGIN TRANSITION TO BOSS FIGHT
for x in range(1):
    whichBoss = random.randint(1, 4)
    if whichBoss == 1:
        finalBoss = Klenke() 
        while finalBoss.hp > 0:
            #os.system('clear')
            playerClass.attack = playerClass.level * randrange(5,9)
            finalBoss.attack = randrange(0,2)
            miniBossFight4(playerClass.hp,finalBoss.hp,playerClass.level)
            selectionNum = input()
            if selectionNum == '1':
                finalBoss.hp = finalBoss.hp - playerClass.attack
            playerClass.hp = playerClass.hp - finalBoss.attack
            if selectionNum == '2':
                finalBoss.hp = finalBoss.hp - playerClass.attack * 2
                playerClass.diningDollars -= 50
            if playerClass.hp <= 0:
                #os.system('clear')
                lostToMiniBoss()
                quit()
            #os.system('clear')
            enemyAttacked()
            input()
        playerClass.level += 1
        victoryFinalBoss()

    elif whichBoss == 2:
        finalBoss = Motai() 
        while finalBoss.hp > 0:
            #os.system('clear')
            playerClass.attack = playerClass.level * randrange(5,9)
            finalBoss.attack = randrange(0,2)
            miniBossFight5(playerClass.hp,finalBoss.hp,playerClass.level)
            selectionNum = input()
            if selectionNum == '1':
                finalBoss.hp = finalBoss.hp - playerClass.attack
            playerClass.hp = playerClass.hp - finalBoss.attack
            if selectionNum == '2':
                finalBoss.hp = finalBoss.hp - playerClass.attack * 2
                playerClass.diningDollars -= 50
            if playerClass.hp <= 0:
                #os.system('clear')
                lostToMiniBoss()
                quit()
            #os.system('clear')
            enemyAttacked()
            input()
        playerClass.level += 1
        victoryFinalBoss()
    
    elif whichBoss == 3:
        finalBoss = Resler() 
        while finalBoss.hp > 0:
            #os.system('clear')
            playerClass.attack = playerClass.level * randrange(5,9)
            finalBoss.attack = randrange(0,2)
            miniBossFight6(playerClass.hp,finalBoss.hp,playerClass.level)
            selectionNum = input()
            if selectionNum == '1':
                finalBoss.hp = finalBoss.hp - playerClass.attack
            playerClass.hp = playerClass.hp - finalBoss.attack
            if selectionNum == '2':
                finalBoss.hp = finalBoss.hp - playerClass.attack * 2
                playerClass.diningDollars -= 50
            if playerClass.hp <= 0:
                #os.system('clear')
                lostToMiniBoss()
                quit()
            #os.system('clear')
            enemyAttacked()
            input()
        playerClass.level += 1
        victoryFinalBoss()
    
    elif whichBoss == 4:
        finalBoss = Ghosh() 
        while finalBoss.hp > 0:
            #os.system('clear')
            playerClass.attack = playerClass.level * randrange(5,9)
            finalBoss.attack = randrange(0,2)
            miniBossFight7(playerClass.hp,finalBoss.hp,playerClass.level)
            selectionNum = input()
            if selectionNum == '1':
                finalBoss.hp = finalBoss.hp - playerClass.attack
            playerClass.hp = playerClass.hp - finalBoss.attack
            if selectionNum == '2':
                finalBoss.hp = finalBoss.hp - playerClass.attack * 2
                playerClass.diningDollars -= 50
            if playerClass.hp <= 0:
                #os.system('clear')
                lostToMiniBoss()
                quit()
            #os.system('clear')
            enemyAttacked()
            input()
        playerClass.level += 1
        victoryFinalBoss()