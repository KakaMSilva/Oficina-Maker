# -*- coding: utf-8 -*-
"""Análise_de_Dados_e_Modelagem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15NbUVAQfWwajqk0Od0TwieQE58jy1QKf

# Projeto Oficina Maker

## Estudantes: Felipe Ferro Ramires, Michael da Silva e Verônica Scheifer

## Análise de Dados e Modelagem

# **Importação**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd # importando o pandas para manipularmos o dataset
import seaborn as sns # importando o Seaborn para visualizar o comportamento dos dados
import matplotlib.pyplot as plt # importando o Matplotlib para o elbow method



from pandas_profiling import ProfileReport # importando o pandas-profiling para fazer o profile do dataset
from scipy import stats as sp
from sklearn.model_selection import train_test_split # utilizado para o split entre treinamento e teste
from sklearn.neighbors import KNeighborsRegressor # KNN para regressão
from sklearn.linear_model import LinearRegression # Regressão linear
from sklearn.svm import SVR # SVM para regressão
from sklearn.decomposition import PCA # PCA como aprendizagem não-supervisionada
from sklearn.preprocessing import RobustScaler # utilizado para que todas as entradas estejam na mesma escala numérica
from sklearn.preprocessing import StandardScaler
from pandas.core.frame import DataFrame
from matplotlib import pyplot as plt

# %matplotlib inline

df = pd.read_csv('/content/teste.csv', sep=';', encoding='ISO-8859-1')

df

df.info()

"""# **Informação do dataset**"""

df['ATENDIMENTO_BAIRRO_NOME'].value_counts()

df['NATUREZA1_DESCRICAO'].value_counts()

df['OCORRENCIA_ANO'].value_counts()

df['OCORRENCIA_DIA_SEMANA'].value_counts()

df['OCORRENCIA_MES'].value_counts()

df['OCORRENCIA_HORA'].value_counts()

df.describe()

#.median() Função Pandas retorna a mediana dos valores para o eixo solicitado.
df.median()

#.var() calcula a variância no Pandas através da função
df.var()

"""# **Tratamento de dados**

## *Limpando dados nulos*
"""

for col in df.columns:
 if df[col].isnull().sum():
  total_null=df[col].isnull().sum() 
  print('Column: {} total null {}, i.e. {} %'.format(col,total_null,round(total_null*100/len(df),2)))

#Limpando dados nulos
df.dropna(inplace = True)
df.isnull().sum()

"""## *convertendo para int*

### *OCORRENCIA_HORA*
"""

#converteu para datetime
 df['OCORRENCIA_HORA'] = pd.to_datetime(df['OCORRENCIA_HORA'])

df['OCORRENCIA_HORA'].dt.time

df['OCORRENCIA_HORA'] = df['OCORRENCIA_HORA'].dt.strftime('%H')

df['OCORRENCIA_HORA'] = df['OCORRENCIA_HORA'].astype(str).astype(int)

df['OCORRENCIA_HORA']

"""### ATENDIMENTO_BAIRRO_NOME"""

