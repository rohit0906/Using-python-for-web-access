from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

'''input link=http://py4e-data.dr-chuck.net/comments_417446.xml'''

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input()
html=urlopen(url,context=ctx).read()
soup= BeautifulSoup(html,'html.parser')

tags=soup('a')
sum=0
for i in range(6):
    tag=tags[17]
    url=tag.get('href',None)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

tag=tags[17]
url=tag.get('href',None)
print(tag.contents[0])