#Reader for CSV Files, specifically for the MC All Stars and Titan Projects
#Collums in question: B, C, D
# 2 and down

#Notes:
#Duplicates (Server) and Name herausfischen
#whitelist syntax
#second script for looking up the MC Username and infos
#add in 8 Player barrier


#Imports
import csv
from typing import Type
import mojang as mj
import json


#Variables
max_players = 8

csvpath = "The Factory All-Stars (Minecraft Event).csv"
whitelist_path = "whitelist.json"
participants = dict()


#format mc uuid to the 8-4-4-4-12 format
def uuid_formatter(uuid):
    #failsafe pt 1 if no player with that name
    try:
        listuuid = list(uuid)
        
        #add in the dashes
        listuuid.insert(8, "-")
        listuuid.insert(8+4+1, "-")
        listuuid.insert(8+4+4+2, "-")
        listuuid.insert(8+4+4+4+3, "-")
        

        final = str(listuuid).replace("[", '').replace("]", '').replace(",", '').replace("'", '').replace(" ", '')
    except TypeError:
        final = None

    return final


def whitelist():
    global participants
    global whitelist_path

    #open whitelist
    openobj = open(whitelist_path, mode='w')
    saveobj = list()

    #get minecraft names and uuids

    for player in participants:
        #get the user entry
        data = participants[player]

        #create whitelist container for every person
        container = {
            "uuid": uuid_formatter(mj.MojangAPI.get_uuid(data[0])),
            "name": data[0],
        }

        #failsafe pt 2
        if container["uuid"] != None:
            saveobj.append(container)

        
    #dump json in file
    json.dump(fp=openobj, obj=saveobj)
    openobj.close()
    pass


def save_json():
    pass


def csv_to_dict():
    global csvpath
    global participants
    global max_players

    openobj = open(csvpath, newline='', mode='r')

    csvobj = csv.reader(openobj, delimiter=',')

    #convert to a list
    iter = 0

    for row in csvobj:
        #dont include first row (questions)
        if iter != 0:
            participants[row[1]] = [row[2], row[3]]
        #only 8 participants
        elif iter == max_players:
            break
        else:
            iter += 1 
            pass


def main():
    print("reading csv")

    #get
    csv_to_dict()

    #construct whitelist
    whitelist()


main()


