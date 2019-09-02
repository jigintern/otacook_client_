import json, os, random, glob

#セッションの作成
def createsession(userid):
    #sessionidを生成
    sessionid = random.randint(100,9999999999)
    isok = False
    while isok==False:
        path = "users/sessionindex/"+str(sessionid)
        if not os.path.exists(path):
            isok = True

    f = open(path, "w")
    f.write("{\"userid\": \""+str(userid)+"\"}")
    f.close()
    return sessionid

def checksession(sessionid):
    path = "users/sessionindex/"+str(sessionid)
    if os.path.exists(path):
        f = open(path ,'r')
        jsondata = json.load(f)
        f.close()
        userid = str(jsondata["userid"])
    else:
        userid = "-1"
    return userid

#セッションの削除
def deletesession(sessionid):
    try:
        path = "users/sessionindex/"+str(sessionid)
        os.remove(path)
        print("セッション削除 id:" +str(sessionid))
        return "0"
    except:
        return "-1"

#ログイン処理
def login(email, password):

    f = open("users/maillist" ,'r')
    jsondata = json.load(f)
    f.close()

    try:
        userid = jsondata[email]
    except:
        print("メールアドレスが見つからない")
        return -1

    try:
        path = "users/idindex/"+str(userid)
        f = open(path ,'r')
        jsondata = json.load(f)
        f.close()
        dbpassword = jsondata["password"]
        if dbpassword == password:
            print("正しいパスワード")
            sessionid = createsession(userid)
            data = "{\"sessionid\":\""+str(sessionid)+"\",\"userid\":\""+str(userid)+"\"}"
            print(data)
            return data
        else:
            print("間違ったパスワード")
            return -2
    except:
        print("ユーザーが見つからない")
        return -1
    
#ユーザー登録関数
def createuser(username, email, password):
    #useridを生成
    userid = random.randint(100,999999999999999)
    isok = False
    rate = 1000
    while isok==False:
        path = "users/idindex/"+str(userid)
        if not os.path.exists(path):
            isok = True

    #メールアドレスリストをチェックして未登録ならユーザー情報を保存する
    f = open("users/maillist" ,'r')
    jsondata = json.load(f)
    f.close()
    try:
        jsondata[str(email)]
        print("登録済み")
        return "-1"
    except:
        #未登録の場合
        print("未登録")
        jsondata[str(email)] = str(userid)

        writejsondata = json.dumps(jsondata)
        writejsondata = json.loads(writejsondata)
        f2 = open("users/maillist", "w")
        json.dump(writejsondata, f2)
        f2.close()
            
        f = open(path, "w")
        f.write("{\"userid\": \""+str(userid)+"\", \"username\": \""+str(username)+"\", \"email\": \""+str(email)+"\", \"password\": \""+str(password)+"\", \"rate\": \""+str(rate)+"\"}")
        f.close()
        sessionid = createsession(userid)
        data = "{\"sessionid\":\""+str(sessionid)+"\",\"userid\":\""+str(userid)+"\"}"
        print(sessionid)
        return data

#ユーザー情報をとる関数
#ユーザー名メールレートの基本データを返す
def getuserinfo(userid):
    path = "users/idindex/"+str(userid)
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()

    text = "{\"username\":\""+jsondata["username"]+"\",\"email\":\""+jsondata["email"]+"\",\"rate\":\""+jsondata["rate"]+"\"}"
    print(text)
    return text

#実行中のコンテストのIDとステータスを渡す
def nowcontestinfo():
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    print(jsondata)
    return jsondata

#コンテストの情報を返す
def contestinfo(contestid):
    path = "contests/info/"+str(contestid)
    f = open(path ,'r',encoding="utf-8_sig")
    jsondata = json.load(f)
    f.close()
    print(jsondata)
    return jsondata

#コンテストの材料を返す
def contestmaterialsinfo(contestid):
    path = "contests/materials/"+str(contestid)
    f = open(path ,'r',encoding="utf-8_sig")
    jsondata = f.read()
    f.close()
    print(jsondata)
    return jsondata

#コンテストのレシピを返す
def contestrecipesinfo(contestid):
    path = "contests/recipes/"+str(contestid)
    f = open(path ,'r',encoding="utf-8_sig")
    jsondata = f.read()
    f.close()
    print(jsondata)
    return jsondata

#コンテストの結果を保存する
def savecontestanswer(contestid, userid, title, comment, url):
    path = "contests/entry/"+str(contestid)+"/"+str(userid)
    f = open(path, "w")
    f.write("{\"contestid\": \""+str(contestid)+"\", \"userid\": \""+str(userid)+"\", \"title\": \""+str(title)+"\", \"comment\": \""+str(comment)+"\", \"url\": \""+str(url)+"\"}")
    f.close()
    return "0"

