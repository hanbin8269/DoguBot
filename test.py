import urllib.request
from bs4 import BeautifulSoup
import urllib
import requests

def get_html_from_url(url):
    hdr = {'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.18 Safari/537.36'}
    req = requests.get(url,headers = hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup
"""
['Platinum', '3']
['Iron', '2']
['Challenger', '0']
['Silver', '4']
['Platinum', '4']
['Gold', '3']
['Gold', '2']
['Gold', '2']
['Level', '0']
['Silver', '2']
['Level', '0']
"""
def get_rank_list(nicknames) -> list:
    url = "https://www.op.gg/multi_old/query=" + str(nicknames)
    soup = get_html_from_url(url)
    tiers = []
    for i in soup.select('div.TierRank > div.TierRank'):
        data = i.text.replace('\n','').split()[:2]

        if data[0] == 'Level' or data[0] == 'Challenger': # 언랭이나 챌린저면 level,lp를 0으로 만듦
            data[1] = '0'
        
        tiers.append(data)
    return tiers


get_rank_list(['자이라두둥등장', 'moo호흡딜링머신', '불의축제쓰레기', '황금의왼발황선홍', '복수하는 사자','봉만영', '볼베주면캐리', '야스오장인민채', '난웅동개좁빱채웅', '얼마나오렌지','hide on bush'])
# ["정한빈","류호성","서 진","김승연","김재원","이도건","원준","안채웅","김주성","정현문","이상혁"]