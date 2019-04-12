#Global import
import sys
import random
class House():
    def __init__(self, settings):
        self.items = {}
        self.rooms = {}
        self.doors = [] 
        self.start = None
        with open(settings) as config:
            Hdescription = [line.rstrip('\n') for line in config]
            Hdescription = [line.split(' ') for line in Hdescription]
            for i in range(len(Hdescription)):
                if Hdescription[i][0] == 'room':
                    self.rooms[Hdescription[i][1]] = None
                    self.items[Hdescription[i][1]] = []
                elif Hdescription[i][0] == 'door':
                    self.doors.append(Door(Hdescription[i][1],Hdescription[i][2],(Hdescription[i][3], Hdescription[i][4])))
                elif Hdescription[i][0] == 'item':
                    if Hdescription[i][3] == 'STATIONARY':
                        self.items[Hdescription[i][2]].append(Item(Hdescription[i][1]))
                    elif Hdescription[i][3] == 'USE':
                        self.items[Hdescription[i][2]].append(Useable(Hdescription[i][1]))
                    elif Hdescription[i][3] == 'READ':
                        self.items[Hdescription[i][2]].append(Useable(Hdescription[i][1]))
                    elif Hdescription[i][3] == 'MOVE':
                        self.items[Hdescription[i][2]].append(Moveable(Hdescription[i][1]))
                elif Hdescription[i][0] == 'start':
                    self.start = Hdescription[i][1]
        for room in self.rooms:
            self.rooms[room] = []
            for door in self.doors:
                 if str(door).startswith(room):
                     self.rooms[room].append((door, door.Wall()[0]))
                 elif str(door).endswith(room):
                     self.rooms[room].append((door, door.Wall()[0]))
            self.rooms[room] = Room(room, self.rooms[room], self.items[room])

    def getRooms(self):
        return self.rooms

    def getStart(self):
        return self.start

class Game():
    def __init__(self, house, player):
        self.player = player
        self.rooms = house.getRooms()
        self.curr = house.getStart()
        self.CCommands = ['go', 'open', 'unlock']
        self.itemCommand1 = {'take' : 'self.rooms[self.curr].takeItem(command[1], self.player.getHolding())'}
        self.itemCommand2 = {'release' : 'self.rooms[self.curr].relItem(command[1], self.player.getHolding())'}
        self.allCommands = {'show' : 'self.rooms[self.curr].HouseDes()',  'holding' : "print(self.player.getHolding())", \
                'commands' : "print('go,', 'take Item,', 'release Item,', 'show,',\
                 'holding,','commands and', 'quit')", 'quit' : "print('Good bye and thanks for playing!')"}

    def init(self):
        while True:
            command = input('>>  ')
            command = command.split(' ', 1)

            if command[0] in self.CCommands:
                if len(command) >=2:
                    if command[1] not in [door[1] for door in self.rooms[self.curr].getDoors()]:
                        print("There is no door in this direction!")
                    else:
                        for door in self.rooms[self.curr].getDoors():
                            if command[1] == door[1] and door[0].getStatus() == 'open':
                                if command[0] == 'go':
                                    for link in door[0].getneighbour():
                                        if link != self.curr:
                                            self.curr = link
                            elif command[1] == door[1] and door[0].getStatus() == 'closed':
                                if command[0] == 'go':
                                    print('The door is closed, you can open it with open command.')
                                elif command[0] == 'open':
                                    door[0].openDoor()
                            elif command [1] == door[1] and door[0].getStatus() == 'locked':
                                if command[0] == 'go' or command[0] == 'open':
                                    print('The door is locked and a key is required to unlock it.')
                                elif command[0] == 'unlock':
                                    door[0].unlockDoor(self.player.getHolding(),door[0])
                else:
                    print('Please enter the direction:')
        
            elif command[0] in self.itemCommand1:
                if len(command) > 3:
                    exec(self.itemCommand1[command[0]])
                else:
                    print('Please enter the name of item you want to take:')
        
            elif command[0] in self.itemCommand2:
                if len(command) > 3:
                    exec(self.itemCommand2[command[0]])
                else:
                    print('Please enter the name of item you want to release:')

            elif command[0] in self.allCommands:
                exec(self.allCommands[command[0]])
        
            else:
                print('Please use the valid command, you can see the list of valid ones with commands.')
