# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 17:34:16 2025

@author: Maria G
"""

import pandas as pd
import streamlit as st
import numpy as st
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split #Entrenamiento
from sklearn.preprocessing import LabelEncoder
from metrics import classification_reprot, confuncion_matrix

# mostrar o cargar los datos
ds= pd.read_csv("dataset_financiero_riesgo.csv")

#Colocar un título principal en la página Web
st.title("Predicción de Riesgo Financiero")

# Cargar los datos en la memoria CACHE para mejorar la velocidad del acceso al
# conjunto de datos
@st.cache_data

#Hacemos una función que se llama cargar_datos. leemos el archivo en una variable
# y retornamos la variable al que llama a la función.
# que retornamos se llama "ds", abreviatura de "dataset".
def cargar_datos():
    ds= pd.read_csv("dataset_financiero_riesgo.csv")
    return ds

ds= cargar_datos()
st.write("Vista previa de los datos")
st.dataframe(ds.head())













    













