import requests

# Cambia el número de estado según lo que desees consultar
estado = "3"
url = f"http://localhost:5000/probabilidades?estado={estado}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Probabilidades de ganar para el estado {estado}:")
    for party, probability in data.items():
        probability_percentage = probability * 100
        print(f"Probabilidad de que el partido {party} gane: {probability_percentage:.2f}%")
else:
    print(f"Error al obtener los datos. Estado del servidor: {response.status_code}")