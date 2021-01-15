import requests #modul za komunikaciju
import json

ime = input("Unesi ime: ")

response = requests.get("https://api.agify.io/?name={ime}")

if response.status_code == 200:
    textr = response.text
    data = json.loads(textr)
    print(f"Korisnik {data['name']} ima {data['age']} godina")
else:
    print("Dogodila se pogrješka!")

print(response.text)
print(response.status_code)
print(response.raw)
