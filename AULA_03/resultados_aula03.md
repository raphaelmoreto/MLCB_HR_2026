#========== PRODUÇÃO DO RELATÓRIO:==============
# 1 - Qual o impacto da remoção de stopwords no tamanho do vocabulário do modelo?
Acaba levando em consideração muitas informações que não relevantes para o modelo.

# 2 - O que significa a configuração ngram_range=(1, 2) no TfidfVectorizer?
O 1 ele instrui o modelo a analisar as palavravas individualmente, e o 2 pares de palavras consecutivas.

# 3 - Como a remoção de palavras genéricas ajuda a evitar classificações incorretas?
Ela acaba criando palavras chaves que direcionem o modelo a interpretar da forma correta.

# Todos os resultados devem ser inseridos no arquivo resultados_aula03.md
#========== FIM ==============

--- RESULTADOS DO LAB 01 (AULA 03) ---
Mensagem: 'Preciso urgente da segunda via da fatura'
Intenção Predita: [segunda_via]
Vocabulário Filtrado (sem stopwords): ['2a', '2a via', 'aberto', 'acordo', 'acordo pagar', 'alterar', 'alterar endereço', 'app', 'atrasada', 'atualizo', 'atualizo dados', 'boleto', 'cadastramento', 'dados', 'dados residenciais', 'débito', 'débito aberto', 'dívida', 'emitir', 'emitir segunda', 'endereço', 'endereço cadastramento', 'fatura', 'fatura atrasada', 'fazer', 'fazer um', 'gostaria', 'gostaria alterar', 'negociar', 'negociar pagamento', 'no', 'no app', 'onde', 'onde atualizo', 'pagamento', 'pagamento dívida', 'pagar', 'pagar débito', 'posso', 'posso emitir', 'residenciais', 'residenciais no', 'segunda', 'segunda via', 'um', 'um acordo', 'via', 'via boleto', 'via fatura']

_____________________________________________________________

#========== PRODUÇÃO DO RELATÓRIO:==============
# 1 - O que representam as métricas Precision, Recall e F1-Score no relatório?
Precision mede o acerto do modelo de acordo com a mensagem, Recall mede a quantidade de vezes em que a mensagem se enquadrou dentro da resposta correta,
o F1 Score faz o balanceamento entre as duas métricas.

# 2 - Como interpretar a diagonal principal da Matriz de Confusão?
É onde está os acertos de acordo com o modelo apresentado.

# 3 - Por que a acurácia isolada pode ser enganosa quando temos classes desbalanceadas?
Se a maioria das mensagens direcionarem o modelo para uma resposta e ela for a certa, sua precisão será alta porém ao chegar uma mensagem diferente,
levará o modelo para a resposta errada.
# Todos os resultados devem ser inseridos no arquivo resultados_aula03.md
--- RESULTADOS DO LAB 02 (AULA 03) ---

--- Relatório de Classificação ---
                     precision    recall  f1-score   support

horario_atendimento       0.50      1.00      0.67         1
        localizacao       0.00      0.00      0.00         1
    troca_devolucao       0.00      0.00      0.00         1

           accuracy                           0.33         3
          macro avg       0.17      0.33      0.22         3
       weighted avg       0.17      0.33      0.22         3

--- Matriz de Confusão ---
[[1 0 0]
 [1 0 0]
 [0 1 0]]
#========== FIM ==============
