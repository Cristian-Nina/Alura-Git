import certstream

def callback(message, context):
    if message["message_type"] != "certificate_update":
        return

    dominios = message["data"]["leaf_cert"]["all_domains"]
    if dominios:
        print(f"[+] Dominio detectado: {dominios[0]}")

print("Escuchando certificados desde Certstream...\n")
certstream.listen_for_events(callback, url='wss://certstream.calidog.io/')
