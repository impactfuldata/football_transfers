"""
Interactive web app for visualising football transfer rumours 
"""
##### import modules
import requests
from bs4 import BeautifulSoup
import re
import spacy 
import streamlit as st
from datetime import datetime
import Functions

##### page title
st.title("Premier League Football Transfer Rumours")
st.header(datetime.today().strftime("%d-%m-%y"))

##### user input - club selection
user_choice = st.selectbox ("Select your club to get the latest transfer gossip from the BBC" , ["Arsenal", "Aston Villa", "Bournemouth", "Brentford","Brighton & Hove Albion", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Southampton", "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers"])

##### get transfer transfer rumour information from BBC sports website 
article = Functions.get_web_data()

##### select transfer rumour information for user selected clu
transfer = Functions.select_data(article, user_choice)

##### display results
st.write(f"{transfer}")
print(transfer)