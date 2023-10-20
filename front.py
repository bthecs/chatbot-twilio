from informe.arbol import arbol
from informe.grafico import grafico
from informe.mapa import mapa
from informe.constantes import main
from apscheduler.schedulers.background import BackgroundScheduler
import requests

def get_all_data():
    url = "https://12ee-207-248-125-20.ngrok-free.app/get-all-data"
    total_mensajes = requests.get(url)
    url_2 = "https://12ee-207-248-125-20.ngrok-free.app/get-filter-data"
    json_data = {
        "value": "si, me encantaria",
        "column": "initial_message"
    }
    si_resp = requests.get(url_2, json=json_data)
    json_data_2 = {
        "value": "en otro momento",
        "column": "initial_message"
    }
    no_resp = requests.get(url_2, json=json_data_2)
    
    return main(total_mensajes.json(), si_resp.json(), no_resp.json())

if __name__ == "__main__":
    mapa(['2604017664'])
    arbol(0, 0, 0, 0, 0, 0, 0, 0)
    grafico(0, 0, 0)
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_all_data, 'interval', seconds=10)
    scheduler.start()

    