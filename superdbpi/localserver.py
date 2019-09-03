import json
from flask import Flask, render_template, request
from flask_cors import CORS
import database

UPLOAD_FOLDER = './img_files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

filepath = "datas/data.json"

app = Flask(__name__)
CORS(app)
#app.logger.disabled = True

#werkzeug_logger = logging.getLogger('werkzeug')
#werkzeug_logger.disabled = True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#ユーザー関連
@app.route('/api/login', methods=["POST"])
def login():
    print(request.get_data())
    data=request.get_data()
    json_data = json.loads(data)
    email = json_data["email"]
    password = json_data["password"]
    return_data = database.login(email, password)
    if return_data == -1:
        print("ユーザーが見つからない")
        return "/USER/"
    elif return_data == -2:
        print("パスワードが違う")
        return "/PASS/"
    else:
        print(return_data)
        return return_data

@app.route('/api/logout', methods=["POST"])
def logout():
    data=request.get_data()
    print(data)
    json_data = json.loads(data)
    session_id = json_data["session_id"]
    return_data = database.delete_session(session_id)
    return return_data

@app.route('/api/signup', methods=["POST"])
def signup():
    data=request.get_data()
    print(data)
    json_data = json.loads(data)
    email = json_data["email"]
    password = json_data["password"]
    username = json_data["username"]
    return_data = database.create_user(username, email, password)
    return return_data

@app.route('/api/check_session', methods=["POST"])
def check_session():
    data=request.get_data()
    print(data)
    json_data = json.loads(data)
    session_id = json_data["session_id"]
    return_data = database.check_session(session_id)
    return return_data

@app.route('/api/userinfo/<user_id>', methods=["GET"])
def userinfo(user_id):
    return_data = database.get_user_info(str(user_id))
    return return_data

#コンテスト関連
@app.route('/api/contest/now', methods=["GET"])
def contestnowinfo():
    return_data = database.now_contest_info()
    return return_data

@app.route('/api/contest/info/<contest_id>', methods=["GET"])
def contestinfo(contest_id):
    return_data = database.contest_info(contest_id)
    return return_data

@app.route('/api/contest/materialsinfo/<contest_id>', methods=["GET"])
def contestmaterialsinfo(contest_id):
    return_data = database.contest_materials_info(contest_id)
    return return_data

@app.route('/api/contest/recipesinfo/<contest_id>', methods=["GET"])
def contestrecipesinfo(contest_id):
    return_data = database.contest_recipes_info(contest_id)
    return return_data

#コンテストに投稿
@app.route('/api/contest/send', methods=['POST'])
def send():
    data=request.get_data()
    print(data)
    json_data = json.loads(data)
    contest_id = json_data["contest_id"]
    user_id = json_data["user_id"]
    title = json_data["title"]
    comment = json_data["comment"]
    url = json_data["url"]
    return_data = database.save_contest_answer(contest_id, user_id, title, comment, url)
    return return_data

#投票
@app.route('/api/contest/vote', methods=['POST'])
def vote():
    data=request.get_data()
    print(data)
    json_data = json.loads(data)
    group_id = json_data["group_id"]
    no1 = json_data["no1"]
    no2 = json_data["no2"]
    no3 = json_data["no3"]
    return_data = database.vote(group_id, no1, no2, no3)
    return return_data

@app.route('/api/contest/memberlistfromuser/<user_id>', methods=["GET"])
def get_member_list_from_user(user_id):
    return_data = database.get_member_list_from_user(user_id)
    return return_data

@app.route('/api/contest/memberlistfromgroop/<group_id>', methods=["GET"])
def get_member_list_from_group(group_id):
    return_data = database.get_member_list_from_group(group_id)
    return return_data

@app.route('/api/contest/rankingmemberlistfromuser/<user_id>', methods=["GET"])
def get_ranking_member_list_from_user(user_id):
    return_data = database.get_ranking_member_list_from_user(user_id)
    return return_data

@app.route('/api/contest/getrandomgroopid', methods=['GET'])
def get_random_group_id():
    return_data = database.get_random_group_id()
    return return_data

@app.route('/api/contest/getentryusertotal', methods=['GET'])
def get_entry_user_total():
    return_data = database.get_entry_user_total()
    return return_data


@app.route('/api/admin/contest/vote', methods=['GET'])
def ad_star_tvote():
    database.start_vote()
    return "投票モード"

@app.route('/api/admin/contest/result', methods=['GET'])
def ad_start_result():
    database.start_result()
    return "結果モード"


#コンテストマッチング関連
def start():
    app.run(port=8080)

start()