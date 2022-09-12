from funcs import *
import datetime
import time

def launch_client(): #NOTE maybe add an option here to launch the webserver later instead of force launching it
    print("Running Client") 
    while True:
        time.sleep(10)
        check_giveaway()

def check_giveaway():
    web_content = get_web_content()
    keys = get_keys(web_content)

    if (keys):
        print("####################### " + str(datetime.datetime.now()) + " " + "a giveaway is active" + " #######################")
        start_windows_notify(keys)
    if (not keys):
        print(str(datetime.datetime.now()) + " " + "no giveaway running - still waiting...")

launch_client()