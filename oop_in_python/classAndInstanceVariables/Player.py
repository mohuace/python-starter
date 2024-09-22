class Player:
    teamName = "CSK" #This is a class variable (static variable) belongs to the class and common for all objects
    formerTeams = []

    def __init__(self, name, id):
        self.name = name
        self.id = id #These two are instance variables
        #self.teamName = teamName



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




