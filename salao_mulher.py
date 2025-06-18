import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="Salão da Mulher 💇‍♀️", layout="centered")

st.title("💇‍♀️ Salão da Mulher")
st.subheader("Agende seu horário com praticidade!")

nome = st.text_input("👩 Seu nome completo")
telefone = st.text_input("📱 Telefone com DDD", placeholder="Ex: 11999998888")

servicos = [
    "Corte feminino",
    "Corte masculino",
    "Escova",
    "Coloração",
    "Luzes",
    "Progressiva",
    "Manicure",
    "Pedicure",
    "Hidratação",
    "Sobrancelha"
]
servico_escolhido = st.selectbox("💅 Qual serviço deseja?", servicos)

data_agendamento = st.date_input("📅 Escolha a data do atendimento")
horario = st.selectbox("⏰ Escolha o horário", [
    "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00"
])

if st.button("📲 Confirmar e enviar pelo WhatsApp"):
    if nome and telefone and servico_escolhido:
        numero = "+55" + telefone.strip()
        mensagem = (
            f"Olá, aqui é o assistente virtual do *Salão da Mulher*! 💇‍♀️\n"
            f"Agendamento solicitado:\n\n"
            f"👩 Cliente: {nome}\n"
            f"💅 Serviço: {servico_escolhido}\n"
            f"📅 Data: {data_agendamento.strftime('%d/%m/%Y')}\n"
            f"⏰ Horário: {horario}\n\n"
            f"Aguarde a confirmação! 💖"
        )
        mensagem_encoded = urllib.parse.quote(mensagem)
        link_whatsapp = f"https://wa.me/{numero}?text={mensagem_encoded}"

        st.markdown(f"👉 [Clique aqui para enviar no WhatsApp]({link_whatsapp})", unsafe_allow_html=True)
        st.success("Mensagem gerada com sucesso! Clique no link acima.")
    else:
        st.warning("Preencha todos os campos para agendar.")
