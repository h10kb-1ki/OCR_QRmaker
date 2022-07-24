import streamlit as st 
import qrcode
from PIL import Image

st.title('QRコード生成')

txt = st.text_input('QRコード化したいテキストを入力してください:')

if st.button('QRコード生成'):
    _img = qrcode.make(txt)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)