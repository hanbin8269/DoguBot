import urllib.request
from bs4 import BeautifulSoup
import urllib
import requests
from utils.alias import TIER_NUMBER

class OPGGCrawler:
    def __init__(self):
        base_url = "http://www.op.gg"
        
    @staticmethod
    def get_html_from_url(url):
        hdr = {'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.18 Safari/537.36'}
        req = requests.get(url,headers = hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        return soup

    @staticmethod
    def get_profile(nickname):
        soup = OPGGCrawler.get_html_from_url("http://www.op.gg/summoner/userName="+ urllib.parse.quote(str(nickname)))
        #bs_obj = BeautifulSoup(html, "html.parser")
        return soup
    @staticmethod
    def get_tier_list(nicknames) -> list:
        url = "https://www.op.gg/multi_old/query=" + str(nicknames)
        
        soup = OPGGCrawler.get_html_from_url(url)
        tiers = []
        
        parse_string = 'div.lp' if len(nicknames) <= 5 else 'div.TierRank > div.TierRank'
        for i in soup.select(parse_string):
            data = i.text.replace('\n','').split()[:2]
            print("get_tier_list " + str(data))
            if data[0] == 'Level' or data[0] == 'Challenger': # 언랭이나 챌린저면 level,lp를 0으로 만듦
                data[1] = '0'

            tiers.append(data)
        return tiers

    @staticmethod
    def get_rank(nickname):
        
        soup = OPGGCrawler.get_profile(nickname)
        tier_text = ''
        for i in soup.select('div.TierRank'):
            tier_text = i.text
        
        tier_list = tier_text.split()
        try:
            score = TIER_NUMBER[tier_list[0]] + 4 -int(tier_list[1])
        except IndexError:
            score  = TIER_NUMBER[tier_list[0]]
        
        return score

    def get_position(nickname): # 미완성 기능
        soup = OPGGCrawler.get_profile(nickname)
        win_text = ''
        for i in soup.select('span.winratio'):
            win_text = i.text
        win_list = win_text.split()
        win_per = float(win_list[1].replace('%',''))
        return win_per