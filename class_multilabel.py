#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:01:43 2021

@author: rfx
"""

import pandas as pd
perguntas = pd.read_csv("dataset/stackoverflow_perguntas.csv")
#classificação binária temos duas possibilidades 
print(len(perguntas))#quantas linhas que temos no dataframe

print(len(perguntas.Tags.unique())) #aqui temos todas as combinações de tags no dataframe 

print(perguntas.Tags.unique())

#realizar uma transformação 
lista_de_tags = list()
for tags in perguntas.Tags.unique():
    for tag in tags.split():
        if tag not in lista_de_tags:
            lista_de_tags.append(tag)
            
print(lista_de_tags)
    
"node.js html".split()
#transformando labels em colunas
node_js = list()
for linha_tag in perguntas.Tags:
    if "node.js" in linha_tag:
        node_js.append(1)
    else:
        node_js.append(0)
        
perguntas["node.js"] = node_js

def nova_coluna(lista_tags, dataframe, nome_tags):
    for tag in lista_tags:
        coluna = list()
        for linha_tag in dataframe[nome_tags]:
            if tag in linha_tag:
                coluna.append(1)
            else:
                coluna.append(0)
        dataframe[tag] = coluna 
nova_coluna(lista_de_tags, perguntas, "Tags")
perguntas.sample(10)

from sklearn.model_selection import train_test_split

perguntas_treino, perguntas_test, tags_treino, tags_test = train_test_split(
    perguntas.Perguntas,
    perguntas.todas_tags,
    test_size = 0.2,
    random_state = 123)

lista_1 = [1,2]
lista_2 = [5,4]
lista_zip = zip(lista_1, lista_2)
print(list(lista_zip))

lista_zip_tags = list(zip(perguntas[lista_de_tags[0]], perguntas[lista_de_tags[1]],
                     perguntas[lista_de_tags[2]], perguntas[lista_de_tags[3]]))
perguntas["todas_tags"] = lista_zip_tags 

perguntas_treino





