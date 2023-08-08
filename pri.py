import pandas as pd

# Cargar el archivo CSV
data = pd.read_csv('diputados.csv')

# Crear un diccionario para almacenar las sumas de votos por estado
resultados = {}

# Sumar los votos por estado
for index, row in data.iterrows():
    estado = row['ESTADO']
    votos_str = row['PRI']
    
    # Verificar si el valor no está vacío
    if votos_str.strip():
        votos = int(votos_str)
        
        if estado in resultados:
            resultados[estado] += votos
        else:
            resultados[estado] = votos

# Nombres de los estados
nombres_estados = {
    1: 'Aguascalientes',
    2: 'Baja California',
    3: 'Baja California Sur',
    4: 'Campeche',
    5: 'Coahuila',
    6: 'Colima',
    7: 'Chiapas',
    8: 'Chihuahua',
    9: 'Distrito Federal',
    10: 'Durango',
    11: 'Guanajuato',
    12: 'Guerrero',
    13: 'Hidalgo',
    14: 'Jalisco',
    15: 'México',
    16: 'Michoacán',
    17: 'Morelos',
    18: 'Nayarit',
    19: 'Nuevo León',
    20: 'Oaxaca',
    21: 'Puebla',
    22: 'Querétaro',
    23: 'Quintana Roo',
    24: 'San Luis Potosí',
    25: 'Sinaloa',
    26: 'Sonora',
    27: 'Tabasco',
    28: 'Tamaulipas',
    29: 'Tlaxcala',
    30: 'Veracruz',
    31: 'Yucatán',
    32: 'Zacatecas'
}

# Obtener los nombres de estado y los totales de votos
nombres_estado = [nombres_estados[estado] for estado in resultados.keys()]
total_votos = list(resultados.values())

for estado, votos in resultados.items():
    print('Estado:', estado)
    print('- Votos totales:', votos)
    print('---')