df['ATENDIMENTO_BAIRRO_NOME'] = df['ATENDIMENTO_BAIRRO_NOME'].replace({'CIDADE INDUSTRIAL':1, 'FAZENDINHA':2, 'UBERABA':3, 'SÍTIO CERCADO':4, 'TATUQUARA':5, 'SANTA CÂNDIDA':6, 'BOQUEIRÃO':7, 'CENTRO':8, 'BOA VISTA':9, 'TABOÃO':10, 'XAXIM':11, 'PILARZINHO':12, 'REBOUÇAS':13, 'ÁGUA VERDE':14, 'BATEL':15, 'NOVO MUNDO':16, 'ALTO BOQUEIRÃO':17, 'CAPÃO RASO':18, 'JARDIM BOTÂNICO':19, 'PORTÃO':20, 'ORLEANS':21, 'SANTA FELICIDADE':23, 'CASCATINHA':24, 'CAPÃO DA IMBUIA':25, 'BARREIRINHA':26, 'SEMINÁRIO':27, 'CAMPO COMPRIDO':28, 'PRADO VELHO':29, 'PINHEIRINHO':30, 'BUTIATUVINHA':31, 'CAMPINA DO SIQUEIRA':32, 'CAJURU':33, 'SÃO FRANCISCO':34, 'CENTRO CÍVICO':35, 'SÃO BRAZ':36, 'UMBARÁ':37, 'CAXIMBA':38, 'JARDIM SOCIAL':39, 'BACACHERI':40, 'CAMPO DE SANTANA':41, 'SANTO INÁCIO':42, 'JARDIM DAS AMÉRICAS':43, 'LINDÓIA':44, 'GANCHINHO':45, 'PAROLIN':46, 'ABRANCHES':47, 'SÃO JOÃO':48, 'ATUBA':49, 'TARUMÃ':50, 'ALTO DA RUA XV':51, 'MOSSUNGUÊ':52, 'TINGUI':53, 'BIGORRILHO':54, 'BAIRRO ALTO':55, 'HAUER':56, 'VILA IZABEL':57, 'CABRAL':58, 'BOM RETIRO':59, 'GUAÍRA':60, 'CACHOEIRA':61, 'AUGUSTA':62, 'CRISTO REI':63, 'AHÚ':64, 'ALTO DA GLÓRIA':65, 'GUABIROTUBA':66, 'MERCÊS':67, 'SANTA QUITÉRIA':68, 'SÃO MIGUEL':69, 'SÃO LOURENÇO':70, 'FANNY':71, 'JUVEVÊ':72, 'VISTA ALEGRE':73, 'HUGO LANGE':74, 'RIVIERA':75, 'LAMENHA PEQUENA':76, 'INDICAÇÕES CANCELADA':77, 'BAIRRO NAO INFORMADO':78, 'BAIRRO FICTÍCIO':79, 'fanny':80, 'TINGÜI':81, 'CIDADE JARDIM':82, 'VENEZA':83, 'PLANTA MEIRELES':84, 'TANGUA':85, 'MONTE REY':86, 'JD EUROPA':87, 'BORDA DO CAMPO':88, 'JARDIM BOA VISTA':89, 'SÃO JOSE':90, 'JARDIM COLONIAL':91, 'MENINO DEUS':92, 'SÃO JUDAS TADEU':93, 'VILA MARIA ANTONIETA':94, 'MARIA ANTONIETA':95, 'SANTO ANTONIO':96, 'COLOMBO':97, 'CANGUIRI':98, 'NÃO ENCONTRADO':99, 'FERRARIA':100, 'SÃO CRISTOVÃO':101, 'JD SUISSA':102, 'VILA FORMOSA':103, 'FORMOSO':104, 'SÃO PEDRO':105, 'SAO JOSE DOS PINHAIS':106, 'CAMPO PEQUENO':107, 'PINHAIS':108, 'VILA PERNETA ':109, 'SEM DADOS':110, 'CAMPO DE SÃO BENEDIT':111, 'QUATRO BARRAS':112, 'LOT. MARINONI':113, 'SÃO JORGE':114, 'BAIRRO NÃO LOCALIZAD':115, 'BRAGA':116, 'JARDIM LOANDA':117, 'NÃO INFORMADO ':118, 'SANTA TEREZINHA':119, 'SANTA TERESINHA':120, 'JARDIM WEISSOPOLIS':121, 'SITIO DAS PALMEIRAS':122, 'CAMPO PEQUENO ':123, 'NI':124, 'THOMAS COELHO':125, 'NF':126, 'SÃO THOMAS':127, 'JARDIM INDUSTRIAL':128, 'ROÇA NEGRA':129, 'SÃO THOMAZ':130, 'GRALHA AZUL':131, 'MARACANÃ':132, 'VILA BANCÁRIA':133, 'JARDIM BOM PASTOR':134, 'SAO GERONIMO':135, 'RIO VERDE':136, 'JD IPE':137, 'IGUAÇÚ 1':138, 'AGUAS BELAS':139, 'ÁGUAS BELAS':140, 'IGUAÇU 01':141, 'ESTADOS':142, 'CIC':143, 'JR TAISA':144, 'PLANTA DEODORO':145, 'MAUA':146, 'COLONIA FARIA':147, 'NAÇÕES':148, 'JARDIM SANTA MÔNICA':149, 'LOTEAMENTO SÃO GERÔN':150, 'TAMANDARE ':151, 'CAMPO LARGO':152, 'BOQUEIRÃO ':153, 'JARDIM BELA VISTA':154, 'ESTANCIA PINHAIS ':155, 'COLONIA SAO VENANCIO':156, 'FRANCISCO GORSKI':157, 'OSASCO':158, 'BARIGUI':159, 'GUATUPE ':160, 'PARQUE DAS NASCENTES':161, 'CENTRO ':162, 'JD. ORESTES THÁ':163, 'PARQUE DAS FONTES':164, 'PINEVILLE':165, 'BORDA DO CAMPO ':166, ' JARDIM OSASCO':167, 'JARDIM PRIMAVERA':168, 'JD DONA BELIZARIA':169, 'PIRAQUARA':170, 'JARDIM RAFAELA':171, 'BARRO PRETO':172, 'BELAS AGUAS':173, 'EUCALIPTOS':174, 'VILA GRAZIELA':175, 'CIDADE INDUSTRIAL DE':178, 'AFONSO PENA':179, 'PALMEIRINHA':180, 'IPE 2':181, 'SANTA MONICA':182, 'GUATUPE':183, 'AFONSO PENA ':184, 'SAO SEBASTIAO':185, 'MAUÁ':186, 'SÃO GERONIMO':187, 'OURO FINO':188, 'SANTO ANTÔNIO':189, 'CAMPINHA GRANDE DO S':190, ' JARDIM PEDRO DEMETE':191, 'ROÇA GRANDE':192, 'TINDIQUERA':193, 'SÃO BENEDITO':194})

