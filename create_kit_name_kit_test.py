import sender_stand_request
import data

# función que cambia el contenido del cuerpo de solicitud
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy() #se copia el kit_body del archivo dara para trabajar en la funcion
    current_kit_body["name"] = kit_name #Se le pasa el valor ingresado en la funcion a esta key
    return current_kit_body #Devuelve dicho valor

# Funcion para obtener el token del usuario creado
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body) #Guarda la respuesta de la solicitud en la variable response
    return response.json()["authToken"] #Obtiene solamente el token de la respuesta
#*******************************************************************************************************************

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token()) #Crea la solicitud con el nombre enviado desde la prueba y obtiene su token
    assert response.status_code == 201 #Valida que la respuesta sea 201 OK
    assert response.json()["name"] == kit_body["name"] #Se valida que el nombre coincida con el que fue enviado

def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400 #Valida que la respuesta sea 400 Error
    assert response.json()["name"] == kit_body["name"]  # Se valida que el nombre coincida con el que fue enviado

#*************************************************************************************************************

def test_1_create_kit_name_1_char():
    current_kit_body =  get_kit_body("A") #crea el kit con el nombre "A"
    positive_assert(current_kit_body) #Testea el escenario positivo de acuerdo a la lista de comprobacion

def test_2_create_kit_name_511_char():
    current_kit_body =  get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC") #crea el kit con 511 caracteres
    positive_assert(current_kit_body) #Testea el escenario positivo de acuerdo a la lista de comprobacion

def test_3_create_kit_name_0_char():
    current_kit_body =  get_kit_body("") #crea el kit con ningun caracter
    negative_assert(current_kit_body) #Testea el escenario negativo de acuerdo a la lista de comprobacion

def test_4_create_kit_name_512_char():
    current_kit_body =  get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD") #crea el kit con 512 caracter
    negative_assert(current_kit_body) #Testea el escenario negativo de acuerdo a la lista de comprobacion

def test_5_create_kit_name_special_char():
    current_kit_body =  get_kit_body("'№%@'-_") #crea el kit con caracteres especiales
    positive_assert(current_kit_body) #Testea el escenario positivo de acuerdo a la lista de comprobacion

def test_6_create_kit_name_blank_char():
    current_kit_body =  get_kit_body(" A Aaa ") #crea el kit con espacios
    positive_assert(current_kit_body) #Testea el escenario positivo de acuerdo a la lista de comprobacion

def test_7_create_kit_name_numbers_string():
    current_kit_body =  get_kit_body("123") #crea el kit con numeros
    positive_assert(current_kit_body) #Testea el escenario positivo de acuerdo a la lista de comprobacion

def test_8_create_kit_name_no_parameter():
    current_kit_body = {} #crea el kit sin parametro
    negative_assert(current_kit_body) #Testea el escenario negativo de acuerdo a la lista de comprobacion

def test_9_create_kit_name_int_numbers():
    current_kit_body =  get_kit_body(123) #crea el kit con datos de numeros enteros (no válidos)
    negative_assert(current_kit_body) #Testea el escenario negativo de acuerdo a la lista de comprobacion


