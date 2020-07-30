import random
from utils.alias import name_nickname, tier_number
from utils.crawling import OPGGCrawler

class OranizeTeam:

    @staticmethod
    def get_score_list(tiers) -> list:
        score = []
        for i in tiers:
            score.append(tier_number[i[0]] + int(i[1]))
        return score
        
    def common_orgainze(members):
        random.shuffle(members)
        result = {
            "1팀" : members[0:len(members)//2],
            "2팀" : members[len(members)//2:]
        }
        return result

    def tier_organize_reform(members):
        nicknames = []
        for i in members:
            nicknames.append(name_nickname[i][0])
        tiers = OPGGCrawler.get_tier_list(nicknames= nicknames)
        print("tiers : {0}".format(tiers))
        scores = OranizeTeam.get_score_list(tiers)
        print("scores : {0}".format(scores))

        nickname_score = [[i,j] for i,j in zip(nicknames,scores)]

        result = { '1팀' : [], '2팀' : [] }
        for i in range(0,len(nickname_score) - 1 , 2):
            rand = random.randint(0,1)
            result['1팀'].append(nickname_score[i + 1 - rand])
            result['2팀'].append(nickname_score[i + rand])
        return result
        
    def tier_organize(members):
        nicknames = []
        for i in members:
            nicknames.append(name_nickname[i])
        scores = []
        for i in nicknames:
            scores.append(OPGGCrawler.getRank(nickname = i))
        nickname_score = []
        for i, j in zip(nicknames,scores):
            nickname_score.append([i,j])
        print('===================')
        print(nickname_score)

        scores.sort()
        result = {
            "1팀" : [],
            "2팀" : []
        }
        for i in range(0,len(nickname_score) -1,2):
            rand = random.randint(0,1)
            result['1팀'].append(nickname_score[i + 1 - rand])
            result['2팀'].append(nickname_score[i + rand])
        return result