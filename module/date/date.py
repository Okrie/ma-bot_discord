"""
    Date Class
    Get Date Times
    Author : Okrie
"""

from datetime import datetime, timedelta
from pytz import timezone

KST = timezone('Asia/Seoul')

# 현재 요일
def get_day_of_week():
    weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    weekday = weekday_list[datetime.today().weekday()]
    date = datetime.today().strftime("%Y년 %m월 %d일")
    result = '{}({})'.format(date, weekday)
    return result

# 현재 년-월-일
def get_now_time():
    timeis = (datetime.now(tz=KST) - timedelta(1)) if (datetime.now(tz=KST) - timedelta(1)).time().hour < 9 else (datetime.now(tz=KST) - timedelta(2))
    return str(timeis)[:10]

# 현재 시간
def get_time():
    return datetime.today().strftime("%H시 %M분 %S초")

# 현재 년-월-일 시-분-초
def get_now_times(len=23):
    return str(datetime.now(tz=KST))[:len]

