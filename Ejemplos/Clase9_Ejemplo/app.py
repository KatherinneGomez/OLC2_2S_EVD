import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('StudentGuard')
    st.header('Carga Masiva')

    left_column, right_column = st.columns(2)
    df = pd.DataFrame()

    with left_column:
        archivo = st.file_uploader('Cargue un archivo CSV')
        if archivo is not None:
            df = pd.read_csv(archivo)
            st.success('Archivo cargado exitosamente!')
            

    with right_column:
        st.button('Limpiar datos')
        st.button('Entrenar modelo', type='primary')
    
    if not df.empty:
        st.dataframe(df)
    
    st.header('Métricas de Evaluación de Rendimiento')

    lcol, rcol = st.columns(2)

    with lcol:
        fig1 = px.pie(
            values=[70, 30],
            title='Exactitud',
            hole=0.4
        ) 

        st.plotly_chart(fig1)
    
    with rcol:
        fig2 = px.pie(
            values=[90, 10],
            title='Recall',
            hole=0.4
        ) 

        st.plotly_chart(fig2)
    
    st.header('Ajuste de hiperparámetros')
    val1 = st.slider('Número máximo de hojas', 
    min_value=3, max_value=10, step=1, value=5)
    st.write(val1)
    val2 = st.slider('Número máximo de áboles', 
    min_value=10, max_value=100, step=10, value=15)
    st.write(val2)
    st.button('Reentrenar')


if __name__ == '__main__':
    main()