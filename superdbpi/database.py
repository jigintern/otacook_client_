import json, os, random, glob

#セッションの作成
def create_session(user_id):
    #session_idを生成
    session_id = random.randint(100,9999999999)
    isOk = False
    while isOk == False:
        path = "users/sessionindex/"+str(session_id)
        if not os.path.exists(path):
            isOk = True

    with open(path, 'w') as f:
        f.write("{\"user_id\": \""+str(user_id)+"\"}")

    return session_id

def check_session(session_id):
    path = "users/sessionindex/"+str(session_id)
    if os.path.exists(path):
        with open(path ,'r') as f:
            json_data = json.load(f)

        user_id = str(json_data["user_id"])
    else:
        user_id = "-1"
    return user_id

#セッションの削除
def delete_session(session_id):
    try:
        path = "users/sessionindex/"+str(session_id)
        os.remove(path)
        print("セッション削除 id:" +str(session_id))
        return "0"
    except:
        return "-1"

#ログイン処理
def login(email, password):

    f = open("users/maillist" ,'r')
    json_data = json.load(f)
    f.close()

    try:
        user_id = json_data[email]
    except:
        print("メールアドレスが見つからない")
        return -1

    try:
        path = "users/idindex/"+str(user_id)
        f = open(path ,'r')
        json_data = json.load(f)
        f.close()
        db_password = json_data["password"]
        if db_password == password:
            print("正しいパスワード")
            session_id = create_session(user_id)
            data = "{\"session_id\":\""+str(session_id)+"\",\"user_id\":\""+str(user_id)+"\"}"
            print(data)
            return data
        else:
            print("間違ったパスワード")
            return -2
    except:
        print("ユーザーが見つからない")
        return -1
    
#ユーザー登録関数
def create_user(username, email, password):
    #useridを生成
    user_id = random.randint(100,999999999999999)
    isOk = False
    rate = 1000
    while isOk==False:
        path = "users/idindex/"+str(user_id)
        if not os.path.exists(path):
            isOk = True

    #メールアドレスリストをチェックして未登録ならユーザー情報を保存する
    with open("users/maillist" ,'r') as f:
        json_data = json.load(f)

    try:
        json_data[str(email)]
        print("登録済み")
        return "-1"
    except:
        #未登録の場合
        print("未登録")
        json_data[str(email)] = str(user_id)

        write_json_data = json.dumps(json_data)
        write_json_data = json.loads(write_json_data)
        f = open("users/maillist", "w")
        json.dump(write_json_data, f)
        f.close()
            
        f = open(path, "w")
        f.write("{\"user_id\": \""+str(user_id)+"\", \"username\": \""+str(username)+"\", \"email\": \""+str(email)+"\", \"password\": \""+str(password)+"\", \"rate\": \""+str(rate)+"\"}")
        f.close()
        session_id = create_session(user_id)
        data = "{\"session_id\":\""+str(session_id)+"\",\"user_id\":\""+str(user_id)+"\"}"
        print(session_id)
        return data

#ユーザー情報をとる関数
#ユーザー名メールレートの基本データを返す
def get_user_info(user_id):
    path = "users/idindex/"+str(user_id)
    with open(path ,'r') as f:
        json_data = json.load(f)

    text = "{\"username\":\""+json_data["username"]+"\",\"email\":\""+json_data["email"]+"\",\"rate\":\""+json_data["rate"]+"\"}"
    print(text)
    return text

#実行中のコンテストのIDとステータスを渡す
def now_contest_info():
    path = "contests/now"
    with open(path ,'r') as f:
        json_data = json.load(f)

    print(json_data)
    return json_data

#コンテストの情報を返す
def contest_info(contest_id):
    path = "contests/info/"+str(contest_id)
    with open(path ,'r',encoding="utf-8_sig") as f:
        json_data = json.load(f)

    print(json_data)
    return json_data

