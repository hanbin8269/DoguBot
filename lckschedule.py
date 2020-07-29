import requests
from bs4 import BeautifulSoup
import urllib3

class LckSchedule:


    source = requests.get("https://qwer.gg/leagues/LCK/2020/summer?type=schedules",verify=False)
    source = source.text
    soup = BeautifulSoup(source, "html.parser")     
    today = soup.find("div",{"class":"Calendar__box Calendar__box__today"})


    def today_schedule(self):   

        matches = self.today.findAll("a",{"class":"Calendar__box__matchLink"}) 

        result = []
        #오늘 일정
        for i in matches:
            match = i.find("div",{"class":"Calendar__box__matchLink__teams"})
            teams = match.findAll("img",{"class":"Calendar__box__matchLink__teamLogo"})
            team1 = teams[0]['src']
            team2 = teams[1]['src']

            temp = {
                "time":i.text[:-2],
                "team1":team1.split("/")[5].split(".")[0],
                "team2":team2.split("/")[5].split(".")[0],
                "team1_img":team1,
                "team2_img":team2
            }

            result.append(temp)

        return result


    def week_schedule(self):
        week = self.today.parent
        calendar_boxes = week.findAll("div",{"class":"Calendar__box"})

        result = []


        for calendar_box in calendar_boxes:
            day_matches = calendar_box.findAll("a",{"class":"Calendar__box__matchLink"})
            date = calendar_box.find("div",{"class":"Calendar__box__dateWrapper"}).text
            
            day_temp = []

            for i in day_matches:
                match = i.find("div",{"class":"Calendar__box__matchLink__teams"})
                teams = match.findAll("img",{"class":"Calendar__box__matchLink__teamLogo"})
                team1 = teams[0]['src']
                team2 = teams[1]['src']
                
                match_temp = {
                    "date":date,
                    "time":i.text[:-2],
                    "team1":team1.split("/")[5].split(".")[0],
                    "team2":team2.split("/")[5].split(".")[0],
                    "team1_img":team1,
                    "team2_img":team2
                }
                                        
                day_temp.append(match_temp)

            result.append(day_temp)

        return result


lckschedule = LckSchedule()

print(lckschedule.week_schedule())