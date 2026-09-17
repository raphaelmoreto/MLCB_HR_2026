--- Exercício 1 — Construção da Esteira de Pré-processamento ---

Collecting pt-core-news-sm==3.8.0
  Downloading https://github.com/explosion/spacy-models/releases/download/pt_core_news_sm-3.8.0/pt_core_news_sm-3.8.0-py3-none-any.whl (13.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.0/13.0 MB 49.2 MB/s eta 0:00:00
Installing collected packages: pt-core-news-sm
Successfully installed pt-core-news-sm-3.8.0
✔ Download and installation successful
You can now load the package via spacy.load('pt_core_news_sm')
⚠ Restart to reload dependencies
If you are in a Jupyter or Colab notebook, you may need to restart Python in
order to load all the package's dependencies. You can do this by selecting the
'Restart kernel' or 'Restart runtime' option.
Ambiente preparado com sucesso.
Frase original:
Gostaria de saber se vocês estão DEVOLVENDO os valores das mesas compradas!!!

Frase processada:
gostar saber devolver valor meso comprada
Texto original:
MEU sofá!!! chegou quebrado e quero DEVOLVER!!!

Texto normalizado:
sofá chegar quebrar querer devolver

Quantidade de caracteres:
47

Quantidade de tokens antes:
7

Quantidade de tokens depois:
5

Tokens removidos:
['meu', 'chegou', 'quebrado', 'e', 'quero']

Tokens finais:
['sofá', 'chegar', 'quebrar', 'querer', 'devolver']

#=============================================||=========================================

---

EXERCÍCIO 2 - SENTENCE EMBEDDINGS + MEAN POOLING ---

============================================================
DATASET CARREGADO COM SUCESSO
============================================================
Quantidade de registros: 80

Colunas disponíveis:
['mensagem', 'intencao']

Primeiras linhas:
None
Like what you see? Visit the data table notebook to learn more about interactive tables.
1 to 5 of 5 entries
Filter

index mensagem intencao
0 Meu pedido está atrasado logistica_entregas
1 Quero devolver este sofá que chegou com rasgo trocas_devolucoes
2 Qual o prazo de entrega do sofá que comprei? logistica_entregas
3 Quero consultar o status da entrega logistica_entregas
4 Recebi um armário com peças quebradas e quero devolver trocas_devolucoes
Show
25
per page
Like what you see? Visit the data table notebook to learn more about interactive tables.

============================================================
CARREGANDO MODELO DE EMBEDDINGS
============================================================
Modelo: glove-wiki-gigaword-50
A primeira execução pode levar alguns minutos...
[==================================================] 100.0% 66.0/66.0MB downloaded

Modelo carregado com sucesso!
Dimensão dos vetores: 50

============================================================
RESULTADO DO MEAN POOLING
============================================================
Formato da Matriz de Vetores Densos (Exemplos, Dimensões): (80, 50)
Quantidade de mensagens: 80
Dimensão de cada vetor: 50

Exemplo do primeiro vetor:
[ 0.03580334 -0.00656666 -0.00654334 -0.27905166 -0.34923998 -0.8410566
0.70792 0.18564034 0.6604653 0.18762334 0.32517666 -0.15048333
0.85067004 0.12161667 -0.05653999 -0.52796 -0.12249666 0.05662167
0.6182367 0.5360667 -0.9704733 -0.64024335 0.16702199 -0.00810333
0.59204 0.7011333 -0.796985 0.29518002 0.30173 0.01335667
-0.56295663 -0.29436123 -0.4395 1.11531 -0.441888 -0.20111334
0.8851867 0.15324266 0.00986399 0.19261633 0.14949434 -0.54722667
0.16618668 -0.6791057 0.03916783 -1.0168201 0.2638437 -0.31577
0.5223133 1.0195934 ]

Primeiras 10 dimensões do primeiro vetor:
[ 0.03580334 -0.00656666 -0.00654334 -0.27905166 -0.34923998 -0.8410566
0.70792 0.18564034 0.6604653 0.18762334]

