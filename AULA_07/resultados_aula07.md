#EXERCÍCIO 1: Regressão Logística (Chatbot Bancário)
#Foco do Modelo: Regressão Logística (LogisticRegression)
#Objetivo: Implementar o pipeline base completo com classificação probabilística e extração de valores monetários.

# =====================================================================
# LAB 1: NLU BANCÁRIO COM REGRESSÃO LOGÍSTICA
# =====================================================================

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

dados_treino = [
    ("quero transferir dinheiro", "transferencia"),
    ("como faço uma transferência", "transferencia"),
    ("preciso fazer um pix", "pix"),
    ("quero enviar um pix", "pix"),
    ("qual é o saldo da minha conta", "saldo"),
    ("quanto tenho na conta", "saldo"),
    ("quero sacar dinheiro", "saque"),
    ("onde posso sacar dinheiro", "saque"),
    ("qual a previsão do tempo", "fora_escopo"),
    ("quem ganhou o jogo", "fora_escopo"),
]

stopwords = [
    "a", "o", "as", "os", "um", "uma",
    "de", "da", "do", "das", "dos",
    "em", "no", "na", "nos", "nas",
    "que", "é", "e", "como", "meu", "minha"
]


# 1. PRÉ-PROCESSAMENTO
def pré_processar(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower()).strip()
    tokens = texto_limpo.split()
    
    # TODO 1.1: Filtre as stopwords da lista 'tokens' usando List Comprehension
    tokens_filtrados = [token for token in tokens if token not in stopwords]
    
    return " ".join(tokens_filtrados)

X_treino_limpo = [pré_processar(item[0]) for item in dados_treino]
y_treino = [item[1] for item in dados_treino]

# 2. VETORIZAÇÃO E TREINAMENTO
vectorizer = TfidfVectorizer()

# TODO 1.2: Aprenda o vocabulário e vetorize 'X_treino_limpo' em um único passo
X_vetorizado = vectorizer.fit_transform(X_treino_limpo)

modelo = LogisticRegression()
modelo.fit(X_vetorizado, y_treino)

# 3. EXTRAÇÃO DE ENTIDADE (REGEX)
def extrair_valor_reais(texto_original):
    match = re.search(r'(\d+)\s*reais', texto_original, re.IGNORECASE)
    # TODO 1.3: Se houver match, converta o grupo 1 para float. Caso contrário, retorne None.
    if match:
      return float(match.group(1))

    return None

# 4. PIPELINE NLU
def processar_nlu(mensagem_usuario, threshold=0.55):
    texto_p = pré_processar(mensagem_usuario)
    vetor_input = vectorizer.transform([texto_p])
    
    probas = modelo.predict_proba(vetor_input)[0]
    
    # TODO 1.4: Extraia a MAIOR probabilidade (max) e a intenção prevista (argmax em modelo.classes_)
    maior_confianca = max(probas)
    intencao_prevista = modelo.classes_[probas.argmax()]
    
    # TODO 1.5: Se maior_confianca < threshold ou intencao == "fora_escopo", retorne FALLBACK.
    # Caso contrário, retorne SUCESSO com a intenção, confiança e o valor extraído.
    # TODO 1.5: Escreva a condicional if/else abaixo
    if maior_confianca < threshold or intencao_prevista == "fora_escopo":
      return {
          "status": "FALLBACK",
          "mensagem": "Não consegui identificar sua solicitação com segurança.",
          "confianca": float(maior_confianca)
      }

    valor = extrair_valor_reais(mensagem_usuario)

    return {
        "status": "SUCESSO",
        "intencao": intencao_prevista,
        "confianca": float(maior_confianca),
        "valor": valor
    }

# --- TESTE 1 ---
if __name__ == "__main__":
    print(processar_nlu("qual é o saldo da minha conta"))
