import requests
import time
import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

PRODUCTOS = {
    "Target": https://www.target.com/p/2025-pok-me-2-5-elite-trainer-box/-/A-95082118,
    "Walmart": https://www.walmart.com/ip/Pok-mon-Trading-Card-Game-Mega-Evolution-Ascended-Heroes-Elite-Trainer-Box/18710966734?conditionGroupCode=4&classType=REGULAR&athbdg=L1103&from=/search
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def enviar_mensaje(texto):
    data = {"content": texto}
    requests.post(WEBHOOK_URL, json=data)

def revisar_productos():
    for tienda, url in PRODUCTOS.items():
        r = requests.get(url, headers=HEADERS)
        pagina = r.text.lower()

        if "out of stock" not in pagina:
            enviar_mensaje(
                f"🟢 **STOCK DISPONIBLE** en **{tienda}**\n{url}"
            )

while True:
    revisar_productos()
    time.sleep(1200)  # 20 minutos
