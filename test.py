import OurLib
import sys

fileName = sys.argv[1]
table = []
f = open(fileName, 'r')
for i in f:
    table.append(i)

print(table)

f.close()