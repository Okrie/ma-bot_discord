"""
    Bot AnswerList
    Author : Okrie
"""

from module.date.date import get_day_of_week, get_time

_answerList = {
    '?안녕': 'HI',
    '?요일': f':calendar: 오늘은 {get_day_of_week()}입니다',
    '?시간': f':clock9: 현재 시간은 {get_time()}입니다.',
    '?캐릭터정보' : 'ex) ?캐릭터정보 캐릭터이름 => 기본 정보가 나옴',
    '?레벨별사냥터' : """```0~30 새비지터미널 뉴트리아 18렙, 33렙있음 
30~48.5 새비지터미널 들개, Mr.해저드의 부하, 와보땅
48.5~52 골드비치퀘스트 
52~60 제1군영 
60~80 조습축습 하늘계단 구름공원4 (텔직업 : 모래성놀이터(64~80)
80~93 미요캐츠 (아리안트 북문 밖)
93~103 폭군의 성채로 가는길
103~111 루디 1~2층 곰돌이랑 로보토이 
(107~111 클라크 (얼장))
설치기 O 111 ~ 122  날절4  -> 122~ 128 폐광1~4 
설치기 X 111 ~ 126 날절4 -> 126~128 시련의동굴 
128 ~ 140 안개낀 숲 
135 ~ 150 파르템 
150 ~ 165 커닝타워 
165 ~ 176 연무장 
176 ~ 186 위험한 파이트클럽 
186 ~ 200 풍화된 바위지대 ~ 버발4```"""
}

# Answer Return
def answer_fn():
    return _answerList

# Answer List
def answer_dict():
    return _answerList.keys()