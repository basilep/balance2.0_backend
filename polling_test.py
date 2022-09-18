import schedule
import threading
import time
def get_souye():
    print("souye")
def get_xeu():
    print("xeu")
def get_ha():
    print("pute")

def thread_polling():
    schedule.every(1).seconds.do(get_souye)
    schedule.every(1.5).seconds.do(get_xeu)
    #schedule.every().day.at("12:21").do(get_ha)
    while True:
        schedule.run_pending()

print("Je suis là")
t1 = threading.Thread(target=thread_polling)
t1.start()
time.sleep(10)
print("Moi aussi")

