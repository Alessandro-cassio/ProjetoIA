import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carregar dataset
df = pd.read_csv("data/dataset_simulado.csv")

# Verificar a distribuição das classes
print("Distribuição das classes:", df["melhor_opcao"].value_counts())

# Prepara os dados
X = df[["distancia_km", "tempo_estimado_min", "preco_frete", "disponibilidade_motoristas"]]
y = df["melhor_opcao"]

# Converter o target para números (Uber: 0, iFood: 1)
y = y.map({"Uber": 0, "iFood": 1})

# Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar desempenho
acc = accuracy_score(y_test, y_pred)
print(f"\nAcurácia do modelo: {acc:.2%}")
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=["Uber", "iFood"]))
