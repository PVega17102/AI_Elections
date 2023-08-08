import pandas as pd
from flask import Flask, request, jsonify
from sklearn.cluster import KMeans

app = Flask(__name__)

# Leer el CSV y convertir las columnas de votos a tipo numérico
dataframe = pd.read_csv("resultados.csv", dtype={"ESTADO": int})
party_columns = ["NULOS", "PRI", "PAN", "MORENA", "PRD", "PVEM", "PT", "MOVIMIENTO_CIUDADANO", "PH", "PS"]
for col in party_columns:
    dataframe[col] = pd.to_numeric(dataframe[col], errors="coerce")

# Ajustar el modelo K-means con un número de clústeres
num_clusters = 9
kmeans_model = KMeans(n_clusters=num_clusters)
X = dataframe[party_columns].values
kmeans_model.fit(X)

# Obtener los clústeres asignados a cada estado
cluster_labels = kmeans_model.predict(X)

# Identificar el partido político con más votos en cada clúster
parties = ["NULOS", "PRI", "PAN", "MORENA", "PRD", "PVEM", "PT", "MOVIMIENTO_CIUDADANO", "PH", "PS"]
most_voted_party_per_cluster = {}
for cluster in range(num_clusters):
    cluster_data = dataframe[cluster_labels == cluster]
    most_voted_party = cluster_data[parties].idxmax(axis=1).mode().iloc[0]
    most_voted_party_per_cluster[cluster] = most_voted_party

dataframe["CLUSTER"] = cluster_labels

def get_win_probability_for_party_in_state(party_name, state_name):
    state_data = dataframe[dataframe["ESTADO"] == state_name]
    if state_data.empty:
        return jsonify({"message": f"El estado '{state_name}' no se encontró en los datos."}), 404
    
    total_valid_votes = state_data[party_columns].sum().sum()
    party_votes = state_data[party_name].iloc[0]
    probability = party_votes / total_valid_votes
    return probability

# Ruta del API para obtener las probabilidades en formato JSON
@app.route('/api/v1/estado/<int:estado_id>', methods=['GET'])
def obtener_probabilidades(estado_id):
    state_data = dataframe[dataframe["ESTADO"] == estado_id]
    if state_data.empty:
        return jsonify({"message": f"El estado '{estado_id}' no se encontró en los datos."}), 404
    
    party_probabilities_in_state = {}
    for party in parties:
        probability = get_win_probability_for_party_in_state(party, estado_id)
        party_probabilities_in_state[party] = probability * 100
    
    return jsonify(party_probabilities_in_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    #para entrar al api se tiene que entrar a esta url: http://localhost:5000/api/v1/estado/7 al final donde viene el 7 es para cambiar el estado que queremos revisar
