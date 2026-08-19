--- RESULTADOS DO LAB 01 ---
Mensagem: 'Quero consultar quanto dinheiro tenho' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Pode me ajudar a fazer um pix?' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Gostaria de cancelar meu cartão de crédito' ==> Intenção Predita: [cancelar_conta]

# 1 -Incorreto na primeira mensagem.
# 2 - Para consertar eu incluí a mensagem que gerou erro (a primeira) dentro do meu dataframe
# 3 - Detalhe a função do LogisticRegression no algorítmo.


--- RESULTADOS DO LAB 02 ---
Mensagem de Teste: 'Gostaria de devolver o produto que comprei'
Intenção Predita: troca_devolucao

--- Distribuição de Probabilidades por Classe ---
Classe [duvida_frete]: 27.99%
Classe [rastrear_pedido]: 24.54%
Classe [troca_devolucao]: 47.46%

# 1 - Resultados corretos.
# 2 - Incluir dentro do dataset a mensagem digitada pelo usuário para que o NavieBayes entenda melhor.
# 3  - Ele busca as palavras que tem mais peso e calcula com o rotulo direcionado.

--- RESULTADOS DO LAB 03 ---

#========== PRODUÇÃO DO RELATÓRIO:==============
# Para a entrega completa deste LAB03 você precisa colar o código corrigido com os TODOs preenchidos, a acurácia obtida e responder:
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dataset de Suporte Técnico
dados_tech = {
    'mensagem': [
        'Esqueci minha senha de acesso', 'Não consigo entrar no sistema', 'Como redefinir minha senha?',
        'A internet esta muito lenta', 'Sem conexao de rede no escritorio', 'Minha conexao caindo toda hora',
        'Impressora nao esta funcionando', 'Nao consigo imprimir documentos', 'Impressora travada com papel'
    ],
    'intencao': [
        'reset_senha', 'reset_senha', 'reset_senha',
        'problema_conexao', 'problema_conexao', 'problema_conexao',
        'suporte_impressora', 'suporte_impressora', 'suporte_impressora'
    ]
}

df3 = pd.DataFrame(dados_tech)

# TODO 1: Separe o dataset em X (coluna 'mensagem') e y (coluna 'intencao')
X = df3['mensagem']
y = df3['intencao']

# TODO 2: Realize a divisão em treino (70%) e teste (30%) com random_state=42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state=42)

# TODO 3: Instancie o CountVectorizer e ajuste/transforme os dados de treino e teste
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# TODO 4: Instancie o DecisionTreeClassifier e treine o modelo com .fit()
modelo_arvore = DecisionTreeClassifier(random_state=42)
modelo_arvore.fit(X_train_vec, y_train)

# TODO 5: Gere as predições para o X_test_vec e exiba a acurácia
predicoes = modelo_arvore.predict(X_test_vec)
acuracia = accuracy_score(y_test, predicoes)
print(f"Acurácia do Modelo: {acuracia * 100:.2f}%")

# 1 - Qual foi a acurácia obtida pelo modelo no conjunto de teste e por que, em um dataset tão pequeno (9 exemplos), essa métrica pode ser enganosa?
Acurácia do Modelo: 33.33% , entendo que uma base pequena de dataset entrega menos confiabilidade para a decisão tomada pela Arvores de Decisão.
# 2 - Como o modelo de Árvore de Decisão (DecisionTreeClassifier) toma a decisão de separar as intenções do usuário?
Criando uma estrutura hierárquica de dados, "Se/ Senão"
# 3 - Qual é o risco de utilizar uma Árvore de Decisão sem limite de profundidade (max_depth) em datasets de texto maiores?
Como o texto gera milhares de palavras , a árvore cresce até decorar o treino decorando regras irrelevantes.
