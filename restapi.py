from flask import Flask, render_template, request, jsonify, app
import sqlite3
import json
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
import os

# {
#     "key": "how are you",
#     "array": ["zero", "one", "two", "three"]
#
# }
#init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Weather')
cur.execute('CREATE TABLE Weather (outlook TEXT, temp TEXT, humidity TEXT, windy TEXT, play TEXT)')
conn.close()

@app.route('/train', methods=['GET','POST'])
def index():
    outlook     =       request.json['outlook']
    temp        =       request.json['temp']
    humidity    =       request.json['humidity']
    windy       =       request.json['windy']
    play        =       request.json['play']


    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute('INSERT INTO Weather (outlook, temp, humidity,windy,play) VALUES (?, ?, ?, ?, ?)',(outlook, temp, humidity, windy, play))
    conn.commit()

    cur.execute('SELECT outlook, temp, humidity, windy,play FROM Weather')

    for row in cur:
        print(row)
    conn.close()

    return jsonify({'play' : play})

if __name__=="__main__":
    app.debug = True
    app.run(debug=True)


















# #DataBase
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#
# # init db
# db = SQLAlchemy(app)
#
# #init marshmallow
# ma = Marshmallow(app)
#
# #Weather
# class Weather(db.Model):
#     id = db.Column(db.Integer, primary_key= True)
#     outlook = db.Column(db.String(20))
#     temp= db.Column(db.string(20))
#     humidity = db.Column(db.string(20))
#     windy = db.Column(db.string(20))
#     play = db.Column(db.string(20))
#
#     def __init__(self,outlook,temp,humidity,windy,play):
#         self.outlook=  outlook
#         self.temp = temp
#         self.humidity = humidity
#         self.windy = windy
#         self.play = play
#
# #Weather Schema
# class WeatherSchema(ma.Schema):
#     class Meta:
#         fields = ('outlook','temp','humidity','windy','play')
#
# #init Schema
# Weather_Schema = Weather_Schema(strict=True)
# WeatherS_Schema= Weather_Schema(many=True,strict=True)