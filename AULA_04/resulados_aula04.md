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
