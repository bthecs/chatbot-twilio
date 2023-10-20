from database_module import get_number_of_records, get_number_of_records_by_filter



cantidad_mensajes = None
responde = None
si = None
por_si = None
por_no = None
no_en_otro_momento = None
no = None
porcentaje_si = None
porcentaje_no = None


def main( total_mensajes):
    print(total_mensajes)
    total = len(total_mensajes)
    cantidad_mensajes = total
    responde_no = 1 # no responde
    responde_si = 1 # si responde
    responde = responde_si + responde_no
    responde = responde
    si = responde_si
    por_si = si/responde
    por_no = 1-por_si
    no_en_otro_momento = responde-si
    no = cantidad_mensajes-responde
    porcentaje_si = "{:.2f}".format(por_si)
    porcentaje_no = "{:.2f}".format(por_no)
    return cantidad_mensajes, responde, si, por_si, por_no, no_en_otro_momento, no, porcentaje_si, porcentaje_no



