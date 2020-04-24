import time
import re
import config
from playsound import playsound
from win10toast import ToastNotifier
from pathlib import Path


def alerter(audioPath):
    boiFile = Path(audioPath)
    if boiFile.is_file():
        print("playing sound")
        playsound(audioPath)


def alerter_notif(iconPath, notif_dur):
    toaster = ToastNotifier()
    toaster.show_toast("HydrationBot💦", "Mah D U D E, you require some D R I N C C!👏 It's been " + str(alert_delay_min) + " minutes since your last sip ⌛️🌊", threaded=True, icon_path=iconPath, duration = notif_dur)
    while toaster.notification_active():
        time.sleep(0.1)


iconPath = config.iconFile
audioPath = config.audioFile
alert_delay_min = config.notifTimer['notifDelay']
alert_audio_delay_min = config.notifTimer['audioDelay']
notifDur = config.notifTimer['notifDur']
minu = 0
alerter_notif(iconPath, notifDur)
if alert_audio_delay_min >= 0:    
    while minu != alert_audio_delay_min:
        time.sleep(59)
        minu += 1
        print("One minute has passed")
        if minu % alert_delay_min == 0:
            alerter_notif(iconPath, notifDur)
            if (minu >= alert_audio_delay_min):
                alerter(audioPath)
                minu = 0
    if alert_delay_min > 0:
        while minu != alert_delay_min:
            time.sleep(59)
            minu += 1
            print("One minute has passed")
            if minu == alert_delay_min:
                alerter_notif(iconPath, notifDur)
                minu = 0
    elif alert_audio_delay_min < 0 or alert_delay_min <= 0:
        toaster = ToastNotifier()
        toaster.show_toast("HydrationBot💦", "Please ensure that the alert delays are not negative numbers and that notifDelay > 0. This can be changed in the config.py file in the directory of the program.", threaded=True, icon_path=None, duration = 10)
        while toaster.notification_active():
            time.sleep(0.1)
    else:
        toaster = ToastNotifier()
        toaster.show_toast("HydrationBot💦", "Something went horribly wrong", threaded=True, icon_path=None, duration = 10)
        while toaster.notification_active():
            time.sleep(0.1)
elif alert_audio_delay_min < 0 or alert_delay_min <= 0:
    toaster = ToastNotifier()
    toaster.show_toast("HydrationBot💦", "Please ensure that the alert delays are not negative numbers and that notifDelay > 0. This can be changed in the config.py file in the directory of the program.", threaded=True, icon_path=None, duration = 10)
    while toaster.notification_active():
        time.sleep(0.1)
else:
    toaster = ToastNotifier()
    toaster.show_toast("HydrationBot💦", "Something went horribly wrong", threaded=True, icon_path=None, duration = 10)
    while toaster.notification_active():
        time.sleep(0.1)
