from server.funcs import *
from server.giveawayInfo import *
import datetime
import time

def launch_client(): #NOTE maybe add an option here to launch the webserver later instead of force launching it
    print("Running Client") 
    while True:
        time.sleep(10)
        check_giveaway()

def check_giveaway():
    giveaway_obj = GiveawayInfo()
    webcontent = giveaway_obj.get_web_content()
    keys = giveaway_obj.get_keys(webcontent)

    if (keys and '0' not in keys):
        print("####################### " + str(datetime.datetime.now()) + " " + "a giveaway is active" + " #######################")
        start_windows_notify(keys)
    else:
        print(str(datetime.datetime.now()) + " " + "no giveaway running - still waiting...")
        

launch_client()