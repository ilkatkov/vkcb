while True:
    try:
        while True:
            try:
                messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
                if messages["count"] >= 1:
                    id = messages["items"][0]["last_message"]["from_id"]
                    user_word = messages["items"][0]["last_message"]["text"]