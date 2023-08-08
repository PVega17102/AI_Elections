import pandas as pd

def eliminar_columnas(csv_entrada, columnas_eliminar, csv_salida):
    # Cargar el archivo CSV de entrada en un DataFrame
    df = pd.read_csv(csv_entrada)

    # Eliminar las columnas no utilizadas
    df = df.drop(columnas_eliminar, axis=1)

    # Guardar el DataFrame resultante en un nuevo archivo CSV
    df.to_csv(csv_salida, index=False)

# Ejemplo de uso
csv_entrada = 'diputados_modificado.csv'
csv_salida = 'votos.csv'
columnas_eliminar = ['NUM_BOLETAS_EXTRAIDAS','CAND_IND_2','DISTRITO', 'SECCION','ID_CASILLA','TIPO_CASILLA','EXT_CONTIGUA','UBICACION_CASILLA','TIPO_ACTA','NUM_BOLETAS_SOBRANTES','TOTAL_CIUDADANOS_VOTARON','C_PRI_PVEM','C_PRD_PT','CAND_IND_1','NO_REGISTRADOS','TOTAL_VOTOS','LISTA_NOMINAL','OBSERVACIONES','CONTABILIZADA']  # Lista de columnas a eliminar

eliminar_columnas(csv_entrada, columnas_eliminar, csv_salida)
