#!/usr/bin/python
import getpass
import sys

lang = sys.argv[1]
username = getpass.getuser()


print("Hello {}!".format(username))
if lang == "All":
	print("You chose to execute all languages, what a curious!")
else:
    print("You chose to execute {}, Great choise!".format(lang))


with open("hello.txt", "w") as f:   
    f.write("Hello World")
