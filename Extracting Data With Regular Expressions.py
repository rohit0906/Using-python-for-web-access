import re
sum=0
handle=open('test.txt')
for line in handle:
    #line=line.split()
    dig=re.findall('[0-9]+', line)
    if len(dig)==0:continue
    for n in dig:
        sum=sum+int(n)
    print(dig)
print(sum)
