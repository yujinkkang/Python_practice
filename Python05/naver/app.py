# -*- coding:utf-8 -*-
from flask import Flask, render_template
from bs4 import BeautifulSoup
# pip install flask_cors
from flask_cors import CORS
import requests
import json

app =Flask(__name__)

CORS(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/crawling') #, methods=['post']
def crawling():
    #naver movie list를 crawling 해오자
    resp= requests.get('https://movie.naver.com/movie/running/current.nhn')
    soup = BeautifulSoup(resp.text, 'html.parser')

    movie_list = soup.find_all('dl',class_='lst_dsc')
    
    #crawling 된 데이터를 dictionary[{title:제목, star: 별점},...}]로 저장하자
    lst = list()
    for movie in movie_list:
        title= movie.find('a').text
        star= movie.find('span',class_='num').text # = tmp['star'] = movie.select('num')[0].text
        
        tmp={} # = tmp = dict()
        tmp['title'] = title
        tmp['star'] = star
        lst.append(tmp)
        
    
    #json으로 변환하여 리턴하자
    res ={}
    res['movies'] = lst
    res_json = json.dumps(res, ensure_ascii=False)
   
    return res_json

if __name__ =='__main__':
    app.run('localhost',port='8585')
    
    
    
    
    