import cv2
import fitz  # PyMuPDF
import numpy as np
import streamlit as st
from PIL import Image

import input_file

st.set_page_config(layout='wide')
st.write("""
<div style='text-align:center'>
    <h1 style='color:#5e17eb;'>Counting the Number of Colored Boxes</h1>
</div>
""", unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')
# File uploader widget
uploaded_file = st.file_uploader("Upload a PDF or Image File", type=["pdf", "jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Check if it's an image file
    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        image = Image.open(uploaded_file)
        # converting to numpy array
        image_np = np.array(image)
        # converting from rgb to bgr for opencv
        image_np = cv2.cvtColor(image_np,cv2.COLOR_RGB2BGR)
        col1, col2 = st.columns(2)
        with col1:

            st.image(image, caption='Uploaded Image', use_column_width=True)
        # Detect Colors
        color_boxes = input_file.detect_colors(image_np)
        with col2:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.markdown("<h2 style='color: black;'>Detected Boxes</h2>", unsafe_allow_html=True)
            for key, value in color_boxes.items():
                st.write(f'{key} : {value}')
    # Check if it's a PDF file
    elif uploaded_file.type == "application/pdf":
        doc = fitz.open(stream=uploaded_file.read(),filetype='pdf')
        col1,col2 = st.columns(2)
        # Loop through each page and save it as an image
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Load page
            pix = page.get_pixmap()  # Get page as an image
            # Convert pixmap to image
            img_pil = Image.frombytes('RGB',(pix.width, pix.height),pix.samples)
            # Convert to opencv format
            img_np = np.array(img_pil)
            # Convert bgr for opencv format
            img_np = cv2.cvtColor(img_np,cv2.COLOR_RGB2BGR)

            with col1:

                st.image(img_pil,caption=f'page {page_num + 1} from PDF',use_column_width=True)
            # detect colors
            color_boxes = input_file.detect_colors(img_np)
            with col2:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.markdown("<h2 style='color: black;'>Detected Boxes</h2>", unsafe_allow_html=True)
                for key, value in color_boxes.items():
                    st.write(f'{key} : {value}')