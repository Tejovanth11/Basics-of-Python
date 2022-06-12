import re
fname = open("regex_sum_1524718.txt")
x=list()
for line in fname:
     f = re.findall('[0-9]+',line)
     x = x+f
sum=0
for z in x:
    sum = sum + int(z)
print(sum)