#if want to use this plz add numbers after the command
#for example
#python ex14.py X X X
#X=numbers
from sys import argv

script,first,second,third = argv
first=raw_input("can you write down first?")
second=raw_input("can you write down second?")
third=raw_input("can you write down third?")
print "the script is called:", script
print "your first variable is:", first
print "your second variable is:", second
print "your third variable is:", third
