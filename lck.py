import requests
from bs4 import BeautifulSoup
import urllib3

source = requests.get("https://qwer.gg/leagues/LCK/2020/summer?type=schedules",verify=False)
source = source.text
soup = BeautifulSoup(source, "html.parser")


today = soup.find("div",{"class":"Calendar__box Calendar__box__today"})
one_day = soup.find("div",{"class":"Calendar__box"}) #test
matches = one_day.findAll("a",{"class":"Calendar__box__matchLink"}) 


#오늘 일정
print("오늘경기")
for i in matches:
    print("-----")
    match = i.find("div",{"class":"Calendar__box__matchLink__teams"})
    teams = match.findAll("img",{"class":"Calendar__box__matchLink__teamLogo"})
    print(i.text[:-2])
    print(teams[0]['src'].split("/")[5].split(".")[0] , "VS" , teams[1]['src'].split("/")[5].split(".")[0])
print("------------------------------------------------------------------------------------")

#일주일 간 일정
week = today.parent
calendar_boxes = week.findAll("div",{"class":"Calendar__box"})

print("이번 주 경기")
for calendar_box in calendar_boxes:
    day_matches = calendar_box.findAll("a",{"class":"Calendar__box__matchLink"})
    date = calendar_box.find("div",{"class":"Calendar__box__dateWrapper"}).text
    print("-----------",date,"-------------------")
    for i in day_matches:
        match = i.find("div",{"class":"Calendar__box__matchLink__teams"})
        teams = match.findAll("img",{"class":"Calendar__box__matchLink__teamLogo"})
        print(i.text[:-2])
        print(teams[0]['src'].split("/")[5].split(".")[0] , "VS" , teams[1]['src'].split("/")[5].split(".")[0])

        print("---------------------")
