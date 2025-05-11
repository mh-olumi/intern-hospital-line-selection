import re
num = 0
total = " " #from : https://convertio.co/
with open (r'C:\Users\ASUS\Desktop\program\project\intern-hospital-line-selection\python\line_maker_intern.txt', encoding="utf-8", errors="ignore") as file:
    for i in file:
        i = i.strip()
        if re.search('^<td.*',i):
            if i.find('column0') != -1 or i.find('***') != -1 or i.find('آزمون') != -1:
                pass
            else:
                num = num+1
                first = i.split('>')
                second = first[1].split('<')
                last = second[0]
                if i.find('column1 ') != -1:
                    final = last + "-1A"
                elif i.find('column2 ') != -1:
                    final = last + "-1B"
                elif i.find('column3 ') != -1:
                    final = last + "-2A"
                elif i.find('column4 ') != -1:
                    final = last + "-2B"
                elif i.find('column5 ') != -1:
                    final = last + "-3A"
                elif i.find('column6 ') != -1:
                    final = last + "-3B"
                elif i.find('column7 ') != -1:
                    final = last + "-4A"
                elif i.find('column8 ') != -1:
                    final = last + "-4B"
                elif i.find('column9 ') != -1:
                    final = last + "-5A"
                elif i.find('column10 ') != -1:
                    final = last + "-5B"
                elif i.find('column11 ') != -1:
                    final = last + "-6A"
                elif i.find('column12 ') != -1:
                    final = last + "-6B"
                elif i.find('column13 ') != -1:
                    final = last + "-7A"
                elif i.find('column14 ') != -1:
                    final = last + "-7B"
                elif i.find('column15 ') != -1:
                    final = last + "-8A"
                elif i.find('column16 ') != -1:
                    final = last + "-8B"
                elif i.find('column17 ') != -1:
                    final = last + "-9A"
                elif i.find('column18 ') != -1:
                    final = last + "-9B"
                elif i.find('column19 ') != -1:
                    final = last + "-10A"
                elif i.find('column20 ') != -1:
                    final = last + "-10B"
                elif i.find('column21 ') != -1:
                    final = last + "-11A"
                elif i.find('column22 ') != -1:
                    final = last + "-11B"
                elif i.find('column23 ') != -1:
                    final = last + "-12A"
                elif i.find('column24 ') != -1:
                    final = last + "-12B"
                elif i.find('column25 ') != -1:
                    final = last + "-13A"
                elif i.find('column26 ') != -1:
                    final = last + "-13B"
                elif i.find('column27 ') != -1:
                    final = last + "-14A"
                elif i.find('column28 ') != -1:
                    final = last + "-14B"
                elif i.find('column29 ') != -1:
                    final = last + "-15A"
                elif i.find('column30 ') != -1:
                    final = last + "-15B"
                elif i.find('column31 ') != -1:
                    final = last + "-16A"
                elif i.find('column32 ') != -1:
                    final = last + "-16B"
                elif i.find('column33 ') != -1:
                    final = last + "-17A"
                elif i.find('column34 ') != -1:
                    final = last + "-17B"
                elif i.find('column35 ') != -1:
                    final = last + "-18A"
                elif i.find('column36 ') != -1:
                    final = last + "-18B"
                i = i.replace('<td','<td id="p01" title="ttle"')
                i = i.replace("ttle",final)
                i=i.replace("p01",str(num))
        else:
            i = i
        total = total + i + "\n"
print(num)
with open(r'C:\Users\ASUS\Desktop\program\project\intern-hospital-line-selection\python\line_maker_intern_final.txt','w', encoding="utf-8", errors="ignore") as file_total:
    file_total.write(total)
