import requests
from bs4 import BeautifulSoup

def extract_text_from_web_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ''
    for paragraph in soup.find_all('p'):
        text += paragraph.get_text() + '\n'
    return text
