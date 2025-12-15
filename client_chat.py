import requests
import threading
import time
import os

SEND_URL = "http://zag-sms-darack.mypressonline.com/send.php"
GET_URL  = "http://zag-sms-darack.mypressonline.com/get.php"

username = input("Your name: ")

messages_cache = []

def fetch_messages_loop():
    global messages_cache
    while True:
        try:
            r = requests.get(GET_URL)
            msgs = r.json()
            if msgs != messages_cache:
                messages_cache = msgs
                
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Chatting as: {username}\n")
                for m in msgs[-10:]:
                    print(f"[{m['time']}] {m['user']}: {m['text']}")
                print("\nType your message below:")
        except Exception as e:
            print("Error fetching messages:", e)
        time.sleep(1)

def send_message(msg):
    try:
        requests.post(SEND_URL, data={"user": username, "text": msg})
    except Exception as e:
        print("Error sending message:", e)


threading.Thread(target=fetch_messages_loop, daemon=True).start()


while True:
    msg = input("> ")
    if msg.strip():
        send_message(msg)