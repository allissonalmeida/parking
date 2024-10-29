import streamlit as st
import folium
from streamlit_folium import st_folium
import datetime
import random
import json


#Get add datetime
x = datetime.datetime.now()
data_em_texto = x.strftime('%d/%m/%Y %H:%M')


# add image in page
st.image("logo_parking.png", caption="Parking Lot", width=100)


st.header('Hello, welcome to parking lot system!')
#st.subheader(f':date: Today : {x.day}/{x.month}/{x.year} ')
st.subheader(f':date: Today : {data_em_texto} ')


# Open the JSON file
with open('parking_lot.json') as f:
    data = json.load(f)


# Read data json
vagas_free_est_1    = data['1']['vagas_livre'] 
vagas_free_est_2    = data['2']['vagas_livre'] 
total_vagas_est_1   = data['1']['total_vagas'] 
total_vagas_est_2   = data['2']['total_vagas'] 
latitude1           = data['1']['latitude'] 
longitude1          = data['1']['longitude'] 
latitude2           = data['2']['latitude'] 
longitude2          = data['2']['longitude'] 



#Tabs
parking,about = st.tabs(["Parking ","About"])


with parking:

    st.subheader(f':round_pushpin: Parking 1: :red[{vagas_free_est_1}] free / :red[{total_vagas_est_1}] ')
    st.subheader(f':round_pushpin: Parking 2: :red[{vagas_free_est_2}] free / :red[{total_vagas_est_2}] ')


    # Map begin initialize
    map = folium.Map(location=[-2.4981688900228276, -44.285531045356464], zoom_start=16)

    fg = folium.FeatureGroup(name="Parking 1", show=True).add_to(map)
    string_1 = f'Parking 1: {vagas_free_est_1} free'

    folium.Marker(
                [ latitude1, longitude1 ], 
                popup="Parking 1", 
                icon=folium.Icon(color='red'),
                tooltip= f" {vagas_free_est_1} free").add_to(fg)
    
    fg = folium.FeatureGroup(name="Parking 2", show=True).add_to(map)
    string_2 = f"Parking 2: {vagas_free_est_2} parking lot free"

    folium.Marker(
                [latitude2, longitude2], 
                popup="Parking 2", 
                icon=folium.Icon(color='red'),
                tooltip= f" {vagas_free_est_2} parking lot free").add_to(fg)

    st_folium(map, width=750)




with about:

    st.header("About")

    # add image in page about PUC Rio
    #st.image("brasao_puc-rio.png", caption="PUC - Rio", width=100)

    st.write('Name Product: Parking Lot')
    st.write('Describe: Project for the subject INF2473 - TOP DATA SCIENCE III professor Hélio Cortez of Computer Vision for the PhD in Data Science.')
    st.write('Version: 1.0.0')
    st.write('Develepor: Allisson Almeida')
    st.write('E-mail: ajsalmeida@inf.puc-rio.br')
    st.write('GitHub: https://github.com/allissonalmeida/parking')
    st.write('Streamlit Share: https://parking-lot.streamlit.app/')
    st.write('Technologies used: Computer Vision, Python, Streamlit, GitHub, Replit API')
    