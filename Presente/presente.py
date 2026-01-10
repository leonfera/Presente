import streamlit as st
from datetime import date
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA (TEM QUE SER A PRIMEIRA LINHA) ---
st.set_page_config(page_title="Para Gaby", page_icon="❤️")
url="https://github.com/leonfera/Presente/raw/refs/heads/main/Presente/Auras.mp3"
# --- 2. ÁUDIO ---
# Dica: O autoplay pode ser bloqueado pelo navegador, mas tentamos mesmo assim.
st.audio(url, start_time=0, autoplay=True, loop=True)

# --- 3. TÍTULOS E TEXTOS ---
st.title("Feliz aniversário de namoro, amor! ❤️")
st.header("Quero aproveitar cada dia com você na minha vida.")

# --- 4. CÁLCULOS DE DATAS ---
hoje = date.today()

# Data do namoro
data_inicio = date(2025, 9, 10) 
dias_juntos = (hoje - data_inicio).days

# Data da primeira mensagem
data_inicio2 = date(2023, 6, 2)
dias_juntos2 = (hoje - data_inicio2).days

st.image("Presente/nos2.jpeg")

# Exibindo os números lado a lado (fica mais organizado)
col_a, col_b = st.columns(2)
col_a.metric(label="Dias de vida juntos", value=f"{dias_juntos} dias")
col_b.metric(label="Desde a 1ª mensagem", value=f"{dias_juntos2} dias")

st.divider() # Uma linha separadora bonita

# --- 5. O BOTÃO DA SURPRESA ---
# Usamos session_state para garantir que as fotos não sumam se ela clicar em algo
if 'abriu' not in st.session_state:
    st.session_state.abriu = False

if st.button('Clique aqui para ver alguns momentos nossos') or st.session_state.abriu:
    st.session_state.abriu = True # Marca que o botão foi clicado
    
    st.balloons()
    st.success("Te amo do fundo do meu coração! Você é minha pessoa favorita e viveria uma vida só com você. Não esqueça o quanto é especial para mim.")
    

# 1. Volte para a lista simples (apenas os nomes dos arquivos, SEM https)
    lista_fotos = [
        "stark.png", "fri.png", "casa.png", "flauma.png", 
        "cafe.png", "cy.png", "ivantill.png", "fly.png", 
        "zhu.png", "maru.png", "oguri.png", "dona.png", 
        "MC.png", "seth.png", "Denis.png"
    ]

    st.write("---")
    st.write("### 📸 Nossa Galeria")

    col1, col2 = st.columns(2)

    for i, nome_arquivo in enumerate(lista_fotos):
        # --- LÓGICA DE DETETIVE PARA ACHAR A FOTO ---
        # Tenta achar a foto na pasta atual
        if os.path.exists(nome_arquivo):
            caminho_final = nome_arquivo
        # Se não achou, tenta achar dentro da pasta 'Presente' (correção para o seu caso)
        elif os.path.exists(f"Presente/{nome_arquivo}"):
            caminho_final = f"Presente/{nome_arquivo}"
        else:
            # Se não achou em lugar nenhum, avisa qual foto está com problema
            st.error(f"❌ Não achei a foto: {nome_arquivo}")
            continue
        
        # --- MOSTRA A FOTO ---
        if i % 2 == 0:
            col1.image(caminho_final, use_container_width=True)
        else:
            col2.image(caminho_final, use_container_width=True)
    st.success("Te amarei até meu ultimo suspiro")