#コンテストを投票モードに移行
def startvote():
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]

    useridlist = []
    ratelist = []
    filelist = glob.glob("./contests/entry/"+str(contestid)+"/*")
    for i in filelist:
        userid = i.split("\\")[1]
        #print(userid)

        f = open("users/idindex/"+str(userid) ,'r')
        jsondata = json.load(f)
        f.close()

        rate = jsondata["rate"]
        useridlist.append(userid)
        ratelist.append(rate)
    print(useridlist)
    print(ratelist)

    ratelist, useridlist = zip(*sorted(zip(ratelist,useridlist), reverse=True))
    print(useridlist)
    print(ratelist)

    #並べ替えたやつをグループに入れてく
    text = "{"
    count=0
    count2=4
    count3=0
    for i in useridlist:
        count += 1
        count2 += 1
        count3 += 1
        text += "\""+str(count) +"\":"
        text += "\""+str(i) +"\","
        text += "\""+str(count)+"_total" +"\":\"0\","
        if count2%5 == 0:
            #groopidを生成
            groopid = random.randint(100,999999999999999)
            isok = False
            while isok==False:
                path = "contests/groops/"+str(contestid)+"/"+str(groopid)
                if not os.path.exists(path):
                    isok = True
        #groopidとuseridの紐づけ
        f = open("contests/groopindexfromid/"+str(contestid)+"/"+str(i), "w")
        f.write("{\"groopid\":\""+str(groopid)+"\"}")
        f.close()
        
        if count%5 == 0:
            text += "\"total\":\"0\""
            text += "}"
            f = open(path, "w")
            f.write(text)
            f.close()
            print(text)
            count = 0
            text = "{"

            if((int(len(useridlist))-count3) < 4):
                break
        
        '''if((int(len(useridlist))-count3) < 4):
            if(int(len(useridlist))%5 != 0):
                print("五人以下")
                print(int(len(useridlist))-count3)
                if (int(len(useridlist))-count3) == 0:
                    break
                    text += "\"total\":\"0\""
                    text += "}"
                    print(text)
                    f = open(path, "w")
                    f.write(text)
                    f.close()'''

    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    jsondata["status"] = "2"
    writejsondata = json.dumps(jsondata)
    writejsondata = json.loads(writejsondata)
    f2 = open(path, "w")
    json.dump(writejsondata, f2)
    f2.close()

#コンテストを結果モードに移行
def startresult():
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]
    jsondata["status"] = "3"
    writejsondata = json.dumps(jsondata)
    writejsondata = json.loads(writejsondata)
    f2 = open(path, "w")
    json.dump(writejsondata, f2)
    f2.close()

    grooplist = glob.glob("contests/groops/"+str(contestid)+"/*")
    length = int(len(grooplist))
    for i in range(length):
        path = "contests/groops/"+str(contestid)+"/"+str(grooplist[i].split("\\")[1])
        f = open(path ,'r')
        jsondata = json.load(f)
        f.close()
        totallist = []
        idlist = []
        for i in range(5):
            try:
                totallist.append(jsondata[str(i+1)+"_total"])
            except:
                totallist.append(-1)
        print(totallist)

        for i in range(5):
            try:
                idlist.append(jsondata[str(i+1)])
            except:
                idlist.append(-1)
        print(idlist)

        totallist, idlist = zip(*sorted(zip(totallist,idlist), reverse=True))

        for i in range(5):
            path = "users/idindex/"+str(idlist[i])
            f = open(path ,'r')
            jsondata = json.load(f)
            f.close()
            rate = int(jsondata["rate"])
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
            jsondata["rate"] = str(rate)
            writejsondata = json.dumps(jsondata)
            writejsondata = json.loads(writejsondata)
            f2 = open(path, "w")
            json.dump(writejsondata, f2)
            f2.close()

    return "0"
            
def vote(groopid, no1, no2, no3):
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]

    path = "contests/groops/"+str(contestid)+"/"+str(groopid)
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    total = int(jsondata["total"])
    point = int(jsondata[str(no1) + "_total"])
    point += 3
    jsondata[str(no1) + "_total"] = str(point)

    point = int(jsondata[str(no2) + "_total"])
    point += 2
    jsondata[str(no2) + "_total"] = str(point)

    point = int(jsondata[str(no3) + "_total"])
    point += 1
    jsondata[str(no3) + "_total"] = str(point)

    total += 1
    jsondata["total"] = str(total)

    writejsondata = json.dumps(jsondata)
    writejsondata = json.loads(writejsondata)
    f2 = open(path, "w")
    json.dump(writejsondata, f2)
    f2.close()

    return "0"

def getrandomgroopid():
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]

    filelist = glob.glob("./contests/groops/"+str(contestid)+"/*")
    length = int(len(filelist))
    #print(length)
    print(random.randint(0, length-1))
    groopid = str(filelist[random.randint(0, length-1)]).split("\\")[1]
    print(groopid)
    return groopid

