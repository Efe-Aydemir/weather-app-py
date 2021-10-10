import requests
import json
import time



while True:
    print("-- Hava Durumu App --")

    print("_"*31)

    sehir = input("Şehir: ")

    sehir.capitalize()

    r2 = requests.get(f"http://api.weatherapi.com/v1/current.json?key=e8d78d472edb4333888101025210910&q=Turkey/{sehir}&aqi=no")

    res2 = r2 .text

    data2 = json.loads(res2)

    derece2 = data2["current"]["temp_c"]
    sehir2 = data2["location"]["name"]


    print(f"Şehir: {sehir2}\nDerece: {derece2} ")

    soru = input("Program Devam Ettirilsinmi (y/n): ")

    if soru == "y":
        print("_"*31)
        continue
    else:
        print("Çıkış Yapılıyor....")
        time.sleep(5)
        break
