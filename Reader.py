#Reader for CSV Files, specifically for the MC All Stars and Titan Projects
#Collums in question: B, C, D
# 2 and down

#Notes:
#Duplicates (Server) and Name herausfischen
#whitelist syntax
#second script for looking up the MC Username and infos


#Imports
import csv
import mojang as mj
import json


#Variables

csvpath = "The Factory All-Stars (Minecraft Event).csv"
whitelist = "whitelist.json"
participants = dict()

#format mc uuid to the 8-4-4-4-12 format
def uuid_formatter(uuid):
    listuuid = list(uuid)
    
    #add in the dashes
    listuuid.insert(8, "-")
    listuuid.insert(8+4+1, "-")
    listuuid.insert(8+4+4+2, "-")
    listuuid.insert(8+4+4+4+3, "-")
    

    final = str(listuuid).replace("[", '').replace("]", '').replace(",", '').replace("'", '').replace(" ", '')

    return final


def whitelist():
    global participants
    global whitelist
    #open whitelist
    openobj = open(whitelist, mode='w').write()
    saveobj = list()

    #get minecraft names and uuids

    for player in participants:
        #create whitelist container for every person
        container = {
            "uuid": uuid_formatter(mj.MojangAPI.get_uuid(participants.get(player)[0])),
            "name": uuid_formatter(participants.get(player)[0])
        }

        saveobj.append(container)

    print(saveobj)
        

    #dump json in file
    json.dump()
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
        #only 8 participants
        elif iter == 8:
            break
        else:
            iter += 1 
            pass

        

def main():
    print("reading csv")
    #get
    csv_to_dict()


main()


