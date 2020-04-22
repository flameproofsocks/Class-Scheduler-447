from Room import Room

def searchDB(self,guiItem, keywords,searchRooms,searchEvents,sTime,eTime):
    #search db based on keywords
    #search rooms for keywords if searchRooms = 1
    #search events for keywords is searchEvents = 1
    #place correct itmes in roomList
    roomList = []

    #TESTING
    roomTest = Room("BIO","101",200)
    roomList.append(roomTest)

    guiItem.buildItems(roomList,sTime,eTime)