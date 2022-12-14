# -*- coding: utf-8 -*-
"""Análise_de_Dados_e_Experimentos_Big_Data_Oficina_Maker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b2pzo_SZTjVx0KapoR_HhKQZDj313d8S

# Projeto Oficina Maker
## Estudantes: Felipe Ferro Ramires, Michael da Silva e Verônica Scheifer
## Análise de Dados e Experimentos Big Data

# **Importação**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats as sp

df = pd.read_csv("/content/2022-10-01_sigesguarda_-_Base_de_Dados.csv", sep=';', encoding='ISO-8859-1')

"""# **Informação do dataset**"""

df.head()

df.info()

df.describe()

"""# **Tratamento de dados**

Contagem de dados nulos
"""

def contagemNulos(tabela):
  for col in tabela.columns:
   if tabela[col].isnull().sum():
    total_null=tabela[col].isnull().sum() 
    print('Column: {} total null {}, i.e. {} %'.format(col,total_null,round(total_null*100/len(df),2)))

dfContagemNulos = contagemNulos(df)

"""## **Análise de variáveis com quantidades agrupadas**

- Tratmentos de dados e criação de um dataframe com as quantidades agrupadas
"""

df['OCORRENCIA_DATA'] = pd.to_datetime(df.OCORRENCIA_DATA, format='%Y-%m-%d')

df['OCORRENCIA_DATA'] = df['OCORRENCIA_DATA'].dt.strftime('%Y-%m-%d')

df['OCORRENCIA_DATA']

df2 = df.groupby(['ATENDIMENTO_ANO','OCORRENCIA_ANO', "ATENDIMENTO_BAIRRO_NOME", "FLAG_FLAGRANTE", "NATUREZA1_DESCRICAO", "OCORRENCIA_DATA", "OCORRENCIA_DIA_SEMANA", "REGIONAL_FATO_NOME" ])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

df2

"""- Quantidade de ocorrencias atendidas por ano (ATENDIMENTO_ANO)"""

