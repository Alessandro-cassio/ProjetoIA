import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carrega dataset simulado
df = pd.read_csv("data/dataset_simulado.csv")

# Remove linhas com valores nulos (se houver)
df = df.dropna()

# Verificar as colunas do DataFrame e as primeiras linhas
print("Colunas do DataFrame:", df.columns)
print("\nExemplo dos dados:")
print(df.head())

# Verificar valores únicos da variável alvo (se necessário)
print("\nValores únicos da variável alvo:", df["melhor_plataforma"].unique())

# Prepara os dados
X = df[["distancia_km", "tempo_estimado_min", "preco_frete", "disponibilidade_motoristas"]]
y = df["melhor_plataforma"].map({"Uber": 0, "iFood": 1})  # Converte a saída para números

# Divide treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treina modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Faz previsões
y_pred = model.predict(X_test)

# Avalia desempenho
acc = accuracy_score(y_test, y_pred)
print(f"\nAcurácia do modelo: {acc:.2%}")
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=["Uber", "iFood"]))
