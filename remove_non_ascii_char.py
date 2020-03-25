#!/usr/bin/env python

#This program removes non ascii characters, replacing then with "~"
#https://stackoverflow.com/questions/20078816/replace-non-ascii-characters-with-a-single-space

print("Paste string here. Hit enter, then input ';;' then hit enter again")

daString = ""
stopword = ";;"

def remove_non_ascii_1(daString):

    return ''.join([i if ord(i) < 128 else '~' for i in daString])


while True:
    line = input()
    if line.strip() == stopword:
        break
    daString += "%s\n" % line

if all(ord(char) < 128 for char in daString):
    print("All characters are ascii")

else:
    daString = (remove_non_ascii_1(daString))
    print(daString)
