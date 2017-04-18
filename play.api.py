#/usr/bin/env python
import requests
import json
import datetime
import time
import hmac
import hashlib
import base64
#from gdauth.auth_request import GeneDockAuth
#https://cn-qingdao-api.genedock.com/accounts/public/projects/default/tools/

# Generate the signature
AccessKeyId=""
AccessKeySecret=""
endpoint="https://cn-beijing-api.genedock.com"
endpoint_header='cn-beijing-api.genedock.com'
account="sunxingqiang"

#singnature
content_md5 = ""
content_type = ""
method="GET"
date=time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
#x-gd header
gd_headers=('x-gd-apiversion:1.0','x-gd-signaturemethod:hmac-sha1-v1')
canonicalized_gd_headers = "\n".join(gd_headers)
#print canonicalized_gd_headers
#https://cn-qingdao-api.genedock.com/accounts/public/projects/default/tools/

canonicalized_resource="/accounts/sunxingqiang/projects/default/tasks/58f09fea534680001f0cc416/jobs/58f09fea534680001f0cc416_58f09fea534680002018005c_GD_report_report2pdf/"
#authoruzation
string_to_sign = method + "\n" + content_md5 + "\n" + content_type + "\n" + date + "\n" + canonicalized_gd_headers +"\n"+ canonicalized_resource
#string_to_sign = method + "\n" + content_md5 + "\n" + content_type + "\n" + date + "\n" + canonicalized_gd_headers +"\n"
#BASE64/hmac
print string_to_sign
h = hmac.new(AccessKeySecret.encode('utf-8'), string_to_sign, hashlib.sha1)
signature = base64.encodestring(h.digest()).strip()

#print signature
#print string_to_sign
# GeneDock AccessKeyId:signature(transform by AccessKeySecret+hmac+hashlib.sha1+base64)
AuthorizationString=('GeneDock ',AccessKeyId,":",signature)
Auth ="".join(AuthorizationString)

ListTools=(endpoint,"accounts", account, "projects/default","tools/")
#https://www.genedock.com/app/Blastn/2/?accountName=sunxingqiang
# GetTool=(endpoint,"accounts", account, "projects/default","tools","blastx","?tool_version=1")
GetTool=(endpoint, "accounts", account, "projects/default","tasks/58f09fea534680001f0cc416/jobs/58f09fea534680001f0cc416_58f09fea534680002018005c_GD_report_report2pdf/")

#GetTool=(endpoint, "accounts", account, "projects/default","toolparameters","Humann2_Pair-ends/?version=1")
#address = "/".join(ListTask)
address = "/".join(GetTool)
#address = "https://cn-beijing-api.genedock.com/accounts/sunxingqiang/projects/default/tools/blastx/"
print address
header={'Authorization':Auth,
       'Date':date,
       'Host':endpoint_header,
       'x-gd-apiversion':'1.0',
       'x-gd-signaturemethod':'hmac-sha1-v1'}

#print header
#print address
r = requests.get(address, headers=header)
#print r.status_code
print r.content
print r.status_code

