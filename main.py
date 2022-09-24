import re

textfile = open('fb_sub.csv', 'r')
filetext = textfile.read()

re.search(r'\w*\sINC\b',filetext)[0]

print(re.search(r'\w*\sINC\b',filetext)[0])

match = re.search(r'\w*\sINC\b',filetext)[0]
fileout = open("company.txt", "w")

fileout.write(match)




   