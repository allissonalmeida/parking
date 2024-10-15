import streamlit as st
import folium
from streamlit_folium import st_folium
import datetime


#Get add datetime
x = datetime.datetime.now()


# add image in page
st.image("logo_parking.png", caption="Parking Lot", width=100)

st.header('Hello, welcome to parking system!')
st.subheader(f':date: Today : {x.day}/{x.month}/{x.year} ')

#Tabs
parking,about = st.tabs(["Parking ","About"])


with parking:

    st.subheader(':round_pushpin: Parking 1: :red[7] free out of :red[69] ')
    st.subheader(':round_pushpin: Parking 2: :red[56] free out of :red[100] ')


    # Map begin initialize
    map = folium.Map(location=[-2.4981688900228276, -44.285531045356464], zoom_start=16)

    fg = folium.FeatureGroup(name="Estacionamento 1", show=True).add_to(map)

    folium.Marker(
                [-2.499214473542157, -44.28518202906775], 
                popup="Parking 1", 
                icon=folium.Icon(color='red'),
                tooltip="Parking 1: 7 free").add_to(fg)
    
    fg = folium.FeatureGroup(name="Estacionamento 2", show=True).add_to(map)

    folium.Marker(
                [-2.4979254578655006, -44.28468403902029], 
                popup="Parking 2", 
                icon=folium.Icon(color='red'),
                tooltip="Parking 2: 56 free").add_to(fg)

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
    