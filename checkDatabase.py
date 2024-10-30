import requests
import os
import json
listDatabase = [
    {
        "name": "tomarket",
        "url": "https://raw.githubusercontent.com/DMQuan03/database/refs/heads/main/tomarket.json"
    },
    {
        "name": "paws",
        "url": "https://raw.githubusercontent.com/DMQuan03/database/refs/heads/main/paws.json"
    },
    {
        "name": "cryptoRank",
        "url": "https://raw.githubusercontent.com/DMQuan03/database/refs/heads/main/cryptoRank.json"
    }
]

while True:
    os.system("cls")
    print("_____MENU_____")
    for i in range(0, len(listDatabase)):
        print(f"{i}. {listDatabase[i]['name']}")
    print("_______________")
    option = int(input("check database : "))
    data = requests.get(listDatabase[option]['url'])
    result = data.json()
    keys = list(result.keys())
    print(keys[0])
    for i in range(0, len(keys)):
        print(result[keys[i]])
    input("enter continue")
