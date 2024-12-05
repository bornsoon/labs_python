import requests
from bs4 import BeautifulSoup

url = "https://www.daangn.com/kr/local-profile/?disableSearch=false&in=%EB%8F%99%EB%8C%80%EB%AC%B8%EA%B5%AC-87&themeIds=442"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

word = soup.select('meta')
print(word)