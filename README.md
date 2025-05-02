# 🔳 Gerador de QR Code com Streamlit

Este é um aplicativo web simples feito com [Streamlit](https://streamlit.io/) que permite gerar QR Codes a partir de qualquer texto ou URL fornecido. Após gerar, o QR Code pode ser visualizado na tela e baixado como imagem PNG.

## ✅ Funcionalidades

- Entrada de texto ou URL
- Geração de QR Code automaticamente
- Visualização da imagem gerada
- Botão para download do QR Code (.png)


## 🚀 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/gerador-qr-code.git
cd gerador-qr-code
```

## 2. Instale as dependências 📄
python -m venv venv
source venv/bin/activate  
# No Windows: venv\Scripts\activate
pip install -r requirements.txt


## 3. Execute o aplicativo ✔

Comando: "streamlit run app.py"


## 📦 Requisitos ##
Python 3.7+

Dependências do requirements.txt

## Arquivos do projeto 📁 ##

- app.py — código principal da aplicação
- requirements.txt — lista de dependências


# 📚 Tecnologias utilizadas #
Streamlit — criação de interface web simples

qrcode — geração do código QR

Pillow (PIL) — manipulação da imagem

BytesIO — criação de buffer de imagem para download



