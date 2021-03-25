
import sys
import json

# FUNCTIONS
def list_commands():
    print('N: move north')
    print('E: move east')
    print('S: move south')
    print('W: move west')
    print('Q: quit game')

def print_directions(room_name:str):
    room = rooms_data[room_name]
    n = room['north'] is not ''
    s = room['south'] is not ''
    e = room['east'] is not ''
    w = room['west'] is not ''
    out = ''
    if n:
        out = out + "N"
    if s:
        out = out + "S"
    if e:
        out = out + "E"
    if w:
        out = out + "W"
    print('You may go: {}'.format(out))

def command_to_dir(command:str):
    if command == 'w' or command == 'W':
        return "west"
    if command == 'e' or command == 'E':
        return "east"
    if command == 's' or command == 'S':
        return "south"
    if command == 'n' or command == 'N':
        return "north"
    return "ERROR"

def print_room(room_name:str):
    print('You are in room \'{}\''.format(room_name))
    room = rooms_data[room_name]
    print(room['entry'])
    print_directions(room_name)

def enter_room(old_room:str,direction:str):
    room = rooms_data[old_room]
    print(room)
    return room[command_to_dir(direction)]


# READ ROOMS
with open('rooms.json','r') as f:
    rooms_data = json.load(f)

# INTRO
print("Welcome!")
print("What is your name?")
player_name = input() 
print("Well, hello there {}!".format(player_name))

# ROOMS
print("You face North. Before you lies a door.")
command = 'N'
options = { 'n','N','s','S','e','E','w','W' }
quit_options = { 'q','Q'}
current_room = "A"
while command not in quit_options:
    print('Enter the direction you would like to go:')
    command = input()
    
    if command not in options:
        print("I don't know what you mean.")
        list_commands()
        continue
    current_room = enter_room(current_room, command)
    print_room(current_room)
    


print('Goodbye {}!'.format(player_name))