#=============================================||=========================================

--- EXERCÍCIO 3 - REGRESSÃO LOGÍSTICA + FALLBACK ---

Carregando modelo de Embeddings...
Modelo carregado com sucesso!

Colunas do dataset:

- mensagem
- intencao

Coluna utilizada como target: intencao

Distribuição das intenções:
intencao
logistica_entregas 20
trocas_devolucoes 20
vendas_orcamento 20
suporte_tecnico 20
Name: count, dtype: int64

Formato da matriz X:
(80, 50)

Modelo de Regressão Logística treinado com sucesso!

Classes identificadas:
['logistica_entregas' 'suporte_tecnico' 'trocas_devolucoes'
'vendas_orcamento']

---

Frase: Quero saber o valor do frete do sofá
Resultado: FALLBACK_HUMANO
Confiança: 42.56%

---

Frase: Gostaria de ver receitas de bolo de cenoura
Resultado: vendas_orcamento
Confiança: 71.59%

#=============================================||=========================================

--- EXERCÍCIO 4 - KNN ---

Modelo KNN treinado com sucesso!
============================================================
COMPARAÇÃO DOS MODELOS
============================================================
Acurácia - Regressão Logística (Linear): 82.50%
Acurácia - KNN (Distância K=3): 61.25%
mensagem	real	regressao_logistica	knn
0	Meu pedido está atrasado	logistica_entregas	logistica_entregas	logistica_entregas
1	Quero devolver este sofá que chegou com rasgo	trocas_devolucoes	trocas_devolucoes	trocas_devolucoes
2	Qual o prazo de entrega do sofá que comprei?	logistica_entregas	trocas_devolucoes	logistica_entregas
3	Quero consultar o status da entrega	logistica_entregas	logistica_entregas	logistica_entregas
4	Recebi um armário com peças quebradas e quero ...	trocas_devolucoes	trocas_devolucoes	trocas_devolucoes
5	Como faço para rastrear meu pedido?	logistica_entregas	logistica_entregas	logistica_entregas
6	O produto chegou diferente do que comprei	trocas_devolucoes	trocas_devolucoes	trocas_devolucoes
7	Vocês têm promoção de sofá?	vendas_orcamento	vendas_orcamento	vendas_orcamento
8	Preciso devolver a cadeira de escritório com d...	trocas_devolucoes	trocas_devolucoes	logistica_entregas
9	Meu sofá chegou rasgado, como faço a troca?	trocas_devolucoes	trocas_devolucoes	suporte_tecnico
10	Como faço a montagem do guarda roupa?	suporte_tecnico	suporte_tecnico	suporte_tecnico
11	Ainda não recebi minha mesa	logistica_entregas	logistica_entregas	suporte_tecnico
12	Quais as formas de parcelamento do rack?	vendas_orcamento	vendas_orcamento	vendas_orcamento
13	Preciso acompanhar a entrega do meu armário	logistica_entregas	logistica_entregas	suporte_tecnico
14	Quanto custa um sofá de três lugares?	vendas_orcamento	vendas_orcamento	vendas_orcamento

#=============================================||=========================================

--- PERGUNTAS ---

Questão 1 - Qual modelo apresentou melhor desempenho?
A Regressão Logística apresentou o melhor desempenho.

Questão 2 - Por que os resultados podem ser diferentes mesmo utilizando os mesmos embeddings?
Porque embedding é apenas a representação dos textos. Cada algoritmo utiliza essa representação de uma maneira diferente.

Questão 3 - O KNN utiliza distância. Por que a qualidade dos embeddings é particularmente importante para esse algoritmo?
Porque o KNN depende diretamente da distância entre os pontos.

Questão 4 - Se o sistema tivesse 100 mil mensagens e centenas de intenções, você escolheria KNN? Justifique.
Não. No KNN, para classificar uma nova mensagem, precisamos procurar mensagens próximas dentro do conjunto de dados.

Questão 5 - Qual modelo você escolheria para colocar em produção neste cenário?
Regressão Logística.