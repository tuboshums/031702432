import json
import re

def get_province():
    pros=[]
    pros.append(["北京","天津","上海","重庆","河北","山西","辽宁","吉林","黑龙江","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","海南","四川","贵州","云南","陕西","甘肃","青海","台湾","内蒙古自治区","广西壮族自治区","西藏自治区","宁夏回族自治区","新疆维吾尔自治区","香港","澳门"])
    return pros



def fall(addresss):
    sheng=get_province()
    kk=0
    for i in range(len(sheng[0])):
        j=re.match(sheng[0][i],addresss)
        if(j):
            kk=i
            d1=j.group()
            addresss=re.sub(d1,"",addresss,1)
            if i<4:
                 d2=d1+'市'
                 if re.match(r'市',addresss):
                     addresss=re.sub(r'市',"",addresss,1)
            if i>3:  
                 d1=d1+"省"
                 if re.match(r'省',addresss):
                     addresss=re.sub(r'省',"",addresss,1)              
            break
                

    
    #j=re.match(r'.*?(省)',addresss) #省
    #if j==None:
    #    d1=""
    #else:
    #    d1=j.group()
    #    addresss=re.sub(d1,"",addresss,1)
    
    #匹配市
    if kk>3:
        j=re.match(r'.*?(市)',addresss)
        if j==None:
            d2=""
        else:
            d2=j.group()
            addresss=re.sub(d2,"",addresss,1)
    
    #匹配县
    j=re.match(r'.*?(市|区|县)',addresss)
    if j==None:
        d3=""
    else:
        d3=j.group()
        addresss=re.sub(d3,"",addresss,1)
        
    #匹配镇
    j=re.match(r'.*?(镇|街道|乡)',addresss)
    if j==None:
        d4=""
    else:
        d4=j.group()
        addresss=re.sub(d4,"",addresss,1)
        
    #匹配路
    j=re.match(r'.*?(街|路|巷)',addresss)
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
def get_address(w):##获取地址
    addresss=re.sub(r'\d{11}',"",w)
    addresss=re.findall("\D*.*?,(.*?)\.",addresss) 
    addresss=("".join(addresss))
    return(fall(addresss))

def get_phone(w):##获取电话号码
    number=re.findall("\d{11}",w)
    return number

def get_Name(w):##获取姓名
    Names=w[0:w.index(',')]
    return Names
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
