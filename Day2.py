games={}
colItem = []

for line in open('file2.txt'):
     game, items = line.split(":")
     item = items.split(";")
     for eachChoice in item:
         singleChoice = eachChoice.split(",")
         for choice in singleChoice:
            i, ColNum, ColNam = choice.split(" ")
         dictChoice = {ColNam:ColNum}
     games.update({game:dictChoice})
     
    #         colItem.append(choice)
    #  for colour in colItem:
    #      ColNum, ColNam = colour.split(" ")
    #      games.update({game:{ColNam:ColNum}})
     #at this point we have game which has the name of the game, and colItem which has a list of values
print(games)
# print(games)

# print(games)

#     game, list = line.split(":")
#     gameTitle, gameNum = game.split(" ")

#     # game, item1, item2, item3, item4, item5= line.split(",")
#     games.update(line)
#     print(games)