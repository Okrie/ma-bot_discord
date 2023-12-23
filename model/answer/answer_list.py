from module.date.date import get_day_of_week, get_time

_answerList = {
    '?안녕': 'HI',
    '?요일': f':calendar: 오늘은 {get_day_of_week()}입니다',
    '?시간': f':clock9: 현재 시간은 {get_time()}입니다.',
}

# Answer Return
def answer_fn():
    return _answerList

# Answer List
def answer_dict():
    return _answerList.keys()