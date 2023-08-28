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
def get_kin_count(query,display):
    encode_query=urllib.parse.quote(query)

    search_url ="https://openapi.naver.com/v1/search/kin?query=" + encode_query

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
            kin_count=0
        else:
            kin_total=math.ceil(response_body_dict['total'] / int(display))
            if kin_total >=1000:
                kin_count=1000
            else:
                kin_count=kin_total
            print("지식인 전체수:" +str(kin_total))
            print("지식인 갯수:" +str(kin_count))
    return kin_count
def get_kin_post(query,display, start_index,sort):
    global no, fs
    encode_query=urllib.parse.quote(query)

    search_url="https://openapi.naver.com/v1/search/kin?query="+encode_query+\
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
                kin_link=response_body_dict['items'][item_index]['kinlink']
                kin_name=response_body_dict['items'][item_index]['kinname']
                post_date=response_body_dict['items'][item_index]['postdate']
                no+=1
                fs.write(str(no)+"건"+title+"\n"+link+"\n"+description+"\n"+kin_name+"\n"\
                    +kin_link+"\n"+post_date+"\n"+"-------------------------------------"+'\n')

            except:
                item_index+=1

if __name__ =='__main__':
    query =input("검색 질의: ")
    no=0
    display=10
    start=1
    sort="date"

    fs=open(query+".txt",'a',encoding='utf-8')
    movie_count=get_kin_count(query, display)
    for start_index in range(start, movie_count +1,display):
        get_kin_post(query,display,start_index,sort)

    fs.close()