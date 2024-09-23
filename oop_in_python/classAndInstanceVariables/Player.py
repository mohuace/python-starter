class Player:
    teamName = "CSK" #This is a class variable (static variable) belongs to the class and common for all objects
    formerTeams = []
    teams = []
    countPlayers = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id #These two are instance variables
        #self.teamName = teamName
        #It might seem confusing why self is allowed if we are referring to class variables?
        #If we are using self, python first checks if the instance variable exists by that name
        #if not, it checks at the class level. so if you are doing some assignments using self,
        #it will create a new instance variable, but when u are trying to access using self,
        #it will first check at the instance level and then at the class level
        self.teams.append(self.name)
        Player.countPlayers = self.countPlayers + 1



player1 = Player("Suresh Raina", 3)
player2 = Player("MS Dhoni", 4)

# print(player1.teamName)
# print(player2.teamName)


#This is misleading as python creates a new instance variable teamName for player1 object which overrides the class variable
player1.teamName = "Not CSK"
print(player1.teamName)


#This still references class variable so it will print CSK
print(player2.teamName)
print(Player.teamName)
#Prints the same memory address
print(id(player2.teamName))
print(id(Player.teamName))
#But player1.teamName has a diff memory address
print(id(player1.teamName))

#This is how you update class variables
Player.teamName = "Not CSK"
#print(player1.teamName)
#print(player2.teamName)

player1.formerTeams.append("abc for p1")
player2.formerTeams.append("abc for p2")

print(player1.formerTeams)


#Printing the teams
print(player1.teams)
print(player2.teams)

print(player1.countPlayers)
print(player2.countPlayers)




