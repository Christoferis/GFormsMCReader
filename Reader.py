#Reader for CSV Files, specifically for the MC All Stars and Titan Projects
#Collums in question: B, C, D
# 2 and down

#Notes:
#Duplicates (Server) and Name herausfischen
#second script for looking up the MC Username and infos


#Imports
import csv
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


def whitelist_and_participants():
    global participants
    global whitelist_path
    global max_players

    #open whitelist
    openobj = open(whitelist_path, mode='w')
    saveobj = list()
    delete_entries = list()

    #get minecraft names and uuids

    for player in participants:
        #get the user entry
        data = participants[player]

        #create whitelist container for every person
        container = {
            "uuid": uuid_formatter(mj.MojangAPI.get_uuid(data[0])),
            "name": data[0],
        }

        #failsafe pt 2, false minecraft name = invalid
        if container["uuid"] != None:
            saveobj.append(container)

        else:
            #append and delete later
            delete_entries.append(player)

    #delete invalid entries
    for delete in delete_entries:
        del participants[delete]


    #8 player limit : whitelist
    for place in range(len(saveobj) - 1):
        if place + 1 >= max_players:
            print(saveobj.pop(place))

    #8 player limit : participants
    iter = 0
    delete_entries = list()
    for player in participants:

        if iter >= max_players:
            delete_entries.append(player)

        iter += 1

    for delete in delete_entries:
        del participants[delete]


        
    #dump json in file
    openobj.write(json.dumps(saveobj, indent=4))

    print("changed whitelist")
    openobj.close()
    pass


def save_json():
    pass


def csv_to_dict():
    global csvpath
    global participants

    openobj = open(csvpath, newline='', mode='r')

    csvobj = csv.reader(openobj, delimiter=',')

    #convert to a list
    iter = 0

    for row in csvobj:
        #dont include first row (questions)
        if iter != 0:
            participants[row[1]] = [row[2], row[3]]
        else:
            iter += 1 
            pass

    print("converted csv to dict")


def main():
    print("reading csv")

    #get
    csv_to_dict()

    #construct whitelist
    whitelist_and_participants()


main()


