import requests
from bs4 import BeautifulSoup

# 웹 페이지를 가져옵니다
response = requests.get('https://www.youtube.com/watch?v=L6MZDx02D9I')

# 웹 페이지의 HTML을 파싱합니다
soup = BeautifulSoup(response.text, 'html.parser')

# aria-label 속성이 있는 태그를 찾습니다
tags_with_aria_label = soup.find_all(attrs={"aria-label": True})

# aria-label 속성이 있는 태그 중에서 첫 번째 태그의 텍스트를 가져옵니다
if tags_with_aria_label:
    aria_label_text = tags_with_aria_label[0].get_text()
    print(aria_label_text)
else:
    print("aria-label 속성을 가진 태그를 찾을 수 없습니다.")