#コンテストの材料を返す
def contest_materials_info(contest_id):
    path = "contests/materials/"+str(contest_id)
    with open(path, 'r', encoding="utf-8_sig") as f:
        json_data = f.read()

    print(json_data)
    return json_data

#コンテストのレシピを返す
def contest_recipes_info(contest_id):
    path = "contests/recipes/"+str(contest_id)
    with open(path ,'r',encoding="utf-8_sig") as f:
        json_data = f.read()

    print(json_data)
    return json_data

#コンテストの結果を保存する
def save_contest_answer(contest_id, user_id, title, comment, url):
    path = "contests/entry/"+str(contest_id)+"/"+str(user_id)
    with open(path, "w") as f:
        f.write("{\"contest_id\": \""+str(contest_id)+"\", \"user_id\": \""+str(user_id)+"\", \"title\": \""+str(title)+"\", \"comment\": \""+str(comment)+"\", \"url\": \""+str(url)+"\"}")

    return "0"

#コンテストを投票モードに移行
def start_vote():
    path = "contests/now"
    with open(path ,'r') as f:
        json_data = json.load(f)

    contest_id = json_data["contest_id"]

    user_id_list = []
    rate_list = []
    file_list = glob.glob("./contests/entry/"+str(contest_id)+"/*")
    for i in file_list:
        user_id = i.split("\\")[1]
        #print(user_id)

        with open("users/idindex/"+str(user_id) ,'r') as f:
            json_data = json.load(f)

        rate = json_data["rate"]
        user_id_list.append(user_id)
        rate_list.append(rate)
    print(user_id_list)
    print(rate_list)

    rate_list, user_id_list = zip(*sorted(zip(rate_list,user_id_list), reverse=True))
    print(user_id_list)
    print(rate_list)

    #並べ替えたやつをグループに入れてく
    text = "{"
    count=0
    count2=4
    count3=0
    for i in user_id_list:
        count += 1
        count2 += 1
        count3 += 1
        text += "\""+str(count) +"\":"
        text += "\""+str(i) +"\","
        text += "\""+str(count)+"_total" +"\":\"0\","
        if count2%5 == 0:
            #groopidを生成
            group_id = random.randint(100,999999999999999)
            isOk = False
            while isOk==False:
                path = "contests/groops/"+str(contest_id)+"/"+str(group_id)
                if not os.path.exists(path):
                    isOk = True
        #groopidとuseridの紐づけ
        with open("contests/groopindexfromid/"+str(contest_id)+"/"+str(i), "w") as f:
            f.write("{\"group_id\":\""+str(group_id)+"\"}")
        
        if count%5 == 0:
            text += "\"total\":\"0\""
            text += "}"
            with open(path, "w") as f: 
                f.write(text)

            print(text)
            count = 0
            text = "{"

            if((int(len(user_id_list))-count3) < 4):
                break
        
        '''if((int(len(user_id_list))-count3) < 4):
            if(int(len(user_id_list))%5 != 0):
                print("五人以下")
                print(int(len(user_id_list))-count3)
                if (int(len(user_id_list))-count3) == 0:
                    break
                    text += "\"total\":\"0\""
                    text += "}"
                    print(text)
                    f = open(path, "w")
                    f.write(text)
                    f.close()'''

    path = "contests/now"
    with open(path, "w") as f:
        json_data = json.load(f)

    json_data["status"] = "2"
    write_json_data = json.dumps(json_data)
    write_json_data = json.loads(write_json_data)
    with open(path, "w") as f:
        json.dump(write_json_data, f)

