import certstream
import datetime


palabras_clave = ["icbc", "ibc", "nbeneficios", "clientes"]

# Para evitar repetidos consecutivos
ultimos_guardados = set()

def callback(message, context):
    if message["message_type"] != "certificate_update":
        return

    try:
        dominios = message["data"]["leaf_cert"]["all_domains"]
        if not dominios:
            return

        for dominio in dominios:
            dominio_lower = dominio.lower()

            if any(palabra in dominio_lower for palabra in palabras_clave):
                if dominio not in ultimos_guardados:
                    ultimos_guardados.add(dominio)
                    # Limpiar set si se acumulan demasiados dominios
                    if len(ultimos_guardados) > 100:
                        ultimos_guardados.clear()

                    fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    url = f"https://{dominio}"
                    print(f"[{fecha}] Coincidencia: {url}")
                    with open("resultados.txt", "a") as archivo:
                        archivo.write(f"{fecha} - {url}\n")
                break  # Solo guardar uno por certificado
    except Exception as e:
        print(f"[ERROR] {e}")

print("Escuchando certificados de Certstream...")
certstream.listen_for_events(callback, url='wss://certstream.calidog.io/')
