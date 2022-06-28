#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt


# In[7]:


notas = pd.read_csv("Dataset/ratings.csv")
filmes = pd.read_csv("Dataset/movies.csv")


# In[18]:


notas.columns = ["UsuarioId", "FilmeId", "Avaliacao", "timestamp"]
notas.drop(["timestamp"], axis=1, inplace=True)
notas.head()


# In[20]:


filmes.columns = ["FilmeId", "NomeFilme", "Genero"]
filmes.head()


# 