#コンテストを結果モードに移行
def start_result():
    path = "contests/now"
    with open(path, "r") as f:
        json_data = json.load(f)
    contest_id = json_data["contest_id"]
    json_data["status"] = "3"
    write_json_data = json.dumps(json_data)
    write_json_data = json.loads(write_json_data)
    with open(path, "w") as f:
        json.dump(write_json_data, f)

    groop_list = glob.glob("contests/groops/"+str(contest_id)+"/*")
    length = int(len(groop_list))
    for i in range(length):
        path = "contests/groops/"+str(contest_id)+"/"+str(groop_list[i].split("\\")[1])
        with open(path ,'r') as f: 
            json_data = json.load(f)

        total_list = []
        id_list = []
        for i in range(5):
            try:
                total_list.append(json_data[str(i+1)+"_total"])
            except:
                total_list.append(-1)
        print(total_list)

        for i in range(5):
            try:
                id_list.append(json_data[str(i+1)])
            except:
                id_list.append(-1)
        print(id_list)

        total_list, id_list = zip(*sorted(zip(total_list,id_list), reverse=True))

        for i in range(5):
            path = "users/idindex/"+str(id_list[i])
            f = open(path ,'r')
            json_data = json.load(f)
            f.close()
            rate = int(json_data["rate"])
            if(i == 0):
                rate += (100)
            if(i == 1):
                rate += (50)
            if(i == 2):
                rate += (0)
            if(i == 3):
                rate += (-50)
            if(i == 4):
                rate += (-100)
            json_data["rate"] = str(rate)
            write_json_data = json.dumps(json_data)
            write_json_data = json.loads(write_json_data)
            with open(path, "w") as f:
                json.dump(write_json_data, f)
    return "0"
            
def vote(group_id, no1, no2, no3):
    path = "contests/now"
    with open(path ,'r') as f:
        json_data = json.load(f)
    contest_id = json_data["contest_id"]

    path = "contests/groops/"+str(contest_id)+"/"+str(group_id)
    with open(path ,'r') as f:
        json_data = json.load(f)

    total = int(json_data["total"])
    point = int(json_data[str(no1) + "_total"])
    point += 3
    json_data[str(no1) + "_total"] = str(point)

    point = int(json_data[str(no2) + "_total"])
    point += 2
    json_data[str(no2) + "_total"] = str(point)

    point = int(json_data[str(no3) + "_total"])
    point += 1
    json_data[str(no3) + "_total"] = str(point)

    total += 1
    json_data["total"] = str(total)

    write_json_data = json.dumps(json_data)
    write_json_data = json.loads(write_json_data)
    with open(path ,'w') as f:
        json.dump(write_json_data, f)

    return "0"

def get_random_group_id():
    path = "contests/now"
    with open(path ,'r') as f:
        json_data = json.load(f)
    contest_id = json_data["contest_id"]

    file_list = glob.glob("./contests/groops/"+str(contest_id)+"/*")
    length = int(len(file_list))
    #print(length)
    print(random.randint(0, length-1))
    group_id = str(file_list[random.randint(0, length-1)]).split("\\")[1]
    print(group_id)
    return group_id

def get_member_list_fromuser(user_id):
    path = "contests/now"
    with open(path ,'r') as f: 
        json_data = json.load(f)
    contest_id = json_data["contest_id"]
    print(contest_id)

    path = "contests/groopindexfromid/"+str(contest_id)+"/"+str(user_id)
    f = open(path ,'r')
    json_data = json.load(f)
    f.close()
    group_id = json_data["group_id"]
    print(group_id)

    path = "contests/groops/"+str(contest_id)+"/"+str(group_id)
    with open(path ,'r') as f:
        json_data = json.load(f)
    id_list = []
    for i in range(5):
        try:
            id_list.append(json_data[str(i+1)])
        except:
            id_list.append(-1)
    print(id_list)

    text = ""
    for i in range(5):
        path = "contests/entry/"+str(contest_id)+"/"+str(id_list[i])
        with open(path ,'r') as f:
            json_data = json.load(f)
        path = "users/idindex/"+str(id_list[i])
        with open(path ,'r') as f:
            u_json_data = json.load(f)
        text += "{\"number\":\""+str(i+1)+"\", \"title\":\""+str(json_data["title"])+"\", \"name\":\""+str(u_json_data["username"])+"\", \"icon\":\"https://vuetifyjs.com/apple-touch-icon-180x180.png\", \"img\":\""+str(json_data["url"])+"\", \"comment\":\""+str(json_data["comment"])+"\"}"
        if(i < 4):
            text += ","
    print(text)

    return text

