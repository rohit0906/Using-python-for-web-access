from urllib.request import urlopen
import ssl
import json


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input()
input=urlopen(url,context=ctx).read()
sum=0

l=json.loads(input)
for i in l["comments"]:
    sum=sum+int(i['count'])

print(sum)