import requests


def send_telegram(text: str):
    token = "5977884733:AAGnFPmmNfvHsDxclaM5mhKmYfCf0C9dSVQ"
    chat_id = "207721952"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

    

    
 

