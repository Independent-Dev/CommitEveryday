from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input("검색어를 입력하세요: ")
url = base_url + quote_plus(plus_url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_= '_img')

for count, i in enumerate(img):
    img_url = i['data-source']
    with urlopen(img_url) as f:  # src의 파일을 open함
        with open('./img/'+plus_url+str(count+1) + '.jpg', 'wb') as d:  # binary file을 다루므로...
            img = f.read()
            d.write(img)


print('다운로드 완료')