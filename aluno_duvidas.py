import streamlit as st
import pymongo # Importando o PyMongo
from pymongo import MongoClient

st.set_page_config(page_title="Pagina de Duvidas", page_icon=":clapper:", layout="wide")


st.page_link("app.py", label="Home", icon="🏠")
st.page_link("http://www.google.com", label="Pesquisa no Google", icon="🌎")






# Configuração da conexão com o MongoDB
client = MongoClient("mongodb+srv://user_01:sucesso1807@cluster0.slfd3no.mongodb.net/")  # Substitua pelo URI do MongoDB
# Nome do banco de dados e coleção
db = client["duvidas_db"]
collection = db["duvidas"]

st.title("Digite sua dúvida")

# Captura do nome do aluno
nome = st.text_input("Digite seu nome")
st.write(f"Olá, {nome}!")

# Checkbox para anonimato
anonimo = st.checkbox("Anônimo")
if anonimo:
    st.write("Você está enviando a dúvida de forma anônima.")

# Captura da dúvida
duvida = st.text_area("Digite sua dúvida")

# Botão para enviar
enviar = st.button("Enviar")

if enviar:
    if duvida.strip():
        # Dados a serem armazenados no MongoDB
        duvida_data = {
            "nome": "Anônimo" if anonimo else nome.strip(),
            "duvida": duvida.strip(),
        }
        
        # Inserindo no MongoDB
        collection.insert_one(duvida_data)
        st.success("Dúvida enviada com sucesso!")
    else:
        st.error("Por favor, digite uma dúvida antes de enviar.")



# Seção para exibir dúvidas frequentes
st.title("Dúvidas Frequentes")
duvidas_frequentes = collection.find()

if collection.count_documents({}) > 0:
    for d in duvidas_frequentes:
        st.subheader(f"Nome: {d['nome']}")
        st.write(f"Dúvida: {d['duvida']}")
else:
    st.write("Nenhuma dúvida registrada ainda.")
