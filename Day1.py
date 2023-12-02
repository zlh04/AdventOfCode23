import re


total=0

#for line in list
for line in open('file.txt'):
    #get first and last int
    digits = re.findall('([0-9])\b(?:(?:zero|one|two|three|four|five|six|seven|eight|nine)(?: +|$))', line)
    first = str(digits[0])
    last = str(digits[-1])
    #concate
    number=int(first+last)
    #add to total
    total= total+number
print(total)