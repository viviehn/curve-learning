import streamlit as st
import pickle
import os
import glob


for model in ['car', 'monster', 'leopard']:
    folders = os.listdir(f'{model}/additive')

    stcols = st.columns(3)
    for i in range(3):
        directory = stcols[i].selectbox(f'Dataset Directory {i}', folders)
        files = glob.glob(f'{model}/additive/{directory}/color_*.png')
        files.sort()
        num_imgs = len(files)
        idx = stcols[i].slider('image id',  min_value=0, max_value=num_imgs-1, value=10, key=i)

        stcols[i].image(files[idx])

        if os.path.exists(f'{model}/additive/{directory}/run_data.pkl'):
            run_data = pickle.load(open(f'{model}/additive/{directory}/run_data.pkl', 'rb'))
            n = run_data['num_strokes'][idx]
            stcols[i].subheader(f'Num strokes: {n}')