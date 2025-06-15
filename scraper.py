import requests
from bs4 import BeautifulSoup
import re
import smtplib

# Configurações
URL = "https://www.amazon.com.br/dp/B0CGRZQG1X/"  # Use o link do produto real
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "pt-BR,pt;q=0.9"
}
ALVO = 3000.00  # Preço desejado

def buscar_preco():
    try:
        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        # Pega o título e o preço
        titulo = soup.find(id="productTitle").get_text(strip=True)
        preco_raw = soup.find("span", class_="a-offscreen").get_text(strip=True)

        preco = float(re.sub(r"[^\d,]", "", preco_raw).replace(",", "."))

        print(f"[✓] Produto: {titulo}")
        print(f"💰 Preço atual: R$ {preco:.2f}")

        if preco < ALVO:
            enviar_email(titulo, preco)
        else:
            print("🔔 Preço ainda está alto.")

    except Exception as e:
        print(f"[Erro] Não foi possível buscar o preço: {e}")

def enviar_email(nome_produto, preco):
    remetente = "seuemail@gmail.com"
    senha = "sua_senha_de_aplicativo"
    destinatario = "destinatario@gmail.com"

    assunto = "📉 O preço caiu!"
    corpo = f"O produto '{nome_produto}' está por R${preco:.2f}!\nLink: {URL}"

    mensagem = f"Subject: {assunto}\n\n{corpo}"

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, mensagem.encode("utf-8"))

    print("📧 Alerta enviado por e-mail!")

if __name__ == "__main__":
    buscar_preco()
