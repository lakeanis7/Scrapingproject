import requests
from bs4 import BeautifulSoup
pep = input("Enter a date (please like this yyyy/mm/dd): ")
page= requests.get("https://www.washingtonpost.com/technology/{pep}/privacy-check-blacklight/")

def main(page):
    src=page.content
    soup=BeautifulSoup(src,'lxml')
    news_details = []
    news = soup.find_all('div', {'class': 'some-class'})  
    for item in news:
        title = item.find('h2').text.strip() 
        content = item.find('p').text.strip() 
        writer = item.find('span', {'class': 'writer-class'}).text.strip() 
        date = item.find('time').text.strip()
    for detail in news_details:
      with open('Documents'/'python', "w")as output_file:
        print(f"Title: {detail['title']}")
        print(f"Content: {detail['content']}")
        print(f"Writer: {detail['writer']}")
        print(f"Date: {detail['date']}")
        print("-" * 40)
main(page)
