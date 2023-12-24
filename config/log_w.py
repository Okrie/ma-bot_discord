"""
    Log Class
    Question And Answer Log
    Author : Okrie
"""

from module.date.date import get_now_times
import os

class LogClass:
    START_TIME = None

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
        self.saveLog(resultLog)
        return print(resultLog)

    def saveLog(self, strs):
        path = os.getcwd() + '/log'
        f = open(f'{path}/{self.START_TIME}.log', 'a+', encoding='utf8')
        f.write(strs)
        f.write('\n')
        f.close()