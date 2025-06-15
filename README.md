# 📉 Monitorador de Preços com Python (Web Scraper)

Este script monitora o preço de um produto (ex: na Amazon) e envia um e-mail quando o valor estiver abaixo do desejado.

## ⚙️ Tecnologias

- Python 3
- `requests`
- `BeautifulSoup`
- `smtplib` (e-mail)

## 🧪 Funcionalidades

- Coleta o preço diretamente de uma página de produto
- Compara com um preço desejado
- Envia alerta por e-mail se o valor estiver menor

## 🚀 Como usar

1. Clone este repositório:
```bash
git clone https://github.com/thassioramos/monitorador-preco
cd monitorador-preco
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Edite as seguintes variáveis no código:
- `URL` (link do produto)
- `ALVO` (preço desejado)
- Informações do e-mail no método `enviar_email`

4. Execute o script:
```bash
python scraper.py
```

## 📦 requirements.txt
```txt
requests
beautifulsoup4
```

## 📝 Observações

- Pode ser adaptado para sites como Buscapé, Kabum, etc.
- Ideal para praticar scraping, regex, e automação com Python.

## 📤 Portfólio

Este projeto faz parte do meu portfólio como programador júnior.  
Confira mais em [meu LinkedIn](https://www.linkedin.com/in/thassio-ramos-6b8a41236/)

## 📜 Licença

MIT
