import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 0 - 월, 1 - 화, 2 - 수, 3 - 목, 4 - 금, 5 - 토, 6 - 일
today = datetime.today().weekday()
print(datetime.today())
file = open('today_menu.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환

webpage = requests.get("https://sobi.jbnu.ac.kr/menu/week_menu.php")
webpage.encoding = 'UTF-8'
soup = BeautifulSoup(webpage.content, "html.parser")
target = soup.find('table', { 'class':'tblType03'})

tbody = target.find('tbody')
rows = tbody.find_all("tr")[0]
columns = rows.find_all("td")

arr = []
for i in range(5):
    temp = columns[i].find_all("li")
    save_text = ""
    first = True
    for j in temp:
        text = j.text
        if len(text) != 0:
            if first:
                save_text = text
                first = False
            else :
                save_text = save_text + ', ' + text
            #print(j.text)
            
    #print()
    arr.append(save_text)
print(today, "sdsd")
print(arr[today])
if today >= 5:
    file.write("오늘은 운영하지 않습니다.")
else:
    file.write(arr[today])      # 파일에 문자열 저장
file.close()                # 파일 객체 닫기
