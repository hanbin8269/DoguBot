import random
from utils.alias import NAME_NICKNAME, TIER_NUMBER
from utils.crawling import OPGGCrawler

class ExtractTeam:
    @staticmethod
    def get_score_list(tiers) -> list:
        score = []
        for i in tiers:
            score.append(TIER_NUMBER[i[0]] + int(i[1]))
        return score
    
    @staticmethod
    def get_team_common(members):
        random.shuffle(members)
        result = {
            "1팀" : members[0:len(members)//2],
            "2팀" : members[len(members)//2:]
        }
        return result

    @staticmethod
    def get_team_with_tier(members):
        nicknames = []
        for i in members:
            nicknames.append(NAME_NICKNAME[i][0])
        tiers = OPGGCrawler.get_tier_list(nicknames= nicknames)
        print("tiers : {0}".format(tiers))
        scores = ExtractTeam.get_score_list(tiers)
        print("scores : {0}".format(scores))

        nickname_score = [[i,j] for i,j in zip(nicknames,scores)]

        result = { '1팀' : [], '2팀' : [] }
        for i in range(0,len(nickname_score) - 1 , 2):
            rand = random.randint(0,1)
            result['1팀'].append(nickname_score[i + 1 - rand])
            result['2팀'].append(nickname_score[i + rand])
        return result