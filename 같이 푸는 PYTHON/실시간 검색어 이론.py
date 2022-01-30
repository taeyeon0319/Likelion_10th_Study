# pip install requests

# 요청하고 응답받기
# client(요청하기) <-----> server(응답하기)
# GET함수(requests.get(url, params=None, **kwargs))

# Beautiful Soup

import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net"
print(requests.get(url)) #<Response [200]> : 잘 응답한다는 뜻

response = requests.get(url)

# 아래 두 출력은 출력값이 같지만 type이 다름!
print(response.text) # type : <class 'str'>
print(BeautifulSoup(response.text, 'html.parser')) # type : <class 'bs4.BeautifulSoup'>


soup = BeautifulSoup(response.text, 'html.parser')

# 파일생성하기
file = open("같이 푸는 PYTHON/daum.html", "w")
file.write(response.text) # r:read w:write a:append
file.close()

# html 문서에서 모든 a태그 가져오기
print(soup.findAll("a"))

