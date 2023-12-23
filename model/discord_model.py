"""
    Discord Bot Chatting
    Author : Okrie
"""

import discord
import aiohttp
import io, os
from .answer import answer_list
from .maple.maple import get_character_info
from dotenv import load_dotenv

load_dotenv()
CHANNEL = os.environ.get('CHANNEL_ID')
class DiscordClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        await self.change_presence(status=discord.Status.online, activity=discord.Game('대기'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if str(message.content).startswith('?'):
            if message.content == '?ping':
                await message.channel.send(f'pong {message.author.mention}')
            
            else:
                image, answer = self.get_answer(message)
                if image != None:
                    embed = discord.Embed().set_image(url=image)
                await message.reply(answer, embed=embed)
        else:
            return

    def get_answer(self, message):
        text = message.content
        trim_text = text.replace(" ", "")

        answer_dict = answer_list.answer_fn()

        if trim_text == '' or None:
            return "알 수 없는 명령어"
        
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        
        elif trim_text == '?명령어':
            return [v for v in answer_list.answer_dict()]
        
        elif text[:6] in '?캐릭터정보':
            character_name = text[7:]
            image, result = get_character_info(character_name)
            if result == None:
                return '캐릭터 이름을 정확히 입력하세요'
            return image, result
        
        else:
            for key in answer_dict.keys():
                if key.find(trim_text) != -1:
                    return "연관 단어 [" + key + "]에 대한 답변입니다.\n" + answer_dict[key]

            for key in answer_dict.keys():
                if answer_dict[key].find(text[1:]) != -1:
                    return "질문과 가장 유사한 질문 [" + key + "]에 대한 답변이에요.\n" + answer_dict[key]

        return text + "은(는) 없는 질문입니다."