ocorrenciasAtendidasPorAno = df.groupby(['ATENDIMENTO_ANO'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasAtendidasPorAno = ocorrenciasAtendidasPorAno.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Atendidas_Por_Ano'}, axis=1)

ocorrenciasAtendidasPorAno

ocorrenciasAtendidasPorAno.describe()

"""- Quantidade de ocorrencias registradas por ano (OCORRENCIA_ANO)"""

ocorrenciasRegistradasPorAno = df.groupby(['OCORRENCIA_ANO'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasRegistradasPorAno = ocorrenciasRegistradasPorAno.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Registradas_Por_Ano'}, axis=1)

ocorrenciasRegistradasPorAno

ocorrenciasRegistradasPorAno.describe()

"""- Quantidade de ocorrencias por bairro (ATENDIMENTO_BAIRRO_NOME)"""

ocorrenciasPorBairro = df.groupby(['ATENDIMENTO_BAIRRO_NOME'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasPorBairro = ocorrenciasPorBairro.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Registradas_Por_Bairro'}, axis=1)

ocorrenciasPorBairro

ocorrenciasPorBairro.describe()

"""- Quantidade de ocorrencias com flagrante (FLAG_FLAGRANTE)"""

ocorrenciasFlagrante = df.groupby(['FLAG_FLAGRANTE'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasFlagrante = ocorrenciasFlagrante.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Flagrante'}, axis=1)

ocorrenciasFlagrante

"""- Quantidade de ocorrencias por tipo (NATUREZA1_DESCRICAO)"""

ocorrenciasPorTipo = df.groupby(['NATUREZA1_DESCRICAO'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasPorTipo = ocorrenciasPorTipo.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Por_Tipo'}, axis=1)

ocorrenciasPorTipo

ocorrenciasPorTipo.describe()

"""- Quantidade de ocorrencias por dia (OCORRENCIA_DATA)"""

ocorrenciasPorDia = df.groupby(['OCORRENCIA_DATA'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasPorDia = ocorrenciasPorDia.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Por_Dia'}, axis=1)

ocorrenciasPorDia

ocorrenciasPorDia.describe()

"""- Quantidade de ocorrencias por dia da semana (OCORRENCIA_DIA_SEMANA)"""

ocorrenciasPorDiaDaSemana = df.groupby(['OCORRENCIA_DIA_SEMANA'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasPorDiaDaSemana = ocorrenciasPorDiaDaSemana.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Por_Dia_Da_Semana'}, axis=1)

ocorrenciasPorDiaDaSemana

"""- Quantidade de ocorrencias por regional (REGIONAL_FATO_NOME)"""

ocorrenciasPorRegional = df.groupby(['REGIONAL_FATO_NOME'])['QUANTIDADE_OCORRENCIA'].sum().reset_index()

ocorrenciasPorRegional = ocorrenciasPorRegional.rename({'QUANTIDADE_OCORRENCIA': 'Quantidade_Ocorrencias_Por_Regional'}, axis=1)

ocorrenciasPorRegional

"""# **Análise descritiva de dados**"""

tabelas = [ocorrenciasAtendidasPorAno, ocorrenciasRegistradasPorAno, ocorrenciasPorBairro, ocorrenciasFlagrante,
           ocorrenciasPorTipo, ocorrenciasPorDia, ocorrenciasPorDiaDaSemana, ocorrenciasPorRegional]

"""### - Medidas de posição"""

#Média

def calculaMedia(tabela):

    media = tabela.mean()

    media = pd.DataFrame({'metricas':media.index, 'media':media.values})
    
    return media

medias = []
for i in tabelas: 
  medias.append(calculaMedia(i))
  
dfMedia = pd.concat(medias)
dfMedia

#Mediana

def calculaMediana(tabela):

    mediana = tabela.median()

    mediana = pd.DataFrame({'metricas':mediana.index, 'mediana':mediana.values})
    
    return mediana

medianas = []
for i in tabelas: 
  medianas.append(calculaMediana(i))
  
dfMediana = pd.concat(medianas)
dfMediana

"""### - Medidas de dispersão"""

#Variancia (valores ao quadrado)
#Distância dos termos com relação a média
#Quanto menor, melhor e mais próximo a média

def calculaVariancia(tabela):

    var = tabela.var()

    var = pd.DataFrame({'metricas':var.index, 'var':var.values})
    
    return var

variancias = []
for i in tabelas: 
  variancias.append(calculaVariancia(i))
  
dfVariancia = pd.concat(variancias)
dfVariancia

#Desvio Padrao (√ Variancia - mesma unidade media)
#Distância dos termos com relação a média
#Quanto menor, melhor e mais próximo a média

def calculateDesvioPadrao(tabela):

    desvioP = tabela.std()

    desvioP = pd.DataFrame({'metricas':desvioP.index, 'desvioP':desvioP.values})

    return desvioP

desvios = []
for i in tabelas: 
  desvios.append(calculateDesvioPadrao(i))
  
dfDesvio = pd.concat(desvios)
dfDesvio

#Quantis
def calculaQuantil(tabela):

    q1 = tabela.quantile(0.25)
    q1Df = pd.DataFrame({'metricas':q1.index, 'q1':q1.values})

    q2 = tabela.quantile(0.50)
    q2Df = pd.DataFrame({'metricas':q2.index, 'q2':q1.values})

    q3 = tabela.quantile(0.75)
    q3Df = pd.DataFrame({'metricas':q3.index, 'q3':q3.values})

    quantile = pd.concat([q1Df['metricas'], q1Df['q1'], q2Df['q2'], q3Df['q3']], axis=1, ignore_index=True)
    quantile.columns = ['metricas', 'quantil1(25%)', 'quantil2(50%)', 'quantil3(75%)']
    
    return quantile

quantis = []
for i in tabelas: 
  quantis.append(calculaQuantil(i))
  
dfQuantis = pd.concat(quantis)
dfQuantis

"""# **Funções para os gráficos**"""

def criaHistogramaComBins(title, table, bins, color, collumn = None):

    plt.figure(figsize=(10,5))

    plt.title(title, fontsize =13)

    if collumn is None: 

        plt.hist((table), bins = np.array(bins), alpha = 0.8, color = color)

    else:

        plt.hist((table[collumn]), bins = np.array(bins), alpha = 0.8, color = color)
        
    plt.show

def plotScatter(collumnX, collumnY, table, title, color):
    
    sns.set_style('white')

    plt.figure(figsize= (10, 10))

    plt.title(title, fontsize = 13)

    sns.scatterplot(x=collumnX, y=collumnY, data= table, color = color)

    plt.show()

def criaGraficoPizza(table, y, label, title):
    mycolors = ['plum', 'bisque']

    plt.figure(figsize=(15,10), dpi=80)

    plt.pie(table[y], labels = table[label], autopct = '%1.1f%%', colors = mycolors, frame = False)

    #plt.legend()

    plt.title(title)

    plt.rcParams['axes.facecolor'] = 'white'

    plt.show()

def criaGraficoLinha(table, x, y, title, xLabel, yLabel):
    plt.figure(figsize=(10,5))

    plt.plot(table[x], table[y])

    plt.title(title)

    plt.xlabel(xLabel)

    plt.ylabel(yLabel)
    
    plt.show()

def criaGraficoDistribuicao(table, coluna):
    plt.figure(figsize=(10,5))
    sns.distplot(table[coluna])

def criaGraficoBoxplot(table, x):
    plt.figure(figsize=(10,5))
    sns.boxplot(data=table, x=x)

"""# **Visualizações dos dados**

####**Ocorrencias Atendidas Por Ano**
"""

criaGraficoLinha(ocorrenciasAtendidasPorAno, 'ATENDIMENTO_ANO', 'Quantidade_Ocorrencias_Atendidas_Por_Ano', 'Quantidade_Ocorrencias_Atendidas_Por_Ano', 'ATENDIMENTO_ANO', 'Quantidade Ocorrencias')

criaGraficoDistribuicao(ocorrenciasAtendidasPorAno, 'Quantidade_Ocorrencias_Atendidas_Por_Ano')

criaGraficoBoxplot(ocorrenciasAtendidasPorAno, 'Quantidade_Ocorrencias_Atendidas_Por_Ano')

bins = [500, 10000, 20000, 30000, 40000]

criaHistogramaComBins('Quantidade_Ocorrencias_Atendidas_Por_Ano', ocorrenciasAtendidasPorAno, bins, 'mediumaquamarine', 'Quantidade_Ocorrencias_Atendidas_Por_Ano')

bins = [50000, 60000, 70000, 80000, 100000]

criaHistogramaComBins('Quantidade_Ocorrencias_Atendidas_Por_Ano', ocorrenciasAtendidasPorAno, bins, 'mediumaquamarine', 'Quantidade_Ocorrencias_Atendidas_Por_Ano')

"""####**Ocorrencias Registradas Por Ano**

"""

criaGraficoLinha(ocorrenciasRegistradasPorAno, 'OCORRENCIA_ANO', 'Quantidade_Ocorrencias_Registradas_Por_Ano', 'Quantidade_Ocorrencias_Registradas_Por_Ano', 'OCORRENCIA_ANO', 'Quantidade Ocorrencias')

criaGraficoDistribuicao(ocorrenciasRegistradasPorAno, 'Quantidade_Ocorrencias_Registradas_Por_Ano')

criaGraficoBoxplot(ocorrenciasRegistradasPorAno, 'Quantidade_Ocorrencias_Registradas_Por_Ano')

bins = [500, 10000, 20000, 30000, 40000]

criaHistogramaComBins('Quantidade_Ocorrencias_Registradas_Por_Ano', ocorrenciasRegistradasPorAno, bins, 'mediumaquamarine', 'Quantidade_Ocorrencias_Registradas_Por_Ano')

bins = [50000, 60000, 70000, 80000, 100000]

criaHistogramaComBins('Quantidade_Ocorrencias_Registradas_Por_Ano', ocorrenciasRegistradasPorAno, bins, 'mediumaquamarine', 'Quantidade_Ocorrencias_Registradas_Por_Ano')

"""####**Ocorrencias Por Bairro**

"""

criaGraficoDistribuicao(ocorrenciasPorBairro, 'Quantidade_Ocorrencias_Registradas_Por_Bairro')

criaGraficoBoxplot(ocorrenciasPorBairro, 'Quantidade_Ocorrencias_Registradas_Por_Bairro')

bins = [500, 10000, 20000, 30000, 40000]

criaHistogramaComBins('Quantidade_Ocorrencias_Registradas_Por_Bairro', ocorrenciasPorBairro, bins, 'mediumaquamarine', 'Quantidade_Ocorrencias_Registradas_Por_Bairro')

bins = [50000, 60000, 70000, 80000, 100000]

criaHistogramaComBins('Quantidade_Ocorrencias_Registradas_Por_Bairro', ocorrenciasPorBairro, bins, 'mediumaquamarine', 'Quantidade_Ocorrencias_Registradas_Por_Bairro')

"""####**Ocorrencias Flagrante**"""

quantidadeOcorrenciasFlagranteGraficoPizza = criaGraficoPizza(ocorrenciasFlagrante, 'Quantidade_Ocorrencias_Flagrante', 'FLAG_FLAGRANTE', 'Quantidade_Ocorrencias_Flagrante')

"""####**Ocorrencias Por Tipo**

"""

criaGraficoDistribuicao(ocorrenciasPorTipo, 'Quantidade_Ocorrencias_Por_Tipo')

criaGraficoBoxplot(ocorrenciasPorTipo, 'Quantidade_Ocorrencias_Por_Tipo')

"""####**Ocorrencias Por Dia**

"""

criaGraficoDistribuicao(ocorrenciasPorDia, 'Quantidade_Ocorrencias_Por_Dia')

criaGraficoBoxplot(ocorrenciasPorDia, 'Quantidade_Ocorrencias_Por_Dia')

"""####**Ocorrencias Por Dia Da Semana**

"""

criaGraficoLinha(ocorrenciasPorDiaDaSemana, 'OCORRENCIA_DIA_SEMANA', 'Quantidade_Ocorrencias_Por_Dia_Da_Semana', 'Quantidade_Ocorrencias_Por_Dia_Da_Semana', 'OCORRENCIA_DIA_SEMANA', 'Quantidade Ocorrencias')

criaGraficoDistribuicao(ocorrenciasPorDiaDaSemana, 'Quantidade_Ocorrencias_Por_Dia_Da_Semana')

criaGraficoBoxplot(ocorrenciasPorDiaDaSemana, 'Quantidade_Ocorrencias_Por_Dia_Da_Semana')

"""####**Ocorrencias Por Regional**"""

criaGraficoDistribuicao(ocorrenciasPorRegional, 'Quantidade_Ocorrencias_Por_Regional')

criaGraficoBoxplot(ocorrenciasPorRegional, 'Quantidade_Ocorrencias_Por_Regional')









"""# **Análises com Spark**

### **Configurando o Spark**
"""

# install java
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

# install spark (change the version number if needed)
!wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz

# unzip the spark file to the current folder
!tar xf spark-3.0.0-bin-hadoop3.2.tgz

# set your spark folder to your system path environment. 
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"


# install findspark using pip
!pip install -q findspark

import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local")\
        .appName("Colab")\
        .config('spark.ui.port', '4050')\
        .getOrCreate()

"""### **Informação do dataset**"""

sparkDF=spark.createDataFrame(df2) 
sparkDF.printSchema()
sparkDF.show()

sparkDF.head()

sparkDF.describe().show()

sparkDF.printSchema()

"""### **Tratamento de dados**

- Contagem de linhas duplicadas
"""

import pyspark.sql.functions as funcs
sparkDF.groupby(sparkDF.columns).count().where(funcs.col('count') > 1).select(funcs.sum('count')).show()

"""- Achar colunas numericas e categoricas"""

colunas_numericas = list()
colunas_categoricas = list()
for col_ in sparkDF.columns:
    if sparkDF.select(col_).dtypes[0][1] != "string":
        colunas_numericas.append(col_)
    else:
        colunas_categoricas.append(col_)
        
print("Colunas Numericas",colunas_numericas)
print("Colunas Categoricas",colunas_categoricas)

"""- Contagem de valores nulos"""

from pyspark.sql.functions import *
print(sparkDF.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in sparkDF.columns]).show())

"""### **Análise descritiva de dados**

Métricas
"""

sparkDF.summary().show()