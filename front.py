from informe.constantes import main
# from apscheduler.schedulers.background import BackgroundScheduler
import requests

def get_all_data():
    url = "https://ea1b-207-248-125-79.ngrok-free.app/get-all-data"
    total_mensajes = requests.get(url)
    url_2 = "https://ea1b-207-248-125-79.ngrok-free.app/get-filter-data"
    json_data = {"value": "contactar con asesor","column": "initial_message"}
    si_resp = requests.get(url_2, json=json_data)
    json_data_2 = {"value": "no, gracias","column": "initial_message"}
    no_resp = requests.get(url_2, json=json_data_2)
    url_3 = "https://ea1b-207-248-125-79.ngrok-free.app/get-column-data"
    json_column = {"column": "initial_message"}
    message_column = requests.get(url_3, json=json_column)
    
    
    return main(total_mensajes.json(), no_resp.json(), si_resp.json(), message_column.json())

if __name__ == "__main__":
    get_all_data()
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(get_all_data, 'interval', seconds=180)
    # scheduler.start()

    