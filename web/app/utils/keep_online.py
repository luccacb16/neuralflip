import schedule
import requests
import time
import threading
import os

def ping():
    def req():
        try:
            response = requests.get(os.environ.get('URL') + '/ping')
            print(response)
        except requests.RequestException as e:
            print(f"Erro na solicitação: {e}")

    schedule.every(14).minutes.do(req)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
def keep_online():
    thread = threading.Thread(target=ping)
    thread.daemon = True
    thread.start()