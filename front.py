from informe.arbol import arbol
from informe.grafico import grafico
from informe.mapa import mapa
from apscheduler.schedulers.background import BackgroundScheduler
import requests

def get_all_data():
    url = "https://12ee-207-248-125-20.ngrok-free.app/get-all-data"
    response = requests.get(url)
    print(response.json())

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_all_data, 'interval', seconds=30)
    scheduler.start()

    mapa()
    arbol()
    grafico()