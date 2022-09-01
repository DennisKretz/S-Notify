from funcs import *
import time

def launch():
    print("RUNNING...")
    option = settings()
    while True:
        time.sleep(20)
        main(option)

def main(option):
    web_content = get_web_content()
    keys = check_if_keys_available(web_content)

    if (keys):
        start_notify(keys, option)
    if (not keys):
        print("no giveaway running - still waiting...")

launch()