#! /usr/bin/python

""" MonsterOnAGrid.py

    An eighties-era DOS-style text game. There is a human,
    a monster, and a door.  Steer the human to the door
    before it is killed by the monster.
    (Runs in Python 2.)
"""

import random
import os

# Set the grid size here manually
grid_width = 20
grid_height = 20

xcoords = list(range(grid_width))
ycoords = list(range(grid_height))
breadcrumbs = []
monsterpath = []
monster = (0, 0)
center = int(len(xcoords)/2 +1)


def header():
    print center*" " + "MONSTER ON A F'N GRID\n"


def message():
    os.system('clear')
    header()
    print "    You are a human, 'H', on a grid with a terrible monster, 'M'."
    print "    You try to find the door to escape before he subjects you to a terrible death."
    print "    You leave breadcrumbs '*' that mark where you've been.\n"
    raw_input("Press <return> to continue")


def init_game():
    human = (random.choice(xcoords), random.choice(ycoords))
    #print("Human is at {}".format(human))

    monster = (random.choice(xcoords), random.choice(ycoords))
    #print("Monster is at {}".format(monster))

    door = (random.choice(xcoords), random.choice(ycoords))
    #print("The door is at {}".format(door))
    return(human, monster, door)


def print_hidden():
    gridheader = "   "
    for k in xcoords:
        gridheader += " " + str(k)
        if k < 10:
            gridheader += " "
    print gridheader
    for j in ycoords:
        line = str(j) + " "
        if j < 10:
            line += " "
        for i in xcoords:
            if (i, j) == human:
                line += " H "
            elif (i, j) == monster:
                line += " M "
            elif (i, j) == door:
                line += " D "
            elif (i, j) in breadcrumbs:
                line += " * "
            elif (i, j) in monsterpath:
                line += " + "
            else:
                line += " . "
        print line


def print_board(xcoords, ycoords, human, breadcrumbs):
    #global monster
    header()
    gridheader = "   "
    for k in xcoords:
        gridheader += " " + str(k)
        if k < 10:
            gridheader += " "
    print gridheader
    for j in ycoords:
        line = str(j) + " "
        if j < 10:
            line += " "
        for i in xcoords:
            if (i, j) == human:
                line += " H "
            elif (i, j) == monster:
                line += " M "
            elif (i, j) in breadcrumbs:
                line += " * "
            else:
                line += " . "
        print line


def legit_move(point):
    if point[0] not in xcoords or point[1] not in ycoords:
        raw_input(" That direction is not on the grid!!! Try again. (press <return>) ")
        return False
    return True


def found_the_door(nextmove):
    if nextmove == door:
        return True
    return False


def human_move(human):
    breadcrumbs.append(human)
    while True:
        print "\n Your move, human."
        move = str(raw_input(("\n l (left), r (right), u (up), d (down), q (quit): ")))
        if move == "r":
            nextmove = (human[0]+1, human[1])
            return nextmove
        elif move == "l":
            nextmove = (human[0]-1, human[1])
            return nextmove
        elif move == "u":
            nextmove = (human[0], human[1]-1)
            return nextmove
        elif move == "d":
            nextmove = (human[0], human[1]+1)
            return nextmove
        elif move == "q":
            print " \nQuitter.\n"
            exit()
        else:
            print "That is not an option.  Either move 'l', 'r', 'u', 'd'."
            raw_input("hit <enter>")
            continue


def monster_move(newmove):
    if newmove == monster:
        death()
        return True
    if monster[0] < newmove[0]:
        monstergoes = (monster[0] +1, monster[1])
    elif monster[0] > newmove[0]:
        monstergoes = (monster[0] -1, monster[1])
    elif monster[1] < newmove[1]:
        monstergoes = (monster[0], monster[1] +1)
    elif monster[1] > newmove[1]:
        monstergoes = (monster[0], monster[1] -1)
    monsterpath.append(monster)
    monster = monstergoes
    if newmove == monster:
        death()
        return True
    return False


def death():
    os.system('clear')
    header()
    print_hidden()
    print "\nYou have died an unnaturally gruesome death at the hands of the monster!!!\n"
    print "Better luck next time.\n "
    return


def escape():
    os.system("clear")
    header()
    print_hidden()
    print "\nYou found the door!!!"
    print " You are miraculously saved from ingestion by a terrible monster.\n"
    print "You won't be so lucky next time...\n"
    return()



# MAIN()
#

message()
(human, monster, door) = init_game()
dead = False

while not dead:

    os.system("clear")
    print_board(xcoords, ycoords, human, breadcrumbs)

    nextmove = human_move(human)

    if not legit_move(nextmove):
        continue
    if found_the_door(nextmove):
        escape()
        exit()

    dead = monster_move(nextmove)
    human = nextmove

