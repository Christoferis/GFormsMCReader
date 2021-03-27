#Reader for CSV Files, specifically for the MC All Stars and Titan Projects
#Collums in question: B, C, D
# 2 and down

#Notes:
#Duplicates (Server) and Name herausfischen
#whitelist syntax
#second script for looking up the MC Username and infos


#Imports
import csv
import mojang
import json


#Variables

csvpath = "The Factory All-Stars (Minecraft Event).csv"
whitelist = "whitelist.json"
participants = dict()

def whitelist():
    global participants
    global whitelist
    #open whitelist
    openobj = open(whitelist, mode='w').read()
    jsonobj = json.load(fp=openobj)


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
    
    print(participants)

        

def main():
    print("reading csv")
    #get
    csv_to_dict()


main()
