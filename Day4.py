
points = 0
total = 0
overall =0
for line in open("file4.txt"):
    correct = 0
    card, values = line.split(":")
    mine, winners = values.split("|")
    MyValues = mine.split(",")
    WinValues = winners.split(",")
    for value in WinValues:
        for value in MyValues:
            correct = correct+1
    points = correct*2
total = total+points
print(total)