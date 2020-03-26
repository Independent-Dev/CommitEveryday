import urllib.request
import urllib.parse as parse
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plus_url = input('검색어를 입력하세요: ')
url = base_url + parse.quote_plus(plus_url)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()

print(url)