
'''
❓ PROMPT
In some interview settings, you won't be allowed to run you're code. In an in person interview (they still happen sometimes!) you might be required to write your code on a whiteboard. Some companies emulate this in a remote setting by giving you a shared editor without a runtime environment, just a plain text editor. For this problem, we're going to emulate this.

In a role playing game, our band of intrepid adventurers must escape a dungeon.  They've been dropped into a room somewhere without a map, so must explore the rooms as they encounter them.

You'll be given an instance of this Dungeon clas:

class Dungeon:
  // This gets the label of the room where the adventurers start
  +getStartingLocation(): number
  // Returns the list of rooms accessible from the given one
  +getNextRooms(location): list[number]
  // Is this room an exit?
  +isExit(location)

Your task is to use this instance to explore and find the room number (label) of the exit.

Since an implementation of this class isn't provided, you'll have to write your code given this interface. You COULD write your own Dungeon class and test this (and I recommend this!) but please write this code first without running it.

Example(s)
No example is provided. You have to trust that the Dungeon class does what it is supposed to! This function will be called after creating an instance of the Dungeon class.
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function escapeDungeon(dungeon)
def escape_dungeon(dungeon):

 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
'''
class Dungeon:
  // This gets the label of the room where the adventurers start
  +getStartingLocation(): number
  // Returns the list of rooms accessible from the given one
  +getNextRooms(location): list[number]
  // Is this room an exit?
  +isExit(location)
'''

class Dungeon:
    def __init__(self):
        self.location = 0
        pass
    def getStartingLocation(self):
        pass
    def getNextRooms(self, location):
        pass
    def isExit(self, location):
        pass

def escape_dungeon(dungeon):

    dungeon = Dungeon()
    visited = set()

    def dfs(location):

        if dungeon.isExit(location):
            return location

        rooms = dungeon.getNextRooms(location)

        for room in rooms:
            if room in visited:
                continue
            return dfs(room)
             
    return dfs(dungeon.getStartingLocation())
        