def get_member_list_from_group(group_id):
    path = "contests/now"
    with open(path ,'r') as f:
        json_data = json.load(f)
    contest_id = json_data["contest_id"]
    print(contest_id)

    path = "contests/groops/"+str(contest_id)+"/"+str(group_id)
    f = open(path ,'r')
    json_data = json.load(f)
    f.close()
    id_list = []
    for i in range(5):
        try:
            id_list.append(json_data[str(i+1)])
        except:
            id_list.append(-1)
    print(id_list)

    text = ""
    for i in range(5):
        path = "contests/entry/"+str(contest_id)+"/"+str(id_list[i])
        f = open(path ,'r')
        json_data = json.load(f)
        f.close()
        path = "users/idindex/"+str(id_list[i])
        f = open(path ,'r')
        u_json_data = json.load(f)
        f.close()
        text += "{\"number\":\""+str(i+1)+"\", \"title\":\""+str(json_data["title"])+"\", \"name\":\""+str(u_json_data["username"])+"\", \"icon\":\"https://vuetifyjs.com/apple-touch-icon-180x180.png\", \"img\":\""+str(json_data["url"])+"\", \"comment\":\""+str(json_data["comment"])+"\"}"
        if(i < 4):
            text += ","
    print(text)

    return text


def get_ranking_member_list_from_user(user_id):
    path = "contests/now"
    with open(path ,'r') as f: 
        json_data = json.load(f)
    contest_id = json_data["contest_id"]
    print(contest_id)

    path = "contests/groopindexfromid/"+str(contest_id)+"/"+str(user_id)
    with open(path ,'r') as f: 
        json_data = json.load(f)
    group_id = json_data["group_id"]
    print(group_id)

    path = "contests/groops/"+str(contest_id)+"/"+str(group_id)
    with open(path ,'r') as f:
        json_data = json.load(f)
    total_list = []
    id_list = []
    for i in range(5):
        try:
            total_list.append(json_data[str(i+1)+"_total"])
        except:
            total_list.append(-1)
    print(total_list)

    for i in range(5):
        try:
            id_list.append(json_data[str(i+1)])
        except:
            id_list.append(-1)
    print(id_list)

    total_list, id_list = zip(*sorted(zip(total_list,id_list), reverse=True))

    print(total_list)
    print(id_list)

    text = ""
    for i in range(5):
        path = "contests/entry/"+str(contest_id)+"/"+str(id_list[i])
        with open(path ,'r') as f:
            json_data = json.load(f)

        path = "users/idindex/"+str(id_list[i])
        with open(path ,'r') as f:
            u_json_data = json.load(f)
        text += "{\"rank\":\""+str(i+1)+"\", \"title\":\""+str(json_data["title"])+"\", \"name\":\""+str(u_json_data["username"])+"\", \"icon\":\"https://vuetifyjs.com/apple-touch-icon-180x180.png\", \"img\":\""+str(json_data["url"])+"\", \"comment\":\""+str(json_data["comment"])+"\"}"
        if(i < 4):
            text += ","
    print(text)

    return text

def get_entry_user_total():
    path = "contests/now"
    with open(path ,'r') as f:
        json_data = json.load(f)
    contest_id = json_data["contest_id"]

    file_list = glob.glob("./contests/entry/"+str(contest_id)+"/*")
    total = str(len(file_list))
    print(total)
    return total

#get_entry_user_total()

#get_ranking_member_list_from_user(107089007957609)

#vote(35327020981809, 1, 2, 3)
#start_vote()
#now_contest_info()
#contest_info(1)
#contest_materials_info(1)
#contestresipesinfo(1)

#get_user_info(367823181502481)
#create_user("おちんちん ", "otinntin@otinntinn.com", "otinntinn")
#login("ufuS","himitu")
#delete_session(100769456888905161181693367)