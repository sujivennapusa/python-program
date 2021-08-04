import json
import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=10c19b8f37514a3c90f433b420a45343")
""" print(data.text) """
extracteddata=data.json()
""" print(extracteddata) """
""" print(extracteddata["status"]) """
print(extracteddata["articles"])
articles=extracteddata["articles"]
for i in articles:
    print(i["title"])