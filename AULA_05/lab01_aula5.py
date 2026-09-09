#Instalando o modelo
!python -m spacy download pt_core_news_sm

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import spacy
from nltk.corpus import stopwords
#from gensim.models import FastText
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

nltk.download("stopwords", quiet=True)

stop_words_pt = set(stopwords.words("portuguese"))

nlp = spacy.load("pt_core_news_sm")

print("Ambiente preparado com sucesso.")

def limpar_e_lemmatizar(texto):
  """
  Realiza o pré-processamento de uma mensagem:
  
  1. Converte para minúsculas
  2. Remove caracteres especiais e números
  3. Processa o texto com spaCy
  4. Remove stopwords
  5. Realiza lemmatization
  6. Retorna o texto normalizado
  """
  
  # 1. Converter para minúsculas
  texto_limpo = texto.lower()
  
  # 2. Remover caracteres especiais e números
  texto_limpo = re.sub(
      r'[^a-záàâãéèêíïóôõöúçñ\s]',
      '',
      texto_limpo
  )
  
  # 3. Processar o texto com spaCy
  doc = nlp(texto_limpo)
  
  # 4. Extrair os lemas
  tokens_filtrados = []
  
  for token in doc:
      
      # Ignorar espaços
      if token.is_space:
          continue
      
      # Ignorar stopwords
      if token.text in stop_words_pt:
          continue
      
      # Ignorar tokens muito pequenos
      if len(token.text) <= 1:
          continue
      
      # Adicionar o lema
      tokens_filtrados.append(token.lemma_)
  
  # 5. Reconstruir a frase
  return " ".join(tokens_filtrados)

def analise_pocessamento(texto):
  texto_original = texto
  texto_limpo = texto.lower()

  texto_limpo = re.sub(
        r'[^a-záàâãéèêíïóôõöúçñ\s]',
        '',
        texto_limpo
  )

  doc_original = nlp(texto_limpo)

  token_antes = [
      token.text
      for token in doc_original
      if not token.is_space
  ]

  texto_normalizado = limpar_e_lemmatizar(texto)

  tokens_finais = texto_normalizado.split()

  tokens_removidos = [
      token
      for token in token_antes
      if token not in tokens_finais
  ]

  # Exibir diagnóstico
  print("Texto original:")
  print(texto_original)

  print("\nTexto normalizado:")
  print(texto_normalizado)

  print("\nQuantidade de caracteres:")
  print(len(texto_original))

  print("\nQuantidade de tokens antes:")
  print(len(token_antes))

  print("\nQuantidade de tokens depois:")
  print(len(tokens_finais))

  print("\nTokens removidos:")
  print(tokens_removidos)

  print("\nTokens finais:")
  print(tokens_finais)

frase_teste = (
    "Gostaria de saber se vocês estão DEVOLVENDO "
    "os valores das mesas compradas!!!"
)

resultado = limpar_e_lemmatizar(frase_teste)

print("Frase original:")
print(frase_teste)

print("\nFrase processada:")
print(resultado)

analise_pocessamento(
    "MEU sofá!!! chegou quebrado e quero DEVOLVER!!!"
)