df['ATENDIMENTO_BAIRRO_NOME'] = df['ATENDIMENTO_BAIRRO_NOME'].astype(str).astype(int)

"""### NATUREZA1_DESCRICAO"""

df['NATUREZA1_DESCRICAO'] = df['NATUREZA1_DESCRICAO'].replace({'Apoio':1, 'Alarmes':2, 'Invasão':3, 'Vistoria':4, 'Roubo':5, 'Perturbação do sossego':6, 'Trânsito':7, 'Risco de acidente/à vida (Defesa Civil)':8, 'Violação de Medida Protetiva Lei Maria da Penha':9, 'Dano':10, 'Lesão Corporal':11, 'Fundada Suspeita (Abordagem)':12, 'Substância Ilícita':13, 'Orientação':14, 'Alagamento':15, 'Animais':16, 'Furto':17, 'Desinteligência':18, 'Patrulha Maria da Penha':19, 'Atitude Suspeita':20, 'Atos obscenos/libidinosos':21, 'Vias de fato':22, 'Queima a céu aberto':23, 'Ameaça':24, 'Averiguação':25, 'Encaminhamento':26, 'Estupro':27, 'Saturação':28, 'Agressão física/verbal':29, 'AIFU':30, 'Escolta':31, 'Incêndio':32, 'Risco de acidente / à vida':33, 'Desacato':34, 'Paciente/usuário alterado':35, 'Veículo':36, 'Pesca em local proibido':37, 'Ronda':38, 'Destelhamento':39, 'Construção Irregular':40, 'Crime ambiental':41, 'Risco de desabamento / desmoronamento':42, 'Tentativa':43, 'Fornecimento de Lona':44, 'Suicídio':45, 'Obstrução de via':46, 'Substância Lícita':47, 'Depósito irregular':48, 'Corte irregular de árvore':49, 'Achado':50, 'Queda de árvore':51, 'Disparo de arma':52, 'Órgãos acionados':53, 'Averiguação (Defesa Civil)':54, 'Antecedentes Criminais - Verificação':55, 'Injúria':56, 'Desaparecimento':57, 'Manifestação':58, 'Seqüestro e cárcere privado':59, 'Arrastão':60, 'Deslizamenton de Terra':61, 'ZELADORIA URBANA':62, 'Desabamento':63, 'Devolução de coisa achada':64, 'Conduta inconveniente':65, 'Uso indevido do cartão transporte':66, 'Maus tratos à pessoas':67, 'Extravio de Equipamento':68, 'Porte Ilegal':69, 'Rixa':70, 'Erosão':71, 'Importunação\xa0sexual':72, 'Situação de risco':73, 'Queda de fios de energia':74, 'Estelionato':75, 'Desobediência':76, 'Racismo':77, 'Homicídio':78, 'Queda de galho':79, 'Homofobia':80, 'Descumprimento lei 15799/2021 COVID-19':81, 'Fuga de aluno/interno':82, 'Menores abordando transeuntes':83, 'Abandono de incapaz':84, 'Risco de queda de árvore':85, 'Retirada de invasão':86, 'Banho em local impróprio':87, 'Abuso de incapazes':88, 'Contrabando ou descaminho':89, 'Criança perdida/desaparecida':90, 'Extravio, sonegação ou inutilização de livro ou doc.':91, 'Resistência':92, 'Aliciamento de menor':93, 'Apropriação indébita':94, 'Proteção ao patrimônio':95, 'Infiltração':96, 'Roubo, furto, extravio, recuperação, apreensão de armas de fogo.':97, 'Receptação':98, 'Ataque de insetos':99, 'Fiscalizações e Orientações':100, 'Vazamento ou derramamento de Produto Perigoso ou Infectante':101, 'Falsidade ideológica (Falsa Identidade)':102, 'Câmera Off-Line':103, 'Poluição visual/ambiental':104, 'Óbito':105, 'Avaria em Equipamento/Patrimônio (não intencional)':106, 'Fuga de paciente':107, 'Moeda Falsa':108, 'Embriaguez':109, 'Queda de poste':110, 'Material abandonado':111, 'Calote':112, 'Quedas de objetos ou partes de construções':113, 'Acidente Viatura':114, 'Risco de queda de poste':105, 'Constrangimento ilegal':106, 'Comércio ambulante':107, 'Usar de uniforme, ou distintivo de função pública que não exerce':108, 'Envenenamento':109, 'Denúncia de bomba':110, 'Mendigar, por ociosidade ou cupidez':111, 'Extorsão':112, 'Atentado violento ao pudor':113, 'Verificação':114, 'Pragas Animais':115, 'Inundação/Enchente':116, 'Importunação ofensiva ao pudor':117, 'Jogo de Azar':118, 'Porte de artefato explosivo':119, 'Maus tratos a animais':120, 'Calúnia':121, 'Sedução':122, 'Violência arbitrária':123, 'Afogamento':124, 'Explosão':125, 'Câmeras de videomonitoramento':126, 'Bueiro aberto/sem tampa':127, 'Menor gazeando aula':128, 'Fornecimento de bebida alcoólica à menores':129, 'Vadiagem':130, 'Discriminação':131, 'Escrito ou objeto obsceno (panfletos pornográficos)':132, 'Favorecimento da prostituição':133, 'Peculato':134, 'Impedimento ou perturbação de cerimônia funerária':135, 'Risco de queda de fios de energia':136, 'Ataque cão feroz':137, 'Abandono de função':138, 'Uso indevido do telefone público':139, 'Aterro irregular':140, 'Risco de explosão':141, 'Obstrução da Atividade Policial':142, 'Bueiro entupido':143, 'Corrupção de menores':144, 'Queda de aeronave':145, 'Incendio/Explosão em edificação':146, 'Vilipêndio a cadáver':147, 'Risco de queda de galho':148, 'Prostituição':149, 'Violação de sepultura/túmulo':150, 'Fingir-se funcionário público':151, 'Trote Telefonico':152, 'Apologia de crime ou criminoso':153, 'Falsificação de documento Publico':154, 'Denuncia Improcedente':155, 'Quadrilha ou bando':156, 'Desabamento de Telhado/Cobertura':157, 'Exploração de menores':158, 'Queda de Muro':159, 'Abalo Sísmico':160, 'Omissão de socorro':161, 'Rompimento de Barragem':162, 'Liberação de pessoa presa/apreendida por recusa no recebimento pela DP':163, 'Venda proibida de produtos específicos à menores':164, 'Concussão':165, 'Charlatanismo':166, 'Difamação':167, 'RECUSAR SE IDENTIFICAR AO POLICIAL':168, 'Perseguição (stalking)':169, 'Enxurrada':170, 'Rufianismo':171, 'Incitação ao crime':172, 'Averiguação (COSEDI)':173, 'Queda de Revestimento de Fachadas':174, 'Corrupção ativa':175, 'Óbito (Defesa Civil)':176, 'Prevaricação':177})

