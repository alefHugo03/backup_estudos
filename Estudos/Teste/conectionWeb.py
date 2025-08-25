import requests
from bs4 import BeautifulSoup 

page = requests.get('https://www.correios.com.br/') 

print(page)