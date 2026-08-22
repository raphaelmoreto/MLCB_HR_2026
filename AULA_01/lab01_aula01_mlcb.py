# EXERCÍCIO AULA 01 - CLASSIFICADOR DE INTENÇÕES PARA CHATBOT
# Aluno: RAPHAEL QUEIROZ MORETO
# Repositório GitHub: https://github.com/raphaelmoreto/MLCB_HR_2026

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. EXPANDA O DATASET: Adicione pelo menos mais 2 frases para cada intenção (Total minimo: 9 frases)
mensagens_intencao = [
    "Quero a segunda via do meu boleto",
    "Como faço para pagar a fatura?",
    "Minha internet está caindo muito",
    "O sinal da TV não está funcionando",
    "Quero cancelar meu plano imediatamente",
    "Desejo encerrar minha conta",
    "Erro ao validar o meu boleto",
    "O sistema está travando!",
    "Quero encerrar minha conta"
]

rotulos_intencao = [
    "financeiro",
    "financeiro",
    "suporte_tecnico",
    "suporte_tecnico",
    "cancelamento",
    "cancelamento",
    "financeiro",
    "suporte_tecnico",
    "cancelamento"
]

# 2. VETORIZAÇÃO DE TEXTO
# TODO: Instancie o CountVectorizer na variável 'vectorizer_intencao'
vectorizer_intencao = CountVectorizer(lowercase=True)

# TODO: Aplique o fit_transform nas mensagens_intencao e armazene em 'X_intencao'
X_intencao = vectorizer_intencao.fit_transform(mensagens_intencao)

# 3. TREINAMENTO DO MODELO
# TODO: Instancie o MultinomialNB na variável 'modelo_intencao'
modelo_intencao = MultinomialNB()

# TODO: Execute o treino do modelo usando o fit(X_intencao, rotulos_intencao)
modelo_intencao.fit(X_intencao, rotulos_intencao)


# 4. TESTE DE INFERÊNCIA
# Teste com uma frase inédita digitada por você
mensagem_usuario = ["Não recebi minha fatura deste mês"]

# TODO: Transforma a mensagem_usuario usando o vetorizador instanciado (use o método transform)
# X_usuario = ...
x_usuario = vectorizer_intencao.transform(mensagem_usuario)

# TODO: Faça a predição da intenção usando o método predict do modelo
# predicao = ...
predicao = modelo_intencao.predict(x_usuario)

print(f"Frase do Usuário: {mensagem_usuario[0]}")
print(f"Intenção Identificada: {predicao[0]}")