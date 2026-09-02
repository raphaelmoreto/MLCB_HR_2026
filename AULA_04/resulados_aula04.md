# ==============================================================================
# ATIVIDADE 1: CHATBOT VERSÃO 1 (KNN)
# ==============================================================================
                precision    recall  f1-score   support

     consultas       1.00      0.75      0.86         8
financiamentos       0.78      1.00      0.88         7
 investimentos       1.00      1.00      1.00         8
    pagamentos       1.00      1.00      1.00         7

      accuracy                           0.93        30
     macro avg       0.94      0.94      0.93        30
  weighted avg       0.95      0.93      0.93        30

[[6 2 0 0]
 [0 7 0 0]
 [0 0 8 0]
 [0 0 0 7]]

=== INICIANDO BATERIA DE TESTES (10 INPUTS OBRIGATÓRIOS) ===

[Teste 1/10]
Digite a frase do cliente: estou com sono
Intenção: ['financiamentos']
Probabilidade: 100.00%

[Teste 2/10]
Digite a frase do cliente: quero comprar um hamburguer
Intenção: ['financiamentos']
Probabilidade: 100.00%

[Teste 3/10]
Digite a frase do cliente: quero fazer um financiamento
Intenção: ['financiamentos']
Probabilidade: 100.00%

[Teste 4/10]
Digite a frase do cliente: quero pagar o meu boleto
Intenção: ['pagamentos']
Probabilidade: 100.00%

[Teste 5/10]
Digite a frase do cliente: quero ver o meu saldo
Intenção: ['consultas']
Probabilidade: 100.00%

[Teste 6/10]
Digite a frase do cliente: quero assistir o jogo do Péle
Intenção: ['pagamentos']
Probabilidade: 66.67%

[Teste 7/10]
Digite a frase do cliente: quero aplicar investimentos
Intenção: ['investimentos']
Probabilidade: 100.00%

[Teste 8/10]
Digite a frase do cliente: preciso calcular o meu imposto de renda
Intenção: ['consultas']
Probabilidade: 66.67%

[Teste 9/10]
Digite a frase do cliente: quero abrir uma conta
Intenção: ['consultas']
Probabilidade: 66.67%

[Teste 10/10]
Digite a frase do cliente: palmeiras não tem mundial
FALLBACK: encaminhando para atendimento humano...

# ==============================================================================
# ATIVIDADE 2: Construção do Zero (Versão 2 — Decision Tree e 8 Testes Digitados)
# ==============================================================================
precision    recall  f1-score   support

     consultas       1.00      1.00      1.00         8
financiamentos       1.00      0.86      0.92         7
 investimentos       1.00      0.75      0.86         8
    pagamentos       0.70      1.00      0.82         7

      accuracy                           0.90        30
     macro avg       0.93      0.90      0.90        30
  weighted avg       0.93      0.90      0.90        30


<img width="910" height="690" alt="image" src="https://github.com/user-attachments/assets/06dd54bd-d36f-4b1a-b910-f77e854a80d5" />

# ==============================================================================
# ATIVIDADE 3: Relatório Comparativo de Modelos
# ==============================================================================

# Relatório de Avaliação NLU - SAC Móveis Residenciais

## 1. Tabela Comparativa de Métricas (Dados de Teste)

| Modelo            | Acurácia Geral | F1-Score (Weighted) | Principais Erros na Matriz                                        |
| :---------------- | :------------: | :-----------------: | :---------------------------------------------------------------- |
| **KNN (K=3)**     |     **93%**    |       **0.93**      | Confusão entre `consultas` e `financiamentos`                     |
| **Decision Tree** |     **90%**    |       **0.90**      | Erros envolvendo `financiamentos`, `investimentos` e `pagamentos` |

### Análise das métricas

O modelo **KNN (K=3)** apresentou acurácia de **93%** e F1-Score Weighted de **0.93**. Dos 30 exemplos utilizados no conjunto de teste, o modelo classificou corretamente 28 e apresentou 2 classificações incorretas.

Na matriz de confusão do KNN, observa-se que a principal confusão ocorreu na classe `consultas`, que apresentou **6 classificações corretas e 2 classificações incorretas**. As demais classes (`financiamentos`, `investimentos` e `pagamentos`) foram classificadas corretamente nos dados de teste.

O modelo **Decision Tree** apresentou acurácia de **90%** e F1-Score Weighted de **0.90**. Dos 30 exemplos de teste, 27 foram classificados corretamente.

