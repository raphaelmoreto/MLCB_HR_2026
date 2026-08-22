import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ============================================================
# PROJETO: MOTOR DE NLU - AGÊNCIA DE VIAGENS
# ============================================================


# ============================================================
# REQUISITO 1
# Criar um dataset próprio em um DataFrame Pandas
# com no mínimo 12 frases e 3 intenções distintas.
# ============================================================

dados_viagem = {

    "mensagem": [
        "Quero comprar uma passagem para Orlando",
        "Gostaria de reservar um voo para Salvador",
        "Qual o preço da passagem de avião para Lisboa?",
        "Preciso comprar bilhete aéreo para o Rio de Janeiro",

        "Como faço para cancelar minha reserva de voo?",
        "Quero pedir o cancelamento da minha viagem",
        "Gostaria de anular minha compra de passagem",
        "Preciso cancelar meu voo marcado para amanhã",

        "Quero falar com um atendente humano por favor",
        "Pode me transferir para o suporte ao cliente?",
        "Preciso de ajuda com uma pessoa do atendimento",
        "Gostaria de conversar com um operador da agência"
    ],

    "intencao": [
        "comprar_passagem",
        "comprar_passagem",
        "comprar_passagem",
        "comprar_passagem",
        "cancelar_reserva",
        "cancelar_reserva",
        "cancelar_reserva",
        "cancelar_reserva",
        "falar_atendente",
        "falar_atendente",
        "falar_atendente",
        "falar_atendente"
    ]
}


# Criando o DataFrame
df_viagens = pd.DataFrame(dados_viagem)


# Exibindo o dataset
print("==================================================")
print("DATASET")
print("==================================================")
print(df_viagens)
print()


# ============================================================
# Separação das variáveis
#
# X = mensagens que o modelo vai analisar
# y = intenção que o modelo precisa aprender
# ============================================================

X = df_viagens["mensagem"]
y = df_viagens["intencao"]


# ============================================================
# REQUISITO 2
# Divisão dos dados em Treino e Teste
# usando train_test_split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


print("==================================================")
print("DIVISÃO DOS DADOS")
print("==================================================")
print(f"Quantidade de frases para treinamento: {len(X_train)}")
print(f"Quantidade de frases para teste: {len(X_test)}")
print()


# ============================================================
# REQUISITO 3
# Vetorização do texto utilizando TfidfVectorizer
#
# O modelo não entende diretamente frases.
# O TfidfVectorizer transforma o texto em números.
# ============================================================

vectorizer = TfidfVectorizer()


# Aprende o vocabulário usando somente os dados de treino
X_train_vec = vectorizer.fit_transform(X_train)


# Transforma os dados de teste utilizando o mesmo vocabulário
X_test_vec = vectorizer.transform(X_test)


# ============================================================
# REQUISITO 4
# Criação e treinamento do algoritmo de classificação
#
# Algoritmo escolhido:
# LogisticRegression
# ============================================================

modelo_nlu = LogisticRegression()


# Treinando o modelo
modelo_nlu.fit(
    X_train_vec,
    y_train
)


# ============================================================
# Avaliação do modelo
# ============================================================

y_pred_test = modelo_nlu.predict(X_test_vec)

acuracia = accuracy_score(
    y_test,
    y_pred_test
)


print("==================================================")
print("AVALIAÇÃO DO MODELO")
print("==================================================")
print(f"Acurácia no conjunto de teste: {acuracia * 100:.2f}%")
print()


# ============================================================
# REQUISITO 5
# Criar no mínimo 3 frases INÉDITAS
#
# Essas frases não estavam no dataset original.
# ============================================================

frases_ineditas = [

    "Gostaria de saber o valor para voar até Paris",

    "Quero cancelar o bilhete que comprei ontem",

    "Me transfira para um suporte humano, por favor"

]


# ============================================================
# Transformando as frases inéditas em números
# ============================================================

frases_ineditas_vec = vectorizer.transform(
    frases_ineditas
)


# ============================================================
# Realizando as predições
# ============================================================

predicoes_ineditas = modelo_nlu.predict(
    frases_ineditas_vec
)


# ============================================================
# REQUISITO 6
# Exibir as intenções previstas no console
# ============================================================

print("==================================================")
print("MOTOR DE NLU - AGÊNCIA DE VIAGENS")
print("==================================================")

print(f"Acurácia do modelo: {acuracia * 100:.2f}%")
print()

print("--- PREDIÇÃO DE MENSAGENS INÉDITAS ---")
print()


for frase, intencao in zip(
    frases_ineditas,
    predicoes_ineditas
):

    print(f"Mensagem: '{frase}'")
    print(f"==> Intenção Predita: [{intencao}]")
    print()


print("==================================================")
print("FIM DO PROGRAMA")
print("==================================================")