class Player():
    def __init__(self):
        self.holdings = []
    
    def getHolding(self):
        return self.holdings

class Room():
    def __init__(self, name, doors, items):
        self.name = name
        self.doors = doors
        self.items = items

    @property
    def __str__(self):
        return string

    def __repr__(self):
        return str(self)

    def getName(self):
        return self.name

    def getDoors(self):
        return self.doors

    def HouseDes(self):
        if self.name == 'Hall':
            print('You are in the hall, there is a book in this room. Take it and enjoy it!')
            doorS = 'Here are doors towards: '
            for door in self.doors:
                doorS = doorS + door[1] + '  '
            print(doorS)
        if self.name == 'Kitchen':
            print('You are in the Kitchen, there is no item here.')
            doorS = 'Here are doors towards: '
            for door in self.doors:
                doorS = doorS + door[1] + '  '
            print(doorS)
        if self.name == 'Storage':
            print('You are in the Storage room, there is a heavy box on the corner which your can not lift it.')
            doorS = 'Here are doors towards: '
            for door in self.doors:
                doorS = doorS + door[1] + '  '
            print(doorS)
        if self.name == 'Bedroom':
            print('You are in the Bedroom, there is a bed behind you which you can not move it.')
            doorS = 'Here are doors towards: '
            for door in self.doors:
                doorS = doorS + door[1] + '  '
            print(doorS)
        if self.name == 'Dinning':
            print('You are in the Dinning room, there is an interesting novel just behind you. Take it and enjoy it!')
            doorS = 'Here are doors towards: '
            for door in self.doors:
                doorS = doorS + door[1] + '  '
            print(doorS)
        if self.name == 'Bathroom':
            print('You are in the Bathroom, there is a key here to unlok the door toward storage in N direction or go in W direction without key.')
            doorS = 'Here are doors towards: '
            for door in self.doors:
                doorS = doorS + door[1] + '  '
            print(doorS)
        elif len(self.doors) == 1:
             print('There is one door in the direction')



    def relItem(self, item, holdings):
        for item1 in holdings:
            if item1.getName() == item:
                holdings.remove(item1)
                self.items.append(item1)
                print(item, " is released.")
        print("No item to release.")
        
    def takeItem(self, item, holdings):
            for item1 in self.items:
                if item1.getName() == item:
                    if item1.Move() == False and item1.Use()== False:
                        print('Sorry, you can not move or take this item!')
                    else:
                        if item1.Move() == True or item1.Use()== True:
                            self.items.remove(item1)
                            holdings.append(item1)
                            print('You took the', item)
                        return holdings
            print('There is no item in this room.')

 

class Item():
    def __init__(self, name):
        self.name = name
        self.move = False
        self.use= False
    @property
    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def setName(self, itemname):
        self.name = itemname

    def getName(self):
        return self.name

    def Move(self):
        return self.move
    def Use(self):
        return self.use
#Inheritance 

class Moveable(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        self.move = True

class Useable(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        self.use = True

        
class Door():
    def __init__(self, wall, status, neighbours):
        self.wall = wall
        self.status = status
        self.neighbours = neighbours

    def __str__(self):
        string = "{} - {}".format(self.neighbours[0],self.neighbours[1])
        return string

    def __repr__(self):
        return str(self)

    def Wall(self):
        return self.wall

    def getStatus(self):
        return self.status

    def getneighbour(self):
        return self.neighbours
    
    def openDoor(self):
        if self.status == 'closed':
            self.status = 'open'
            print('The door is open.')
  
    def unlockDoor(self, holdings,door):
        if self.status == 'locked':
            for item in holdings:
                if 'key' in item.getName():
                    self.status = 'open'
                    print('The door is unlocked!')
      
    



print('********Hello, welcome to my house game********')
print('There are six rooms in this house, each room has special item.')
print('You can move into different directions, take different items and explore my house.')
print('To see all possible commands, please type command, to exit the game type quit and to see the description of each room type show.')
print('Please type commands in order to play the game!')
#game = Game(House(sys.argv[1]), Player())
game = Game(House('HD.txt'), Player())
game.init()
