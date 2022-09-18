from math import ldexp
import schedule
import threading
import time
import requests

def messageThreading():
    
    def get_data():
        
        data = requests.get("http://127.0.0.1:8000/balance/beers_data")

        if data != "":
            print(data.text)
        else:
            print("Empty data")

    schedule.every(2).seconds.do(get_data)
    
    while True:
        schedule.run_pending()

print("Test 1")

# Threading part
t1 = threading.Thread(target=messageThreading)
t1.start()

#Execute the rest of the code
time.sleep(10)
print("Test 2")

