import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_new_client_kit(kit_body, auth_token):
    current_header = data.headers.copy() #Copia los header de data para usarlos en la función
    current_header["Authorization"] = "Bearer " + auth_token #Crea el header "Authorization" y concatena el token ingresado con la palabra Bearer (asi lo pide los requerimientos)
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_header)

#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.json())
