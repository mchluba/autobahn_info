import requests

class TelegramBot():
    def __init__(self, api_token, chat_id):
        self.api_token = api_token
        self.chat_id  = chat_id

    def sendMessage(self, dataset):
        if dataset[6] == "True":
            blocked = "Ja"
        else:
            blocked = "Nein"

        telegram_message_uri = "https://api.telegram.org/bot" + self.api_token + "/sendMessage"
        telegram_location_uri = "https://api.telegram.org/bot" + self.api_token + "/sendLocation"
        telegram_message = {
            "chat_id" : self.chat_id,
            "text" : "NEUE VERKEHRSMELDUNG \n" + dataset[7]
        }
        telegram_location = {
            "chat_id" : self.chat_id,
            "latitude" : dataset[3],
            "longitude" : dataset[4]
        }
        requests.post(url=telegram_message_uri, data=telegram_message)
        requests.post(url=telegram_location_uri, data=telegram_location)
        print (telegram_message)
        print (telegram_location)