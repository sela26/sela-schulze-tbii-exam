import streamlit as st
import segno
import time

# usually do not put a definition in a definition!
def generate_qrcode_page():
    st.title("QR CODE GENERATOR")

    # add a text box and store in a variable
    url = st.text_input("Please enter the URL you want to encode:")

    # definition to create a qr code
    def generate_qrcode(url):
        # segno library, make_qr function
        qrcode = segno.make_qr(url)
        qrcode.to_pil(scale=5,
                      dark="red").save("images/L5_qrcode_streamlit.png")


    if url:
        with st.spinner("Generate the QR Code..."):
            time.sleep(2)
        generate_qrcode(url)
        st.image("images/qrcode_streamlit.png",
                 caption="Here is the QR Code"
                 )

    st.markdown("Made by Sela 🤎")