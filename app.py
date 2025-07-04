import streamlit as st
import pandas as pd
import gspread

# --- Autenticação e Conexão ---
# ATENÇÃO: Este método é apenas para teste local. 
# Para deploy, usaremos os segredos do Streamlit (próximo passo).
try:
    # Tenta autenticar usando o arquivo JSON local
    gc = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
    
    # Abre a planilha pelo nome
    spreadsheet = gc.open("Cópia de EM DESENVOLVIMENTO - SR 10 CONTROLE MALHA VIÁRIA")
    
    # --- Seleciona a aba específica pelo nome ---
    worksheet = spreadsheet.worksheet('EXEMPLO DE PLANILHA REGIONAL 10 MAIO')
    
    # Puxa todos os dados da aba
    data = worksheet.get_all_records()
    
    # Converte para um DataFrame do Pandas
    df = pd.DataFrame(data)

    # --- Título do Dashboard ---
    st.title("Dashboard - Exemplo de Planilha Regional 10 Maio")

    # --- Exibindo os Dados ---
    st.header("Dados Brutos da Planilha")
    st.dataframe(df)

    # Adicione seus gráficos e análises aqui
    st.header("Análise de Dados")
    # Exemplo de gráfico de barras
    if not df.empty and 'Nome de uma Coluna para Contar' in df.columns:
        st.bar_chart(df['Nome de uma Coluna para Contar'].value_counts())

# except FileNotFoundError:
#     st.error("Arquivo de credenciais 'google_credentials.json' não encontrado.")
#     st.info("Certifique-se de que o arquivo de credenciais JSON está na mesma pasta que app.py e foi renomeado corretamente.")
# except gspread.exceptions.WorksheetNotFound:
#     st.error("A aba 'EXEMPLO DE PLANILHA REGIONAL 10 MAIO' não foi encontrada. Verifique o nome da aba na sua planilha.")
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar os dados: {e}")