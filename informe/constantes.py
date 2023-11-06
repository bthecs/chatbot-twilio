from informe.arbol import arbol
from informe.grafico import grafico
from informe.mapa import mapa



cantidad_mensajes = None
responde = None
si = None
por_si = None
por_no = None
no_en_otro_momento = None
no = None
porcentaje_si = None
porcentaje_no = None


def main(total_mensajes, si_resp, no_resp, message_column):
    try:
        list_number = []
        for number in total_mensajes:
            list_number.append(number[1])
        
        total = len(total_mensajes)
        cantidad_mensajes = total
        responde_no = len(si_resp)
        responde_si = len(no_resp)
        responde = message_column
        si = responde_si
        por_si = si/responde
        por_no = 1-por_si
        no_en_otro_momento = responde-si
        no = cantidad_mensajes-responde
        porcentaje_si = "{:.2f}".format(por_si)
        porcentaje_no = "{:.2f}".format(por_no)
        print("Refrescando la pagina papa")
        mapa(list_number)
        arbol(total, cantidad_mensajes, responde, responde_no, responde_si, porcentaje_si, porcentaje_no, no)
        grafico(total, responde, responde_si)
    except Exception as e:
        list_number = []
        for number in total_mensajes:
            list_number.append(number[1])
        
        total = len(total_mensajes)
        cantidad_mensajes = total
        responde_no = 0
        responde_si = 0
        responde = responde_si + responde_no
        si = responde_si
        por_si = 0
        por_no = 0
        no_en_otro_momento = 0
        no = cantidad_mensajes-0
        porcentaje_si = "{:.2f}".format(por_si)
        porcentaje_no = "{:.2f}".format(por_no)
        print("Refrescando la pagina papa")
        mapa(list_number)
        arbol(total, cantidad_mensajes, responde, responde_no, responde_si, porcentaje_si, porcentaje_no, no)
        grafico(total, responde, responde_si)


