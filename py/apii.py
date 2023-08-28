import re
import json
import math
import datetime
import requests
import urllib.request
import urllib.error
import urllib.parse
import lxml
from bs4 import BeautifulSoup

naver_client_id = "roUBcoDvfgW4Tu2flyLu"
naver_client_secret = "jGww9cGsvh"
if __name__ =='__main__':
    no=0
    query="컴퓨터"
    display=10
    start=1
    sort="date"

    fs=open(query+".txt",'a',encoding='utf-8')
    fs.close()
def get_blog_count(query,display):
    encode_query=urllib.parse.quote(query)

    search_url ="https://openapi.naver.com/v1/search/blog?query=" + encode_query

    request =urllib.request.Request(search_url)

    request.add_header("X-Naver-Client-Id",naver_client_id)
    request.add_header("X-Naver-Client-Secret",naver_client_secret)

    response =urllib.request.urlopen(request)

    response_code=response.getcode()

    if response_code ==200:
        response_body=response.read()
        response_body_dict=json.loads(response_body.decode('utf-8'))

        print("lastBuildDate:"+str(response_body_dict['lastBuildDate']))
        print("total:"+str(response_body_dict['total']))
        print("start:"+str(response_body_dict['start']))
        print("display:"+str(response_body_dict['display']))

        if response_body_dict['total']==0:
            blog_count=0
        else:
            blog_total=math.ceil(response_body_dict['total'] / int(display))
            if blog_total >=1000:
                blog_count=1000
            else:
                blog_count=blog_total
            print("블로그 전체수:" +str(blog_total))
            print("블로그 갯수:" +str(blog_count))
    return blog_count
def get_blog_post(query,display, start_index,sort):
    global no, fs
    encode_query=urllib.parse.quote(query)

    search_url="https://openapi.naver.com/v1/search/blog?query="+encode_query+\
        "&display="+str(display)+"&start=" +str(start_index)+"&sort="+sort

    request=urllib.request.Request(search_url)

    request.add_header("X-Naver-Client-Id",naver_client_id)
    request.add_header("X-Naver-Client-Secret",naver_client_secret)

    response =urllib.request.urlopen(request)

    response_code=response.getcode()
    if response_code ==200:
        response_body=response.read()
        response_body_dict=json.loads(response_body.decode('utf-8'))

        for item_index in range(0, len(response_body_dict['items'])):
            try:
                remove_html_tag=re.complie('<.*?')
                title=re.sub(remove_html_tag, '',response_body_dict['items'][item_index]['title'])
                link=response_body_dict['items'][item_index]['link'].replace("amp;","")
                description=re.sub(remove_html_tag, '',response_body_dict['items'][item_index]['description'])
                blogger_name=response_body_dict['items'][item_index]['bloggername']
                blogger_link=response_body_dict['items'][item_index]['bloggerlink']
                post_date=response_body_dict['items'][item_index]['postdate']
                no+=1
                fs.write(str(no)+"건"+title+"\n"+link+"\n"+description+"\n"+blogger_name+"\n"\
                    +blogger_link+"\n"+post_date+"\n"+"-------------------------------------"+'\n')

            except:
                item_index+=1

if __name__ =='__main__':
    query =input("검색 질의: ")
    no=0
    display=10
    start=1
    sort="date"

    fs=open(query+".txt",'a',encoding='utf-8')
    blog_count=get_blog_count(query, display)
    for start_index in range(start, blog_count +1,display):
        get_blog_post(query,display,start_index,sort)

    fs.close()