import streamlit as st
from modules.auth import show_login_screen
from modules.data_loader import load_data

def build_dashboard():
    """Constrói e exibe o dashboard principal."""
    df = load_data()

    if not df.empty:
        # --- Título e Exibição do Dashboard ---
        st.title("Dashboard - Exemplo de Planilha Regional 10 Maio")
        st.header("Dados Brutos da Planilha")
        st.dataframe(df)

# --- Lógica Principal do App ---

# Inicializa o estado de login se não existir
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Se o usuário estiver logado, mostra o dashboard.
# Caso contrário, mostra a tela de login.
if st.session_state['logged_in']:
    build_dashboard()
else:
    show_login_screen()