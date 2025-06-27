import asyncio
import websockets
import json
from datetime import datetime

keywords = {"icbc", "beneficios", "clientes"}
filename = "dominios_filtrados.jsonl"

async def writer(queue):
    while True:
        log_entry = await queue.get()
        try:
            with open(filename, "a") as file:
                file.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Error escribiendo archivo: {e}")
        queue.task_done()

async def consume_certstream(queue):
    url = "ws://localhost:8080/full-stream"
    async with websockets.connect(url, max_size=None) as ws:
        while True:
            try:
                message = await ws.recv()
                data = json.loads(message)
                domains = data.get("data", {}).get("leaf_cert", {}).get("all_domains", [])

                for domain in domains:
                    domain_lower = domain.lower()
                    if any(keyword in domain_lower for keyword in keywords):
                        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                        log_entry = {
                            "domain": domain,
                            "timestamp": timestamp
                        }
                        await queue.put(log_entry)
                        print(f"Dominio filtrado: {domain} - {timestamp}")

            except Exception as e:
                print(f"Error en WebSocket: {e}")
                await asyncio.sleep(1)  # espera corta antes de intentar de nuevo

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        consume_certstream(queue),
        writer(queue)
    )

asyncio.run(main())
