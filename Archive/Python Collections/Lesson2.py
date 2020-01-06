# This file has a lot of errors and needs fixing

from titlecase import titlecase
import os

def stats(dictionary):
    bestList = list()
    for key,value in dictionary.items():
        bestList.append({key,len(value)})
    return bestList

something = stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],'Kenneth Love': ['Python Basics', 'Python Collections']})

#print(something)

#####################################################################

my_tuple = (1,2,3)
my_second_tuple = 1,2,3

def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total

#print(multiply(1,2,3))

course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}
for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course,minutes))

def stringcases(string):
    #my_tuple = string.upper(), string.lower(), titlecase(string), string[::-1]
    my_tuple = string.upper(), string.lower(), string.title(), string[::-1]
    return my_tuple

#print(stringcases("there is a way"))


def combo(args, kwargs):
    my_list = []
    for i in range(0, len(args)):
        my_list += (args[i], kwargs[i]),
    return my_list

#print(combo([1, 2, 3], 'abc'))

#####################################################################

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(para):
    newlist = []
    for key, value in COURSES.items():
        if value & para:
            newlist.append(key)
    return newlist

print(covers({"Python"}))



def covers_all(aset):
    names = []
    for key, value in COURSES.items():
        if value.issuperset(aset):
            names.append(key)
    return names

#####################################################################

import random

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster

CELLS = [(0,0)(1,0),(2,0),(3,0),(4,0),
         (0,1)(1,1),(2,1),(3,1),(4,1),
         (0,2)(1,2),(2,2),(3,2),(4,2),
         (0,3)(1,3),(2,3),(3,3),(4,3),
         (0,4)(1,4),(2,4),(3,4),(4,4),
    ]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    monster = None
    door = None
    player = None

    return monster, door, player

monster, door, player = get_locations()

while True:
    valid_moves = get_moves(player)
    print("Welcome to the dungeon")

    move = input("> ")
    move = move.upper()
    if move == "QUIT":
        break
    if moves in valid_:
        # some codes needs to go here
        pass

def move_player(player, move):
    x, y = player
    if move == "LEFT":
        # some codes needs to go here
        pass
    return player

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x ==0:
        moves.remove("LEFT")
    if x==1:
        moves.remove("RIGHT")
    if x==2:
        moves.remove("UP")
    if x==3:
        moves.remove("DOWN")

    return moves

#####################################################################

def move(player, direction):
    x, y, hp = player
    xmove, ymove = direction
    x += xmove
    y += ymove
    if x < 1:
        x = 0
        hp -= 5
    if y < 1:
        y = 0
        hp -= 5
    return x, y, hp

print(move((1, 1, 10), (-1, 0)))
print(move((0, 1, 10), (-1, 0)))
print(move((0, 9, 5), (0, 1)))

