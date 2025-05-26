import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

#Encabezado
st.header('Analisis de datos de vehiculos de EE.UU')

#Lee la data
car_data = pd.read_csv('vehicles_us.csv')

#Boton para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Histograma de odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma por año del modelo')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Creación de un histograma para la columna "model_year"')
    fig2 = px.histogram(car_data, x='model_year')
    st.plotly_chart(fig2, use_container_width=True)

scatter_plot = st.checkbox('Mostrar gráfico de dispersión')
# casilla 2
if scatter_plot:
    st.write('Gráfico de dispersión entre "model_year" y "price"')
    fig3 = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año del Modelo')
    st.plotly_chart(fig3, use_container_width=True)