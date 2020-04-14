# -*- coding:utf-8 -*-

# pip install flask

from flask import Flask
app = Flask(__name__)


@app.route('/') #url 맵핑
def hello():
    return "Hello, Flask!"

if __name__ =='__main__':
    app.run()

