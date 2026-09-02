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

# 1 - Qual foi a acurácia obtida pelo modelo no conjunto de teste e por que, em um dataset tão pequeno (9 exemplos), essa métrica pode ser enganosa?
Acurácia do Modelo: 33.33% , entendo que uma base pequena de dataset entrega menos confiabilidade para a decisão tomada pela Arvores de Decisão.
# 2 - Como o modelo de Árvore de Decisão (DecisionTreeClassifier) toma a decisão de separar as intenções do usuário?
Criando uma estrutura hierárquica de dados, "Se/ Senão"
# 3 - Qual é o risco de utilizar uma Árvore de Decisão sem limite de profundidade (max_depth) em datasets de texto maiores?
Como o texto gera milhares de palavras , a árvore cresce até decorar o treino decorando regras irrelevantes.

--- RESULTADOS DO LAB 04 ---

==================================================
DATASET
==================================================
                                             mensagem          intencao
0             Quero comprar uma passagem para Orlando  comprar_passagem
1           Gostaria de reservar um voo para Salvador  comprar_passagem
2      Qual o preço da passagem de avião para Lisboa?  comprar_passagem
3   Preciso comprar bilhete aéreo para o Rio de Ja...  comprar_passagem
4       Como faço para cancelar minha reserva de voo?  cancelar_reserva
5          Quero pedir o cancelamento da minha viagem  cancelar_reserva
6         Gostaria de anular minha compra de passagem  cancelar_reserva
7        Preciso cancelar meu voo marcado para amanhã  cancelar_reserva
8       Quero falar com um atendente humano por favor   falar_atendente
9       Pode me transferir para o suporte ao cliente?   falar_atendente
10     Preciso de ajuda com uma pessoa do atendimento   falar_atendente
11   Gostaria de conversar com um operador da agência   falar_atendente

==================================================
DIVISÃO DOS DADOS
==================================================
Quantidade de frases para treinamento: 9
Quantidade de frases para teste: 3

==================================================
AVALIAÇÃO DO MODELO
==================================================
Acurácia no conjunto de teste: 33.33%

==================================================
MOTOR DE NLU - AGÊNCIA DE VIAGENS
==================================================
Acurácia do modelo: 33.33%

--- PREDIÇÃO DE MENSAGENS INÉDITAS ---

Mensagem: 'Gostaria de saber o valor para voar até Paris'
==> Intenção Predita: [comprar_passagem]

Mensagem: 'Quero cancelar o bilhete que comprei ontem'
==> Intenção Predita: [cancelar_reserva]

Mensagem: 'Me transfira para um suporte humano, por favor'
==> Intenção Predita: [falar_atendente]

==================================================
FIM DO PROGRAMA
==================================================
