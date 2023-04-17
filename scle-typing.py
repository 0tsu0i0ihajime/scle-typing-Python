import requests
from bs4 import BeautifulSoup

# WebサイトのURL
url = 'https://www.example.com/'

# Webサイトを取得
response = requests.get(url)

# HTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')

# img要素を取得
images = soup.find_all('img')

# img要素から画像のURLを取得
for image in images:
    image_url = image.get('src')
    print(image_url)
