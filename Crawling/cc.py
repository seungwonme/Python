import requests
from bs4 import BeautifulSoup

# 웹 페이지를 가져옵니다
response = requests.get('https://www.naver.com/')

# 웹 페이지의 HTML을 파싱합니다
soup = BeautifulSoup(response.text, 'html.parser')

# 필요한 데이터를 추출합니다
data = soup.find_all('h1')

print(data)
