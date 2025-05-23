from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from flask_cors import CORS

# Inicializa o Flask
app = Flask(__name__)
CORS(app)

# Carrega e prepara os dados
df = pd.read_csv("data/dataset_simulado.csv")
df = df.dropna()

# Features e target
X = df[["distancia_km", "tempo_estimado_min", "preco_frete", "disponibilidade_motoristas"]]
y = df["melhor_opcao"].map({"Uber": 0, "iFood": 1})

# Normalização
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Rota de predição
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convertendo os dados de entrada para o formato de dataframe que o modelo espera
    input_data = pd.DataFrame([{
        'distancia_km': data['distancia_km'],
        'tempo_estimado_min': data['tempo_estimado_min'],
        'preco_frete': data['preco_frete'],
        'disponibilidade_motoristas': data['quantidade_motoristas']  # Certifique-se de que o nome está correto
    }])

    # Normalizando os dados de entrada
    input_scaled = scaler.transform(input_data)

    # Fazendo a predição
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]

    # Convertendo a predição para 'Uber' ou 'iFood'
    prediction_label = "Uber" if prediction == 0 else "iFood"
    prob_uber = round(probabilities[0] * 100, 2)
    prob_ifood = round(probabilities[1] * 100, 2)

    return jsonify({
        'prediction': prediction_label,
        'probabilidades': {
            'Uber': prob_uber,
            'iFood': prob_ifood
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
