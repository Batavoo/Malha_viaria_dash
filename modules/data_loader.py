import streamlit as st
import pandas as pd
import gspread

# Usa o cache do Streamlit para evitar recarregar os dados a cada interação do usuário
@st.cache_data(ttl=600) # Cache de 10 minutos
def load_data():
    """Conecta ao Google Sheets e retorna os dados como um DataFrame do Pandas."""
    try:
        # Autenticação com Google Sheets usando os segredos
        gc = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
        
        # Abre a planilha e a aba desejada
        spreadsheet = gc.open("Cópia de EM DESENVOLVIMENTO - SR 10 CONTROLE MALHA VIÁRIA")
        worksheet = spreadsheet.worksheet('EXEMPLO DE PLANILHA REGIONAL 10 MAIO')
        
        # Puxa e processa os dados
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        return df

    except gspread.exceptions.WorksheetNotFound:
        st.error("A aba 'EXEMPLO DE PLANILHA REGIONAL 10 MAIO' não foi encontrada.")
        return pd.DataFrame() # Retorna um DataFrame vazio em caso de erro
    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar os dados: {e}")
        return pd.DataFrame() # Retorna um DataFrame vazio em caso de erro