def getmemberlistfromuser(userid):
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]
    print(contestid)

    path = "contests/groopindexfromid/"+str(contestid)+"/"+str(userid)
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    groopid = jsondata["groopid"]
    print(groopid)

    path = "contests/groops/"+str(contestid)+"/"+str(groopid)
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    idlist = []
    for i in range(5):
        try:
            idlist.append(jsondata[str(i+1)])
        except:
            idlist.append(-1)
    print(idlist)

    text = ""
    for i in range(5):
        path = "contests/entry/"+str(contestid)+"/"+str(idlist[i])
        f = open(path ,'r')
        jsondata = json.load(f)
        f.close()
        path = "users/idindex/"+str(idlist[i])
        f = open(path ,'r')
        ujsondata = json.load(f)
        f.close()
        text += "{\"number\":\""+str(i+1)+"\", \"title\":\""+str(jsondata["title"])+"\", \"name\":\""+str(ujsondata["username"])+"\", \"icon\":\"https://vuetifyjs.com/apple-touch-icon-180x180.png\", \"img\":\""+str(jsondata["url"])+"\", \"comment\":\""+str(jsondata["comment"])+"\"}"
        if(i < 4):
            text += ","
    print(text)

    return text

def getmemberlistfromgroop(groopid):
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]
    print(contestid)

    path = "contests/groops/"+str(contestid)+"/"+str(groopid)
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    idlist = []
    for i in range(5):
        try:
            idlist.append(jsondata[str(i+1)])
        except:
            idlist.append(-1)
    print(idlist)

    text = ""
    for i in range(5):
        path = "contests/entry/"+str(contestid)+"/"+str(idlist[i])
        f = open(path ,'r')
        jsondata = json.load(f)
        f.close()
        path = "users/idindex/"+str(idlist[i])
        f = open(path ,'r')
        ujsondata = json.load(f)
        f.close()
        text += "{\"number\":\""+str(i+1)+"\", \"title\":\""+str(jsondata["title"])+"\", \"name\":\""+str(ujsondata["username"])+"\", \"icon\":\"https://vuetifyjs.com/apple-touch-icon-180x180.png\", \"img\":\""+str(jsondata["url"])+"\", \"comment\":\""+str(jsondata["comment"])+"\"}"
        if(i < 4):
            text += ","
    print(text)

    return text


def getrankingmemberlistfromuser(userid):
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]
    print(contestid)

    path = "contests/groopindexfromid/"+str(contestid)+"/"+str(userid)
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    groopid = jsondata["groopid"]
    print(groopid)

    path = "contests/groops/"+str(contestid)+"/"+str(groopid)
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    totallist = []
    idlist = []
    for i in range(5):
        try:
            totallist.append(jsondata[str(i+1)+"_total"])
        except:
            totallist.append(-1)
    print(totallist)

    for i in range(5):
        try:
            idlist.append(jsondata[str(i+1)])
        except:
            idlist.append(-1)
    print(idlist)

    totallist, idlist = zip(*sorted(zip(totallist,idlist), reverse=True))

    print(totallist)
    print(idlist)

    text = ""
    for i in range(5):
        path = "contests/entry/"+str(contestid)+"/"+str(idlist[i])
        f = open(path ,'r')
        jsondata = json.load(f)
        f.close()
        path = "users/idindex/"+str(idlist[i])
        f = open(path ,'r')
        ujsondata = json.load(f)
        f.close()
        text += "{\"rank\":\""+str(i+1)+"\", \"title\":\""+str(jsondata["title"])+"\", \"name\":\""+str(ujsondata["username"])+"\", \"icon\":\"https://vuetifyjs.com/apple-touch-icon-180x180.png\", \"img\":\""+str(jsondata["url"])+"\", \"comment\":\""+str(jsondata["comment"])+"\"}"
        if(i < 4):
            text += ","
    print(text)

    return text

def getentryusertotal():
    path = "contests/now"
    f = open(path ,'r')
    jsondata = json.load(f)
    f.close()
    contestid = jsondata["contestid"]

    filelist = glob.glob("./contests/entry/"+str(contestid)+"/*")
    total = str(len(filelist))
    print(total)
    return total

#getentryusertotal()

#getrankingmemberlistfromuser(107089007957609)

#vote(35327020981809, 1, 2, 3)
#startvote()
#nowcontestinfo()
#contestinfo(1)
#contestmaterialsinfo(1)
#contestresipesinfo(1)

#getuserinfo(367823181502481)
#createuser("おちんちん ", "otinntin@otinntinn.com", "otinntinn")
#login("ufuS","himitu")
#deletesession(100769456888905161181693367)