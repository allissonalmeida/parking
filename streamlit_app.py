import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static

# add image in page
st.image("logo_parking.png", caption="Parking Lot", width=100)

st.header('Hello Parking Lot')

#Tabs
parking_1, parking_2, about = st.tabs(["Parking 1", "Parking 2", "About"])


with parking_1:

    st.subheader(' 7 free spots out of 69 ')

    # Map begin initialize
    map = folium.Map(location=[-2.4997650854460436, -44.286793349112095], zoom_start=16)

    fg = folium.FeatureGroup(name="Estacionamento 1", show=True).add_to(map)

    folium.Marker(
                [-2.499214473542157, -44.28518202906775], 
                popup="Parking 1", 
                icon=folium.Icon(color='red'),
                tooltip="Parking 1").add_to(fg)

    st_folium(map, width=950)



with parking_2:

    st.subheader(' 59 free spots out of 100 ')

    # Map begin initialize
    map = folium.Map(location=[-2.4997650854460436, -44.286793349112095], zoom_start=16)

    fg = folium.FeatureGroup(name="Estacionamento 1", show=True).add_to(map)

    folium.Marker(
                [-2.499214473542157, -44.28518202906775], 
                popup="Parking 2", 
                icon=folium.Icon(color='red'),
                tooltip="Parking 2").add_to(fg)

    st_folium(map, width=950)

with about:

    st.header("About")

    # add image in page about PUC Rio
    #st.image("brasao_puc-rio.png", caption="PUC - Rio", width=100)

    st.write('Name Product: Parking Lot')
    st.write('Describe: Project for the subject INF2473 - TOP DATA SCIENCE III professor Hélio Cortez of Computer Vision for the PhD in Data Science.')
    st.write('Version: 1.0.0')
    st.write('Develepor: Allisson Almeida')
    st.write('E-mail: ajsalmeida@inf.puc-rio.br')
    