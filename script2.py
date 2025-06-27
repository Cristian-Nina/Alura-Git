import json
import time
import os
from telegram import Bot

# Configuración
TOKEN = "TU_TOKEN_DE_BOT"
CHANNEL_ID = "@tu_canal"  # o ID numérico como -1001234567890
DOMINIOS_JSONL = "dominios_filtrados.jsonl"
PROCESADOS_FILE = "procesados.json"

# Inicializar bot
bot = Bot(token=TOKEN)

# Cargar dominios ya enviados
if os.path.exists(PROCESADOS_FILE):
    with open(PROCESADOS_FILE, "r") as f:
        procesados = set(json.load(f))
else:
    procesados = set()

def leer_nuevos_dominios():
    nuevos = []
    try:
        with open(DOMINIOS_JSONL, "r") as f:
            for linea in f:
                try:
                    data = json.loads(linea.strip())
                    dominio = data.get("domain")
                    if dominio and dominio not in procesados:
                        nuevos.append((dominio, data.get("timestamp")))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return nuevos

def guardar_procesados():
    with open(PROCESADOS_FILE, "w") as f:
        json.dump(list(procesados), f)

def enviar_a_telegram(dominio, timestamp):
    mensaje = f"🔎 Dominio detectado:\n{dominio}\n🕒 {timestamp}"
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=mensaje)
        print(f"✅ Enviado: {dominio}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def main():
    print("⏳ Monitoreando dominios...")
    while True:
        nuevos = leer_nuevos_dominios()
        for dominio, timestamp in nuevos:
            enviar_a_telegram(dominio, timestamp)
            procesados.add(dominio)
        guardar_procesados()
        time.sleep(10)  # Espera antes de revisar de nuevo

if __name__ == "__main__":
    main()
import json
import time
import os
from telegram import Bot

# Configuración
TOKEN = "TU_TOKEN_DE_BOT"
CHANNEL_ID = "@tu_canal"  # o ID numérico como -1001234567890
DOMINIOS_JSONL = "dominios_filtrados.jsonl"
PROCESADOS_FILE = "procesados.json"

# Inicializar bot
bot = Bot(token=TOKEN)

# Cargar dominios ya enviados
if os.path.exists(PROCESADOS_FILE):
    with open(PROCESADOS_FILE, "r") as f:
        procesados = set(json.load(f))
else:
    procesados = set()

def leer_nuevos_dominios():
    nuevos = []
    try:
        with open(DOMINIOS_JSONL, "r") as f:
            for linea in f:
                try:
                    data = json.loads(linea.strip())
                    dominio = data.get("domain")
                    if dominio and dominio not in procesados:
                        nuevos.append((dominio, data.get("timestamp")))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return nuevos

def guardar_procesados():
    with open(PROCESADOS_FILE, "w") as f:
        json.dump(list(procesados), f)

def enviar_a_telegram(dominio, timestamp):
    mensaje = f"🔎 Dominio detectado:\n{dominio}\n🕒 {timestamp}"
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=mensaje)
        print(f"✅ Enviado: {dominio}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def main():
    print("⏳ Monitoreando dominios...")
    while True:
        nuevos = leer_nuevos_dominios()
        for dominio, timestamp in nuevos:
            enviar_a_telegram(dominio, timestamp)
            procesados.add(dominio)
        guardar_procesados()
        time.sleep(10)  # Espera antes de revisar de nuevo

if __name__ == "__main__":
    main()
import json
import time
import os
from telegram import Bot

# Configuración
TOKEN = "TU_TOKEN_DE_BOT"
CHANNEL_ID = "@tu_canal"  # o ID numérico como -1001234567890
DOMINIOS_JSONL = "dominios_filtrados.jsonl"
PROCESADOS_FILE = "procesados.json"

# Inicializar bot
bot = Bot(token=TOKEN)

# Cargar dominios ya enviados
if os.path.exists(PROCESADOS_FILE):
    with open(PROCESADOS_FILE, "r") as f:
        procesados = set(json.load(f))
else:
    procesados = set()

def leer_nuevos_dominios():
    nuevos = []
    try:
        with open(DOMINIOS_JSONL, "r") as f:
            for linea in f:
                try:
                    data = json.loads(linea.strip())
                    dominio = data.get("domain")
                    if dominio and dominio not in procesados:
                        nuevos.append((dominio, data.get("timestamp")))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return nuevos

def guardar_procesados():
    with open(PROCESADOS_FILE, "w") as f:
        json.dump(list(procesados), f)

def enviar_a_telegram(dominio, timestamp):
    mensaje = f"🔎 Dominio detectado:\n{dominio}\n🕒 {timestamp}"
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=mensaje)
        print(f"✅ Enviado: {dominio}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def main():
    print("⏳ Monitoreando dominios...")
    while True:
        nuevos = leer_nuevos_dominios()
        for dominio, timestamp in nuevos:
            enviar_a_telegram(dominio, timestamp)
            procesados.add(dominio)
        guardar_procesados()
        time.sleep(10)  # Espera antes de revisar de nuevo

if __name__ == "__main__":
    main()
import json
import time
import os
from telegram import Bot

# Configuración
TOKEN = "TU_TOKEN_DE_BOT"
CHANNEL_ID = "@tu_canal"  # o ID numérico como -1001234567890
DOMINIOS_JSONL = "dominios_filtrados.jsonl"
PROCESADOS_FILE = "procesados.json"

# Inicializar bot
bot = Bot(token=TOKEN)

# Cargar dominios ya enviados
if os.path.exists(PROCESADOS_FILE):
    with open(PROCESADOS_FILE, "r") as f:
        procesados = set(json.load(f))
else:
    procesados = set()

def leer_nuevos_dominios():
    nuevos = []
    try:
        with open(DOMINIOS_JSONL, "r") as f:
            for linea in f:
                try:
                    data = json.loads(linea.strip())
                    dominio = data.get("domain")
                    if dominio and dominio not in procesados:
                        nuevos.append((dominio, data.get("timestamp")))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return nuevos

def guardar_procesados():
    with open(PROCESADOS_FILE, "w") as f:
        json.dump(list(procesados), f)

def enviar_a_telegram(dominio, timestamp):
    mensaje = f"🔎 Dominio detectado:\n{dominio}\n🕒 {timestamp}"
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=mensaje)
        print(f"✅ Enviado: {dominio}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def main():
    print("⏳ Monitoreando dominios...")
    while True:
        nuevos = leer_nuevos_dominios()
        for dominio, timestamp in nuevos:
            enviar_a_telegram(dominio, timestamp)
            procesados.add(dominio)
        guardar_procesados()
        time.sleep(10)  # Espera antes de revisar de nuevo

if __name__ == "__main__":
    main()
import json
import time
import os
from telegram import Bot

# Configuración
TOKEN = "TU_TOKEN_DE_BOT"
CHANNEL_ID = "@tu_canal"  # o ID numérico como -1001234567890
DOMINIOS_JSONL = "dominios_filtrados.jsonl"
PROCESADOS_FILE = "procesados.json"

# Inicializar bot
bot = Bot(token=TOKEN)

# Cargar dominios ya enviados
if os.path.exists(PROCESADOS_FILE):
    with open(PROCESADOS_FILE, "r") as f:
        procesados = set(json.load(f))
else:
    procesados = set()

def leer_nuevos_dominios():
    nuevos = []
    try:
        with open(DOMINIOS_JSONL, "r") as f:
            for linea in f:
                try:
                    data = json.loads(linea.strip())
                    dominio = data.get("domain")
                    if dominio and dominio not in procesados:
                        nuevos.append((dominio, data.get("timestamp")))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return nuevos

def guardar_procesados():
    with open(PROCESADOS_FILE, "w") as f:
        json.dump(list(procesados), f)

def enviar_a_telegram(dominio, timestamp):
    mensaje = f"🔎 Dominio detectado:\n{dominio}\n🕒 {timestamp}"
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=mensaje)
        print(f"✅ Enviado: {dominio}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def main():
    print("⏳ Monitoreando dominios...")
    while True:
        nuevos = leer_nuevos_dominios()
        for dominio, timestamp in nuevos:
            enviar_a_telegram(dominio, timestamp)
            procesados.add(dominio)
        guardar_procesados()
        time.sleep(10)  # Espera antes de revisar de nuevo

if __name__ == "__main__":
    main()
v
