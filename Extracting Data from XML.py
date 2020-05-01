from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET
import numpy as np

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input()
xml=urlopen(url,context=ctx).read()

#print(xml.decode())

tree=ET.fromstring(xml)
count=tree.findall('.//count')
sum=0
for i in count:
    sum=sum+int(i.text)

print(sum)