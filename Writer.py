#Reader and Writer between  CSV and Json Files, specifically for the MC All Stars and Titan Projects
#Christoferis c 2021



#Imports
import csv
import mojang as mj
import json
import time
import random


#Variables
max_players = 8

csvpath = "The Factory All-Stars (Minecraft Event).csv"
whitelist_path = "whitelist.json"
participants = dict()
participant_path = "participant_data.json"


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
    all_players = list()

    #get all users and compile a list
    for player in participants:
        all_players.append(player)

    final_participants = dict()

    #make it as long as finalparticipants isnt 8 in length + uuid check


    while True:
        player = random.choice(all_players)

        data = participants[player]

        #create mc entry
        container = {
            "uuid": uuid_formatter(mj.MojangAPI.get_uuid(data[0])),
            "name": data[0],
        }

        #check if mc account exists and if player isnt already in list
        if player not in final_participants and container["uuid"] != None:
            saveobj.append(container)
            final_participants[player] = participants[player]

        #check if finalparticipants already 8
        if len(final_participants) == 8:
            #make final participants list all pariticipant list and exit
            participants = final_participants
            break


    #get minecraft names and uuids


    print("Player cap added")

    #dump json in file
    openobj.write(json.dumps(saveobj, indent=4))

    print("changed whitelist")
    openobj.close()
    pass

#json serialization of final info of all contestants 
def save_json():
    global participant_path
    global participants

    #open the data file and dump the dict in there
    openobj = open(participant_path, mode="w")

    openobj.write(json.dumps(participants, indent=4))

    openobj.close()
    
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
            participants[row[1].replace(" ", "")] = [row[2], row[3]]
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

    #save final participation list
    save_json()

    print("done")

    print("terminate in 1 sec")
    time.sleep(1)


#execute main function
main()

