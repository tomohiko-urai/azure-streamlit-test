
#-*- coding:utf-8 -*-
####import model as shinemuscat_chk 
import sys, os
from PIL import Image
import numpy as np
#import cv2 
import streamlit as st
#import matplotlib.pyplot as plt
#import datetime

image_size = 50
#####import streamlit as st
st.title('Hello')

####st.set_option("deprecation.showfileUploaderEncoding", False)

######st.sidebar.title("シャインマスカット画像収穫認識アプリ")
######st.sidebar.write("オリジナルの画像認識モデルを使ってシャインマスカット収穫色判定をします。")

#####st.sidebar.write("")

#####img_source = st.sidebar.radio("画像のソースを選択してください。",
#####                              ("画像をアップロード", "カメラで撮影"))
#####if img_source == "画像をアップロード":
#####    img_file = st.sidebar.file_uploader("画像を選択してください。", type=["png", "jpg"])
#####elif img_source == "カメラで撮影":
#####    img_file = st.camera_input("カメラで撮影")

####if img_file is not None:
    #####with st.spinner("推定中..."):
        #####img = Image.open(img_file)
        #####st.image(img, caption="対象の画像", width=480)
        #####st.write("")

        ####img = img.convert("RGB")
        ####img = img.resize((image_size,image_size))



