from lxml import html
import requests
import sqlite3


conn = sqlite3.connect("weather.db")
c = conn.cursor()
d_i=[3,4,9,14] #,17,27,28
for y in range(2010,2019):
    d_arr = [y]
    for m in range(12):
        url = 'http://www.pogodaiklimat.ru/summary.php?m=%d&y=%d&id=26063' % (m+1,y)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        for d in (range(31)):
            for i in d_i:
                temp = tree.xpath('//tr[%d]/td[%d]/text()' % (d+3,i))
                #print(temp)
                if temp != []:
                    d_arr.append(str(temp[0]))
                else:
                    break
            #print(d_arr,len(d_arr))
            if d_arr[0] != [] and len(d_arr) > 1 :
                c.execute("INSERT INTO weather VALUES (?,?,?,?,?)", (d_arr))
                d_arr =[y]
conn.commit()
conn.close()
       
#with open('test.html', 'w') as output_file:
#  output_file.write(tree)


