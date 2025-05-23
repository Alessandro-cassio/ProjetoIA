# Pipeline de treinamento completo adaptado para escolha entre Uber e iFood
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Carrega os dados simulados
df = pd.read_csv("data/dataset_simulado.csv")

# Verifica as colunas disponíveis (opcional para debug)
print("Colunas do dataset:", df.columns)

# Define variáveis de entrada e saída
X = df[["distancia_km", "tempo_estimado_min", "preco_frete", "disponibilidade_motoristas"]]
y = df["melhor_opcao"]  # Corrigido para o nome certo da coluna

# Mostra a distribuição da variável alvo
print("\nDistribuição das classes:\n", y.value_counts())

# Divide os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Cria pipeline com normalização + modelo
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100, random_state=0))
])

# Treina o modelo
pipeline.fit(X_train, y_train)

# Faz predições
y_pred = pipeline.predict(X_test)

# Avalia o modelo
acc = accuracy_score(y_test, y_pred)
print(f"\nAcurácia da pipeline: {acc:.2%}")

# Exibe relatório detalhado de desempenho
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))
