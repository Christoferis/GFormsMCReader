#A simple search program for the Writer script

#imports
import json
import time

#vars
participant_path = "participant_data.json"
user_data = None


#unpack the json
def unpack():
    global participant_path
    global user_data

    openobj = open(participant_path, mode='r')
    json_data = openobj.read()

    user_data = json.loads(json_data)


def get_data_discordusr(argument):
    global user_data

    #search for the dict entry using given argument
    for user in user_data:

        if not user.find(argument) and argument != "":
            output = user + " : "+  str(user_data[user])
            break
        else:
            output = "No user with this Discord Tag"
        
    return output 


def get_data_mcuser(argument):
    global user_data


    for user in user_data:
        if not user_data[user][0].find(argument) and argument != "":
            output = user + " : " + str(user_data[user])
            break
        else:
            output = "No user with this MC User"

    return output



def main():

    unpack()

    argument = input(">")

    #find the command
    if not argument.find("discord"):

        output = get_data_discordusr(argument=argument.replace("discord ", ""))
        print(output)

    elif not argument.find("mc"):

        output = get_data_mcuser(argument=argument.replace("mc ", ""))
        print(output)

    #show everything
    elif not argument.find("all"):
        global user_data

        for user in user_data:
            print(user + " : " + str(user_data[user]) + "\n")

    elif not argument.find("exit"):

        print("exiting...")
        time.sleep(1)
        exit()
    
    else:

        print("No argument found")
        pass

    main()


#call main
main()