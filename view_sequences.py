import streamlit as st
import pickle
import os
import glob


st.set_page_config(layout='wide')


info_dict = {}

for model in ['car', 'monster', 'leopard']:
    info_dict[model] = {}
    folders = os.listdir(f'{model}/additive')
    for directory in ['compare_to_prev', 'compare_to_prev_merged', 'premerged_compare_to_prev']:
        path = f'{model}/additive/{directory}'
        info_dict[model][directory] = {}
        if os.path.exists(f'{model}/additive/{directory}/run_data.pkl'):
            num_strokes = pickle.load(open(f'{model}/additive/{directory}/num_strokes.pkl', 'rb'))
            info_dict[model][directory]['num_strokes'] = num_strokes
        if os.path.exists(f'{model}/additive/{directory}/losses.pkl'):
            losses = pickle.load(open(f'{model}/additive/{directory}/losses.pkl', 'rb'))
            info_dict[model][directory]['losses'] = losses

for model in ['car', 'monster', 'leopard']:
    folders = ['compare_to_prev', 'compare_to_prev_merged', 'premerged_compare_to_prev']

    stcols = st.columns(3)
    for i in range(3):
        directory = folders[i]
        stcols[i].subheader(directory)
        files = glob.glob(f'{model}/additive/{directory}/color_*.png')
        files.sort()
        num_imgs = len(files)
        idx = stcols[i].slider('image id',  min_value=0, max_value=num_imgs-1, value=10, key=f'{model}_{i}')

        stcols[i].image(files[idx])

        if info_dict[model][directory].get('num_strokes') is not None:
            n = info_dict[model][directory]['num_strokes'][idx]
            stcols[i].subheader(f'Num strokes: {n}')
        if info_dict[model][directory].get('losses') is not None:
            n = info_dict[model][directory]['losses'][idx]
            stcols[i].subheader(f'LPIPS: {n:4f}')