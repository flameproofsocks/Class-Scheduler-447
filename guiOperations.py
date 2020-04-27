from Room import Room

def searchDB(self, keywords,searchRooms,searchEvents):
    #search db based on keywords
    #search rooms for keywords if searchRooms = 1
    #search events for keywords is searchEvents = 1
    #place correct itmes in roomList
    roomList = []

    #TESTING
    roomList.clear()
    roomTest = Room("ENG","202",200)
    roomList.append(roomTest)
    roomTest = Room("ENG","202",200)
    roomList.append(roomTest)
    #end testing

    return roomList