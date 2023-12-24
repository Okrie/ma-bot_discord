"""
    Log Class
    Question And Answer Log
    Author : Okrie
"""

from module.date.date import get_now_times
import os
import re

class LogClass:
    START_TIME = None
    pattern = re.compile('```ansi\n|\x1B\[.*?m|.*\[\d+;\d+m|\[\d+m|>|>>>|```')

    @classmethod
    def set_value(self, START_TIME):
        self.START_TIME = START_TIME
        
        path = os.getcwd() + '/log'
        f = open(f'{path}/{self.START_TIME}.log', 'a+', encoding='utf8')
        f.close()

    def writeLog(self, message, type='INFO'):
        resultLog = f'{get_now_times()}\tLOG {type}\t{message.guild.name}({message.guild.id})\t{message.channel}\t[{message.author} : {message.content}]'
        self.saveLog(resultLog)
        return print(resultLog)

    def answerLog(self, user, message, answer, type='INFO'):
        resultLog = f'{get_now_times()}\tLOG {type}\t{message.guild.name}({message.guild.id})\t{message.channel}\t[{user} : {answer}]'
        resultLog = resultLog.replace('\n\n', '')
        resultLog = self.pattern.sub('', resultLog)
        resultLog = resultLog.replace('\n', ' ')
        self.saveLog(resultLog)
        return print(resultLog)

    def saveLog(self, strs):
        path = os.getcwd() + '/log'
        f = open(f'{path}/{self.START_TIME}.log', 'a+', encoding='utf8')
        f.write(strs)
        f.write('\n')
        f.close()