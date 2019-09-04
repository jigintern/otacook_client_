import json
import os
import logging
from flask import Flask, render_template, request
from flask_cors import CORS
import database
import glob

UPLOAD_FOLDER = './img_files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

filepath = "datas/data.json"

app = Flask(__name__)
CORS(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#ユーザー関連
@app.route('/api/login', methods=["POST"])
def login():
    print(request.get_data())
    data=request.get_data()
    jsondata = json.loads(data)
    email = jsondata["email"]
    password = jsondata["password"]
    returndata = database.login(email, password)
    if returndata == -1:
        print("ユーザーが見つからない")
        return "/USER/"
    elif returndata == -2:
        print("パスワードが違う")
        return "/PASS/"
    else:
        print(returndata)
        return returndata

@app.route('/api/logout', methods=["POST"])
def logout():
    data=request.get_data()
    print(data)
    jsondata = json.loads(data)
    sessionid = jsondata["sessionid"]
    returndata = database.delete_session(sessionid)
    return returndata

@app.route('/api/signup', methods=["POST"])
def signup():
    data=request.get_data()
    print(data)
    jsondata = json.loads(data)
    email = jsondata["email"]
    password = jsondata["password"]
    username = jsondata["username"]
    returndata = database.create_user(username, email, password)
    return returndata

@app.route('/api/checksession', methods=["POST"])
def check_session():
    data=request.get_data()
    print(data)
    jsondata = json.loads(data)
    sessionid = jsondata["sessionid"]
    returndata = database.check_session(sessionid)
    return returndata

@app.route('/api/userinfo/<userid>', methods=["GET"])
def userinfo(userid):
    returndata = database.get_userinfo(str(userid))
    return returndata

#コンテスト関連
@app.route('/api/contest/now', methods=["GET"])
def contestnowinfo():
    returndata = database.now_contest_info()
    return returndata

@app.route('/api/contest/info/<contestid>', methods=["GET"])
def contest_info(contestid):
    returndata = database.contest_info(contestid)
    return returndata

@app.route('/api/contest/materialsinfo/<contestid>', methods=["GET"])
def contest_materials_info(contestid):
    returndata = database.contest_materials_info(contestid)
    return returndata

@app.route('/api/contest/recipesinfo/<contestid>', methods=["GET"])
def contest_recipes_info(contestid):
    returndata = database.contest_recipes_info(contestid)
    return returndata

#コンテストに投稿
@app.route('/api/contest/send', methods=['POST'])
def send():
    data=request.get_data()
    print(data)
    jsondata = json.loads(data)
    contestid = jsondata["contestid"]
    userid = jsondata["userid"]
    title = jsondata["title"]
    comment = jsondata["comment"]
    url = jsondata["url"]
    returndata = database.save_contest_answer(contestid, userid, title, comment, url)
    return returndata

#投票
@app.route('/api/contest/vote', methods=['POST'])
def vote():
    data=request.get_data()
    print(data)
    jsondata = json.loads(data)
    groopid = jsondata["groopid"]
    no1 = jsondata["no1"]
    no2 = jsondata["no2"]
    no3 = jsondata["no3"]
    returndata = database.vote(groopid, no1, no2, no3)
    return returndata

@app.route('/api/contest/memberlistfromuser/<userid>', methods=["GET"])
def get_memberlist_from_user(userid):
    returndata = database.get_memberlist_from_user(userid)
    return returndata

@app.route('/api/contest/memberlistfromgroop/<groopid>', methods=["GET"])
def getmemberlistfrmgroop(groopid):
    returndata = database.get_memberlist_from_groopid(groopid)
    return returndata

@app.route('/api/contest/rankingmemberlistfromuser/<userid>', methods=["GET"])
def get_ranking_memberlist_from_user(userid):
    returndata = database.get_ranking_memberlist_from_user(userid)
    return returndata

@app.route('/api/contest/getrandomgroopid', methods=['GET'])
def get_random_groopid():
    returndata = database.get_random_groopid()
    return returndata

@app.route('/api/contest/getentryusertotal', methods=['GET'])
def get_entry_user_total():
    returndata = database.get_entry_user_total()
    return returndata


@app.route('/api/admin/contest/vote', methods=['GET'])
def adstart_vote():
    database.start_vote()
    return "投票モード"

@app.route('/api/admin/contest/result', methods=['GET'])
def adstart_result():
    database.start_result()
    return "結果モード"

def start():
    app.run(host='0.0.0.0', port=3031, ssl_context=('server.crt', 'server.key'))

start()