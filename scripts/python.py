#!/usr/bin/python
import getpass

username = getpass.getuser()


print("Hello", username)
if LANGUAGE == "All":
	print("You chose to execute all languages, what a curious!")
else:
    print("You chose to execute ", LANGUAGE, " Great choise!")


with open("hello.txt", "w") as f:   
    f.write("Hello World")
