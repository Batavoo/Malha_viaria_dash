import streamlit as st


def show_login_screen():
    """Exibe a tela de login e gerencia a autenticação."""
    st.title("Acesso ao Dashboard")
    st.write("Por favor, insira a senha para continuar.")

    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        # Verifica se a senha corresponde à definida nos segredos do Streamlit
        correct_password = st.secrets["app_secrets"]["password"]
        if password == correct_password:
            st.session_state['logged_in'] = True
            st.rerun()  # Recarrega o app para mostrar o dashboard
        else:
            st.error("A senha inserida está incorreta.")