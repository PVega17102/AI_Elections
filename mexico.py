'''import pandas as pd

# Cargar el archivo CSV
data = pd.read_csv('diputados.csv')

# Crear un diccionario para almacenar los totales por cada columna
resultados_columnas = {}

# Obtener una lista de todas las columnas que deseas sumar
columnas_suma = ['PAN', 'PRI', 'MORENA', 'NUEVA_ALIANZA']

# Iterar sobre cada fila del DataFrame
for index, row in data.iterrows():
    estado = row['ESTADO']
    
    # Iterar sobre las columnas de suma
    for columna in columnas_suma:
        votos_str = row[columna]  # Obtener el valor de los votos como una cadena
        
        # Verificar si el valor no está vacío
        if votos_str.strip():
            votos = int(votos_str)  # Convertir los votos a entero
            
            # Verificar si la columna ya está en el diccionario
            if columna in resultados_columnas:
                # Verificar si el estado ya está en el diccionario
                if estado in resultados_columnas[columna]:
                    # Sumar los votos al partido existente en el estado
                    resultados_columnas[columna][estado] += votos
                else:
                    # Agregar el estado y los votos al diccionario
                    resultados_columnas[columna][estado] = votos
            else:
                # Crear un nuevo diccionario para el estado y los votos
                resultados_columnas[columna] = {estado: votos}

# Crear un DataFrame para cada columna
df_list = []
for columna, resultados in resultados_columnas.items():
    df = pd.DataFrame(list(resultados.items()), columns=['ESTADO', columna])
    df_list.append(df)

# Combinar los DataFrames en uno solo utilizando la columna 'ESTADO' como referencia
nuevos_datos = df_list[0]
for i in range(1, len(df_list)):
    nuevos_datos = pd.merge(nuevos_datos, df_list[i], on='ESTADO', how='outer')

# Guardar el DataFrame en un archivo CSV
nuevos_datos.to_csv('resultados.csv', index=False)

print("Archivo 'resultados.csv' creado exitosamente.")
'''

import pandas as pd

# Cargar el archivo CSV
data = pd.read_csv('votos_1.csv')
print(data.info())

# Crear un diccionario para almacenar los totales por cada columna
resultados_columnas = {}

# Obtener una lista de todas las columnas que deseas sumar
columnas_suma = ['PAN', 'PRI', 'PRD', 'PVEM', 'PT','MOVIMIENTO_CIUDADANO','MORENA','PH','PS','NULOS']
# Iterar sobre cada fila del DataFrame
for index, row in data.iterrows():
    estado = row['ESTADO']
    
    # Iterar sobre las columnas de suma
    for columna in columnas_suma:
        votos = row[columna]  # Obtener el valor de los votos
        
        # Verificar si el valor no es NaN
        if pd.notnull(votos):
            # Verificar si la columna ya está en el diccionario
            if columna in resultados_columnas:
                # Verificar si el estado ya está en el diccionario
                if estado in resultados_columnas[columna]:
                    # Sumar los votos al partido existente en el estado
                    resultados_columnas[columna][estado] += votos
                else:
                    # Agregar el estado y los votos al diccionario
                    resultados_columnas[columna][estado] = votos
            else:
                # Crear un nuevo diccionario para el estado y los votos
                resultados_columnas[columna] = {estado: votos}

# Crear un DataFrame para cada columna
df_list = []
for columna, resultados in resultados_columnas.items():
    df = pd.DataFrame(list(resultados.items()), columns=['ESTADO', columna])
    df_list.append(df)

# Combinar los DataFrames en uno solo utilizando la columna 'ESTADO' como referencia
nuevos_datos = df_list[0]
for i in range(1, len(df_list)):
    nuevos_datos = pd.merge(nuevos_datos, df_list[i], on='ESTADO', how='outer')

# Guardar el DataFrame en un archivo CSV
nuevos_datos.to_csv('resultados.csv', index=False)

print("Archivo 'resultados.csv' creado exitosamente.")
