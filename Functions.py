##### import modules
import requests
from bs4 import BeautifulSoup
import re
import spacy

##### functions
def get_web_data():
    """
    Gets transfer rumour information from BBC sports website 

    Parmas
        N/A

    Returns
        article - str - transfer rumour information 
    """

    ### access webpage
    response = requests.get("https://www.bbc.co.uk/sport/football/gossip")

    ### parse data
    soup = BeautifulSoup(response.text, "html.parser")

    ### find only transfer information
    article_full = soup.find(class_="qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++").get_text()

    unwanted = soup.find(class_ = "include-box__pullout" ).get_text()

    article = re.sub(unwanted,"", article_full)

    return article

def select_data(article, user_choice):
    """
    selects transfer rumour information for user selected club

    Parmas
        article - str - transfer rumour information 
        user_choice - streamlit selection - user football club selection 

    Returns
        transfer - str - transfer rumour information for club
    """

    ### load language model
    nlp = spacy.load("en_core_web_sm")

    ### create doc object 
    doc = nlp(article)

    ### select sentences in article that match user_choice and remove phrase external-link
    transfer = ""
    for sentence in doc.sents:
        if user_choice in str(sentence):
            clean = re.sub("external-link", " ", str(sentence))
            transfer += "\n" + clean + "\n"
        
        if len(transfer) == 0:
            transfer = "No transfer rumours"

    return transfer