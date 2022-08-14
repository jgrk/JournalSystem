from user import *
import csv
import pandas as pd

def file_read(filedir):
    file = open(filedir, "r")
    list = []
    for line in file:
        new_line = line.strip()
        #print(new_line)
        new_line = new_line.split(",")
        #print(new_line)
        user = User(new_line[0], new_line[1], new_line[2], new_line[3], new_line[4])
        list.append(user)
    file.close
    return list

def login(userlist):
    mail = input("ange din mail: ")
    losen = input("ange lösen: ")
    for user in userlist:
        if str(mail) == str(user.mail) and str(losen) == str(user.losen):
            return user
    return None 

def menu(list):
    pass

userlist = file_read("/Users/erikduvander/Documents/JournalSystem/tests/userlist.txt")

Användare = login(userlist)


Användare.open_journal()







print(userlis)




