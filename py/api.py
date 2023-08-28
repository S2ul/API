import os
import sys
import urllib.request
client_id = "roUBcoDvfgW4Tu2flyLu"
client_secret = "jGww9cGsvh"
encText = urllib.parse.quote("키링")
url = "https://openapi.naver.com/v1/search/shop?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)