import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://py4e-data.dr-chuck.net/comments_1901109.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

sum = 0

for tag in tags:
    sum += int(tag.contents[0])
    
print(sum)