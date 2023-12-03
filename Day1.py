import re


total=0

#for line in list
for line in open('file1.txt'):
    #get first and last int
    digits = re.findall('([0-9])', line)
    first = digits[0]
    last = digits[-1]
    #concate
    number=int(first+last)
    #add to total
    total= total+number
print(total)