Na Decision Tree, a classe `consultas` apresentou o melhor resultado, com **100% de precision, recall e F1-Score**. A classe `financiamentos` apresentou recall de **0.86**, enquanto `investimentos` apresentou recall de **0.75**. A classe `pagamentos` apresentou recall de **1.00**, porém teve precision de **0.70**, indicando que algumas frases classificadas como pagamentos pertenciam a outras classes.

Comparando os dois modelos, o **KNN apresentou melhor desempenho geral**, obtendo 93% de acurácia e F1-Score Weighted de 0.93, contra 90% e 0.90 da Decision Tree.

---

## 2. Análise dos Testes de Entrada (`input()`)

### Comportamento do KNN (10 testes)

Foram realizados 10 testes manuais utilizando frases digitadas pelo usuário.

O KNN apresentou alta confiança em várias frases, chegando a **100% de probabilidade**, mesmo em algumas entradas que não estavam diretamente relacionadas às intenções do dataset.

Nos testes realizados:

* `"estou com sono"` → `financiamentos`, 100%;
* `"quero comprar um hamburguer"` → `financiamentos`, 100%;
* `"quero fazer um financiamento"` → `financiamentos`, 100%;
* `"quero pagar o meu boleto"` → `pagamentos`, 100%;
* `"quero ver o meu saldo"` → `consultas`, 100%;
* `"quero assistir o jogo do Péle"` → `pagamentos`, 66,67%;
* `"quero aplicar investimentos"` → `investimentos`, 100%;
* `"preciso calcular o meu imposto de renda"` → `consultas`, 66,67%;
* `"quero abrir uma conta"` → `consultas`, 66,67%;
* `"palmeiras não tem mundial"` → Fallback.

Um ponto importante observado foi que o modelo classificou algumas frases que não pertenciam claramente às intenções do sistema com confiança elevada. Por exemplo, `"estou com sono"` e `"quero comprar um hamburguer"` foram classificadas como `financiamentos` com 100% de probabilidade.

Isso demonstra uma limitação importante do modelo: **uma probabilidade alta não significa necessariamente que a frase faça sentido para o domínio do chatbot**. O KNN sempre procura uma classe conhecida no conjunto de treinamento e pode acabar atribuindo uma intenção mesmo quando a entrada está fora do domínio.

O mecanismo de Fallback funcionou no décimo teste, quando a confiança ficou abaixo do limiar de 50%.

---

### Comportamento da Decision Tree (8 testes)

Foram realizados 8 testes manuais com a Decision Tree.

O modelo apresentou desempenho inferior ao KNN nos dados de teste, obtendo **90% de acurácia e F1-Score Weighted de 0.90**.

Nos testes manuais, o comportamento do modelo deve ser analisado considerando principalmente as probabilidades retornadas pelo `predict_proba` e o limiar de **50%** utilizado para acionar o Fallback.

A utilização do Fallback é importante porque permite que o sistema encaminhe para um atendente humano as solicitações nas quais o modelo não apresenta confiança suficiente para determinar a intenção.

Assim como no KNN, a Decision Tree pode apresentar classificações incorretas quando recebe frases muito diferentes dos exemplos utilizados durante o treinamento. Portanto, o resultado dos testes manuais deve ser considerado junto às métricas obtidas no conjunto de teste.

---

## 3. Veredito Final

### Melhor modelo para este projeto

**KNN (K=3)**

### Justificativa técnica

Com base nos resultados obtidos nos dados de teste, o **KNN (K=3)** apresentou o melhor desempenho entre os dois modelos avaliados.

O KNN alcançou:

* **93% de acurácia**;
* **0.93 de F1-Score Weighted**;
* 28 classificações corretas em 30 exemplos de teste.

A Decision Tree alcançou:

* **90% de acurácia**;
* **0.90 de F1-Score Weighted**;
* 27 classificações corretas em 30 exemplos de teste.

Além das métricas estatísticas, o KNN apresentou bom desempenho na classificação das classes avaliadas, embora tenha apresentado duas confusões na classe `consultas`.

A Decision Tree apresentou erros distribuídos principalmente entre `financiamentos`, `investimentos` e `pagamentos`, apresentando recall de 75% para `investimentos` e precision de 70% para `pagamentos`.

Outro ponto observado nos testes manuais foi que ambos os modelos podem apresentar alta confiança para frases que não pertencem ao domínio esperado. Isso mostra que o Fallback baseado apenas em probabilidade possui limitações e poderia ser aprimorado em uma versão futura com técnicas de detecção de entradas fora do domínio.

Portanto, considerando as métricas obtidas e o comportamento observado, o **KNN (K=3)** foi o modelo que apresentou o melhor resultado para este experimento.
