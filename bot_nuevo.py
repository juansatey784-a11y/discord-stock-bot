import requests
import time
import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not WEBHOOK_URL:
    raise Exception("WEBHOOK_URL no está configurado")

PRODUCTOS = {
    "Target": "https://www.target.com/p/2025-pok-me-2-5-elite-trainer-box/-/A-95082118",
    "Walmart": "https://www.walmart.com/ip/Pok-mon-Trading-Card-Game-Mega-Evolution-Ascended-Heroes-Elite-Trainer-Box/18710966734?conditionGroupCode=4&classType=REGULAR&athbdg=L1103&from=/search"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def enviar_mensaje(texto):
    requests.post(WEBHOOK_URL, json={"content": texto})

def revisar():
    for tienda, url in PRODUCTOS.items():
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            if "out of stock" not in r.text.lower():
                enviar_mensaje(
                    f"🟢 **STOCK DISPONIBLE** en **{tienda}**\n{url}"
                )
        except Exception as e:
            enviar_mensaje(f"⚠️ Error en {tienda}: {e}")

while True:
    revisar()
    time.sleep(1200)
