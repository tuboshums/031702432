import re
import json

def get_address(w):##获取地址
    addresss=re.sub(r'\d{11}',"",w)
    addresss=re.findall("\D*.*?,(.*?)\.",addresss) 
    addresss=("".join(addresss))
    return(fall(addresss))

def get_phone(w):##获取电话号码
    number=re.findall("\d{11}",w)
    return number

def get_Name(w):##获取姓名
    Names=re.findall("!(\D*.*?),",w)
    ##Names=re.findall("\D*.*?,(.*?)\,",w) 
    return Names


def fall(addresss):
    #匹配省份
    j=re.match(r'.*?(省)',addresss) #省
    if j==None:
        d1=""
    else:
        d1=j.group()
        addresss=re.sub(d1,"",addresss,1)
    
    #匹配市
    j=re.match(r'.*?(市)',addresss)
    if j==None:
        d2=""
    else:
        d2=j.group()
        addresss=re.sub(d2,"",addresss,1)
    
    #匹配县
    j=re.match(r'.*?(县|区|市)',addresss)
    if j==None:
        d3=""
    else:
        d3=j.group()
        addresss=re.sub(d3,"",addresss,1)
        
    #匹配镇
    j=re.match(r'.*?(街道|镇|乡)',addresss)
    if j==None:
        d4=""
    else:
        d4=j.group()
        addresss=re.sub(d4,"",addresss,1)
        
    #匹配路
    j=re.match(r'.*?(路|街|巷)',addresss)
    if j==None:
        d5=""
    else:
        d5=j.group()
        addresss=re.sub(d5,"",addresss,1)
        
    #匹配门号
    j=re.match(r'.*?(号)',addresss)
    if j==None:
        d6=""
    else:
        d6=j.group()
        addresss=re.sub(d6,"",addresss,1)
    #剩下的地址
    d7=addresss
    eed=[]
    eed.append(d1)
    eed.append(d2)
    eed.append(d3)
    eed.append(d4)
    eed.append(d5)
    eed.append(d6)
    eed.append(d7)
    return eed
def end(w):##将姓名，电话号码，地址以此放进输出中
    endss=[]
    name=get_Name(w)
    number=get_phone(w)
    addresss=get_address(w)
    endss.append("".join(name))
    endss.append("".join(number))
    endss.append(addresss)
    return endss   
wen=input()
endw=end(wen)
ends=["姓名","手机","地址"]
f={}
for i in range(len(ends)):
    f[ends[i]]=endw[i]
puts=json.dumps(f,ensure_ascii=False)
print(puts)
