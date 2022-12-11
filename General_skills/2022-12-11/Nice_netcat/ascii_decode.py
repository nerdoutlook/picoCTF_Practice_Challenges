#!/usr/bin/python3

file1 = open("file.txt", "r")

for i in file1:
    print(chr(int(i)), end="")
file1.close()
