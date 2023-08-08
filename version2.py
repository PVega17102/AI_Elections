import pandas as pd

# Cargar el archivo CSV
csv_data = pd.read_csv('diputados.csv')

# Mostrar información del DataFrame antes del cambio
print(csv_data.info())

# Lista de columnas a convertir
columnas_a_convertir = ['PAN', 'PRI', 'PRD', 'MORENA', 'PVEM', 'NUEVA_ALIANZA', 'MOVIMIENTO_CIUDADANO','PT']

# Cambiar el tipo de columna de 'object' a 'int64'
for columna in columnas_a_convertir:
    csv_data[columna] = csv_data[columna].apply(lambda x: int(x) if str(x).strip() else 0)

# Mostrar información del DataFrame después del cambio
print(csv_data.info())

# Guardar el DataFrame modificado en un nuevo archivo CSV
csv_data.to_csv('diputados_modificado.csv', index=False)































