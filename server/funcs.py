from win10toast import ToastNotifier

def start_windows_notify(keys):
    notify = ToastNotifier()
    notify.show_toast (
        "A S&Box Giveaway is active!",
        "keys: "+ str(keys) +"",
        duration = 20,
        threaded = True,
    )