import re
import json
number = 1
total = []
l = list()
t = ""
with open (r'C:\Users\ASUS\Desktop\program\project\intern-hospital-line-selection\python\line_maker_intern_final.txt', encoding="utf-8", errors="ignore") as file:
    for i in file:
        i = i.strip()
        t = t + i + "\n"
        if i.startswith("</tr"):
            l.append(t)
            t = ""  

def row(data,number):
    useable = data.split('<td')
    dic = {"id":"0", "class":"",
       "first":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "second":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "third":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "forth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "fifth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "sixth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "seventh":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "eighth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "nineth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "tenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "eleventh":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twelveth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirteenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "fourteenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "fifteenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "sixteenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "seventeenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "eighteenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "nineteenth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentieth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentyfirst":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentysecond":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentythird":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentyfourth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentyfifth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentysixth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentyseventh":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentyeighth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "twentyninth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtieth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtyfirst":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtysecond":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtythird":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtyfourth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtyfifth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtysixth":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       "thirtyseventh":{"id":"","title":"","class":"","colspan":"","rowspan":"","content":""},
       }
    dic["id"] = number
    dic["class"] = re.findall('class="(.*?)"',useable[0])[0]
    num = 1
    for position in ["first","second","third","forth","fifth","sixth","seventh","eighth","nineth","tenth","eleventh","twelveth","thirteenth","fourteenth","fifteenth","sixteenth","seventeenth","eighteenth","nineteenth","twentieth","twentyfirst","twentysecond","twentythird","twentyfourth","twentyfifth","twentysixth","twentyseventh","twentyeighth","twentyninth","thirtieth","thirtyfirst","thirtysecond","thirtythird","thirtyfourth","thirtyfifth","thirtysixth","thirtyseventh"]:
        if num < len(useable):
            dic[position] = cell(useable[num])      
            num = num+1       
        else:
            dic.pop(position)
            num = num+1   
    return dic
            
def cell(data):
    dic = {"id":"","title":"","class":"","colspan":"","rowspan":"","content":""}
    try:
        dic["id"] = re.findall('id="(.*?)"',data)[0]
    except:
        dic.pop("id")
    try:
        dic["title"] = re.findall('title="(.*?)"',data)[0]
    except:
        dic.pop("title")
    try:
        dic["class"] = re.findall('class="(.*?)"',data)[0]
    except:
        dic.pop("class")
    try:
        dic["colspan"] = re.findall('colspan="(.*?)"',data)[0]
    except:
        dic.pop("colspan")
    try:
        dic["rowspan"] = re.findall('rowspan="(.*?)"',data)[0]
    except:
        dic.pop("rowspan")
    try:
        dic["content"] = re.findall('>(.*?)</td>',data)[0]
    except:
        dic.pop("content")
    return dic
for i in l:
    a = row(i,number)
    number = number + 1
    total.append(a)
print(total)
with open(r'C:\Users\ASUS\Desktop\program\project\intern-hospital-line-selection\python\line_maker_react_intern_final.txt','w', encoding="utf-8", errors="ignore") as file_total:
    file_total.write(str(total))
#total ro be sayt https://jsonformatter.curiousconcept.com/# midim ke moshkelat ehtemali ra hal konad