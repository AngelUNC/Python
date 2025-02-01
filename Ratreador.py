import time
import json
import requests

DEBUG_PORT = 9222
URL_PART = "us.i.mi.com/mobile/find"  
REFRESH_INTERVAL = 300  


try:
    response = requests.get(f"http://localhost:{DEBUG_PORT}/json")
    tabs = json.loads(response.text)
      
    target_tab = None
    for tab in tabs:
        if "webSocketDebuggerUrl" in tab and URL_PART in tab.get("url", ""):
            target_tab = tab["id"]
            break

    if target_tab:
        while True:
            print(f"Recargando la pestaña con {URL_PART}...")
            requests.post(f"http://localhost:{DEBUG_PORT}/json/reload/{target_tab}")
            time.sleep(REFRESH_INTERVAL)
    else:
        print("No se encontró la pestaña con la URL especificada.")

except requests.exceptions.ConnectionError:
    print("No se pudo conectar a Chrome. Asegúrate de iniciarlo con --remote-debugging-port=9222")
