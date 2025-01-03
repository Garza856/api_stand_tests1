import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response_json= post_new_user(data.user_body).json()
auth_token= response_json['authToken']
print(auth_token)

authorization = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {auth_token}'
}

def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # Concatenación de URL base y ruta.
                         json=products_ids,  # Datos a enviar en la solicitud.
                         headers=authorization)  # Encabezados de solicitud.




