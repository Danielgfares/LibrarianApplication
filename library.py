from room import Room

class Library():
    name=""
    rooms = dict()
    
    def __init__(self, name=""):
        self.name = name
        
    def getName(self):
        return self.name
    
    def addRoom(self, room):
        self.rooms[room.getName()] = room
        
    def removeRoom(self, roomName):
        if (roomName in rooms):
            del rooms[roomName]
    
    def getRoom(self, roomName):
        if (roomName in self.rooms):
            return self.rooms[roomName]
        else:
            room = Room(roomName)
            self.rooms[roomName] = room
            return room

    def __str__(self):
        return list(self.rooms.keys()).__str__()