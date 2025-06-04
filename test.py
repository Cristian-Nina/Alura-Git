import certstream

def callback(message, context):
    print(message)  # Muestra todo el JSON recibido

certstream.listen_for_events(callback, url='wss://certstream.calidog.io/')
