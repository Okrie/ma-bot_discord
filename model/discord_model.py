import discord
from datetime import datetime
from .answer import answer_list

class DiscordClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        await self.change_presence(status=discord.Status.online, activity=discord.Game('대기'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content == '?ping':
            await message.channel.send(f'pong {message.author.mention}')
        
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)

    def get_answer(self, text):
        trim_text = text.replace(" ", "")

        answer_dict = answer_list.answer_fn()

        if trim_text == '' or None:
            return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
        
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        
        elif trim_text == '?명령어':
            return [v for v in answer_list.answer_dict()]
        
        
        else:
            for key in answer_dict.keys():
                if key.find(trim_text) != -1:
                    return "연관 단어 [" + key + "]에 대한 답변입니다.\n" + answer_dict[key]

            for key in answer_dict.keys():
                if answer_dict[key].find(text[1:]) != -1:
                    return "질문과 가장 유사한 질문 [" + key + "]에 대한 답변이에요.\n" + answer_dict[key]

        return text + "은(는) 없는 질문입니다."