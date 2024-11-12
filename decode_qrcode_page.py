import streamlit as st
import numpy as np
import cv2


def decode_qrcode_page():
    # create header for your page
    st.header("Decode the QR Code")

    # add a file uploader widget
    qrcode = st.file_uploader("Upload your QR Code",
                              type=['jpg', 'png', 'jpeg'])

    # check you can place a qr code. use if-function because it errors otherwise
    if qrcode:
        # annoying code to convert uploaded qr code image into an image the decoded
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # place the qr code
        st.image(opencv_image)

        # decode qr code
        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QR Code contained {decoded_info}")
        # st.write(point)
        # st.write(straight_qr)