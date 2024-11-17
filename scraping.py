import  csv
from bs4 import BeautifulSoup
import lxml
import requests
page= requests.get("https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/")
def main (page):
    src=page.content
    soup=BeautifulSoup(src,'lxml')
