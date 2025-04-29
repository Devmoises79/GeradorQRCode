import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Gerador de QR Code", layout="centered")
st.title("🔳 Gerador de QR Code")

# Entrada
text = st.text_input("Digite o texto ou URL para gerar o QR Code:")


if st.button("Gerar QR Code"):
    if text.strip() == "":
        st.warning("Por favor, digite algum texto ou URL.")
    else:
        qr = qrcode.QRCode( border=2)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.convert("RGB")  # Conversão importante aqui!

        st.image(img, caption="QR Code Gerado", use_container_width=False)


        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="📥 Baixar QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
