# example
# Made by VKCB

import vk_api
import json
import random

token = "example-api-key" # api-key
vk = vk_api.VkApi(token=token)
vk._auth_token()

def get_button(label, color, payload=''):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {"one_time": False, "buttons": [[get_button(label = 'first_meassage', color = 'default')],[get_button(label = 'second_message', color = 'default')]]}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

print("\n---VKCB---")
print("example: ON")

while True:
    try:
        while True:
            try:
                messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
                if messages["count"] >= 1:
                    id = messages["items"][0]["last_message"]["from_id"]
                    user_word = messages["items"][0]["last_message"]["text"]
                    if user_word.lower() == "first_message":
                        vk.method("messages.send", {"peer_id": id, "message": "message", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                    elif user_word.lower() == "second_message":
                        vk.method("messages.send", {"peer_id": id, "message": "message", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "message", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
            except Exception as message_exception:
                print(message_exception)
    except Exception as message_exception:
        print(message_exception)
