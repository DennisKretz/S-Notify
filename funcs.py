import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
from vars import *

def get_web_content():
    req = requests.get(website_url)
    web_content = req.content
    return web_content

def check_if_keys_available(content):
    scraper = BeautifulSoup(content, 'html.parser')
    for key in scraper.find_all('span', {'class': 'tag'}):
        element = key.find('i').getText()
        if (element == 'key'):
            keys = key.getText()
            if ('0' not in keys):
                keys = keys.replace('key', '')
                print("A giveaway is running right now!")
                return keys

def start_notify(keys, option):
    if (option == 1):
        start_windows_notify(keys)

def start_windows_notify(keys):
    notify = ToastNotifier()
    notify.show_toast (
        "A S&Box Giveaway is active!",
        "keys: "+ str(keys) +"",
        duration = 20,
        threaded = True,
    )

def settings():
    print("[1] windows notify")
    option = input("Please enter a option, this is for the notify: ")
    if (option == str(1)):
        return 1
    else:
        print("wrong option - try again")
        settings()