df['NATUREZA1_DESCRICAO'] = df['NATUREZA1_DESCRICAO'].astype(str).astype(int)

"""### OCORRENCIA_DIA_SEMANA"""

df['OCORRENCIA_DIA_SEMANA'] = df['OCORRENCIA_DIA_SEMANA'].replace({'DOMINGO':1, 'SEGUNDA':2, 'TERÇA':3, 'QUARTA':4, 'QUINTA':5, 'SEXTA':6, 'SÁBADO':7})

df['OCORRENCIA_DIA_SEMANA'] = df['OCORRENCIA_DIA_SEMANA'].astype(str).astype(int)

#.std() calcula o desvio padrão das colunas ou linhas numéricas
df.std()

"""# **Visualizações dos dados**"""

pd.set_option("display.float_format", lambda x: "%.0f" % x)

"""**Qual ano possui mais atendimento?**"""

plt.figure(figsize=(20,20))
sns.displot(data=df,  x='OCORRENCIA_ANO')

"""Resposta: 2021, 2020 e 2022

**Qual bairro possui mais atendimento?**
"""

plt.figure(figsize=(10,10))
sns.displot(data=df[df['ATENDIMENTO_BAIRRO_NOME']<20],  x='ATENDIMENTO_BAIRRO_NOME')

