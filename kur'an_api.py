import requests

sura = int(input("suraning raqamini kiriting"))
oyat = int(input("oyat raqamini kiriting"))
url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-alaaudeenmansou/{sura}/{oyat}.json"
response = requests.get(url)

if response.ok:
    print(response.json()["text"])
else:
    print("xato malumot kiritildi")
