import streamlit as st
from datetime import date, datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Para o Amor da Minha Vida",
    page_icon="❤️",
    layout="centered"
)

# --- TÍTULO E CABEÇALHO ---
st.title("❤️ Nossa História de Amor")
st.write("Um cantinho especial para lembrar dos nossos momentos.")
st.divider() # Linha divisória visual

# --- CONTADOR DE DIAS ---
# IMPORTANTE: Mude a data abaixo para o dia que vocês começaram a namorar
data_inicio = date(2023, 1, 15) 
hoje = date.today()
dias = (hoje - data_inicio).days
anos = dias // 365
meses = (dias % 365) // 30

# Mostra números grandes na tela
col1, col2, col3 = st.columns(3) # Cria 3 colunas lado a lado
col1.metric("Anos juntos", anos)
col2.metric("Meses juntos", meses)
col3.metric("Total de dias", dias)

st.divider()

# --- LINHA DO TEMPO (FOTOS) ---
st.header("📸 Nossos Melhores Momentos")

# Criando abas para organizar as fotos
tab1, tab2, tab3 = st.tabs(["O Início", "Viagens", "Momentos Bobos"])

with tab1:
    st.write("Lembra de como tudo começou?")
    # DICA: Coloque uma foto chamada 'inicio.jpg' na mesma pasta do código
    # st.image("inicio.jpg", caption="Nosso primeiro encontro") 
    st.info("Aqui vai a foto do nosso primeiro encontro! (Coloque o arquivo na pasta)")

with tab2:
    st.write("As aventuras que vivemos...")
    # st.image("viagem.jpg")
    st.write("Imagine uma foto linda nossa na praia aqui.")

with tab3:
    st.write("Nossas caretas e risadas.")
    # st.image("engracada.jpg")

st.divider()

# --- SURPRESA FINAL (Interativo) ---
st.header("🎁 Uma Surpresa para Você")
st.write("Prepare o coração e aumente o som...")

# Botão que libera a surpresa
if st.button("Clique para ver o quanto eu te amo"):
    st.balloons() # Solta balões na tela!
    st.toast("Eu te amo muito! ❤️") # Mensagem que sobe no cantinho
    
    # Se você tiver uma música mp3, coloque na pasta e descomente a linha abaixo:
    # st.audio("nossa_musica.mp3", format="audio/mp3")
    
    st.success("Você é a melhor coisa que aconteceu na minha vida!")
    st.write("Obrigado por cada segundo ao meu lado.")