"""Resposta: 8: Centro, 1: CIC e 4: SÍTIO CERCADO

**Qual ano por bairro possui mais atendimento?**
"""

plt.figure(figsize=(100,80))
sns.displot(data=df[df['ATENDIMENTO_BAIRRO_NOME']<20],  x='ATENDIMENTO_BAIRRO_NOME', hue='OCORRENCIA_ANO', col='OCORRENCIA_ANO', color='red')

"""Resposta: 

`2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018 e 2019;`
*   1ºlugar: 8, Centro. 
*   2ºlugar: 1, CIC.
*   3ºlugar: 4: SÍTIO CERCADO.


`2020: `
*   1ºlugar: 8, Centro. 
*   2ºlugar: 4: SÍTIO CERCADO.
*   3ºlugar: 1, CIC.

`2021: 2022`
*   1ºlugar: 8, Centro. 
*   2ºlugar: 1, CIC.
*   3ºlugar: 4: SÍTIO CERCADO.

**Qual o tipo de natureza da ocorrência?**
"""

plt.figure(figsize=(20,20))
sns.displot(data=df[df['NATUREZA1_DESCRICAO']<20],  x='NATUREZA1_DESCRICAO')

"""Resposta: 1: Apoio, 12: Fundada Suspeita (Abordagem) e 10: Dano

**Qual o tipo de natureza da ocorrência em cada bairro?**
"""

plt.figure(figsize=(20,20))
sns.displot(data=df[df['ATENDIMENTO_BAIRRO_NOME']<20],   x='NATUREZA1_DESCRICAO', hue='ATENDIMENTO_BAIRRO_NOME', col='ATENDIMENTO_BAIRRO_NOME', color=['black'])
plt.xlim(1,20)

"""Resposta: foram utilizado so os 20 tipo de ATENDIMENTO_BAIRRO_NOME e ATENDIMENTO_BAIRRO_NOMe, que se tem mais registro.

**Qual horário da ocorrência mais frequente?**
"""

plt.figure(figsize=(20,20))
sns.displot(data=df,  x='OCORRENCIA_HORA')

"""Resposta: 15 14 e 16

**Qual horário mas a semana mais frequente?**
"""

plt.figure(figsize=(20,20))
sns.displot(data=df,  x='OCORRENCIA_HORA', hue='OCORRENCIA_HORA', col='OCORRENCIA_DIA_SEMANA')

"""Resposta: final de semana a mais ocorrencia a tarde, 13h ate umas 20h

**Qual horário mais a semana e o bairro mais frequentes?**
"""

plt.figure(figsize=(20,20))
sns.displot(data=df[df['ATENDIMENTO_BAIRRO_NOME']<20],  x='OCORRENCIA_HORA', hue='OCORRENCIA_DIA_SEMANA', col='ATENDIMENTO_BAIRRO_NOME', color=['black'])

"""Resposta: Bairro 8, centro tem mais registro de manha e a tarde ja 1, CIC e 4 SÍTIO CERCADO, se mantem igual com descanso so na madrugada"""

plt.figure(figsize=(10,10))
sns.boxplot(data=df[df['NATUREZA1_DESCRICAO']<20],   x='OCORRENCIA_ANO', y='NATUREZA1_DESCRICAO')

"""# **Teste Modelagem**"""

# split entre treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(df.drop('ATENDIMENTO_BAIRRO_NOME', axis=1), # aqui informamos os atributos
                                                                        df['ATENDIMENTO_BAIRRO_NOME'], # aqui informamos as labels e na mesma ordem dos atributos
                                                                        test_size=0.20, # informamos a porcentagem de divisão da base. Geralmente é algo entre 20% (0.20) a 35% (0.35)
                                                                        random_state=0) # aqui informamos um "seed". É um valor aleatório e usado para que alguns algoritmos i

modelo_knn = KNeighborsRegressor().fit(X_train, y_train)
modelo_knn.score(X_test, y_test)

