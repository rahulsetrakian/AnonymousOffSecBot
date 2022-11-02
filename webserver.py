from flask import Flask, render_template, url_for
from threading import Thread
import json

app = Flask(__name__)
def get_analytics():
    filename='data/analytics.json'
    with open(filename,'r') as file:
        data = json.load(file)
    with open(filename,'w') as file:
        json.dump(data, file)
    Start = data[0]['Start']
    Help = data[0]['Help']
    Cybersecurity = data[0]['Cybersecurity']
    Programming = data[0]['Programming']
    Info = data[0]['Information Technology']
    Pathway = data[0]['Pathway']
    Darkweb = data[0]['Darkweb']
    return Start, Help, Cybersecurity, Programming, Info, Pathway, Darkweb


@app.route('/')
def index():
    Start, Help, Cybersecurity, Programming, Info, Pathway, Darkweb = get_analytics()
    return render_template('index.html',Start=Start, Help=Help, Cybersecurity=Cybersecurity, Programming=Programming, Info=Info, Pathway=Pathway, Darkweb=Darkweb)
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():  
    t = Thread(target=run)
    t.start()