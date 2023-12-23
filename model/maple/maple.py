"""
    Maple Story API
    Author : Okrie
    Data based on NEXON Open API
"""

import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pytz import timezone

load_dotenv()

APIKEY = os.environ.get('APIKEY')
APIADDRESS = os.environ.get('API_ADDRESS')
API_HEADER = os.environ.get('API_HEADER')
KST = timezone('Asia/Seoul')
DEFAULT_TYPE = ''

# maple 캐릭터 ocid 받아오기
def get_ocid(character_name):
    response = requests.get(f'{APIADDRESS}id?character_name={character_name}', headers={API_HEADER:APIKEY})

    if response.status_code != 200:
        return '잘못된 유저 이름을 입력하셨어요'
    else:
        res = json.loads(response.text)
        return res['ocid']


# 캐릭터 정보 받아오기
def get_character_info(character_name):
    ocid = get_ocid(character_name)
    nowdate = str(datetime.now(tz=KST) - timedelta(1))[:10]
    response = requests.get(f'{APIADDRESS}/character/basic?ocid={ocid}&date={nowdate}', headers={API_HEADER:APIKEY})

    if response.status_code == 200:
        # 캐릭터 기본 정보
        res = json.loads(response.text)
        image = str(res['character_image']).replace('"', '')
        result = f'\n\n```ansi\n{DEFAULT_TYPE}[1;34m캐릭터 정보\n'
        result = result + f"\n{DEFAULT_TYPE}[0m이름 : {res['character_name']} \n월드 : {res['world_name']} \n직업 : {res['character_class']} \n레벨 : {res['character_level']} \n경험치 : {res['character_exp_rate'][:-1]} % \n길드 : {res['character_guild_name']}"
        
        # 캐릭터 인기도 정보
        response = requests.get(f'{APIADDRESS}/character/popularity?ocid={ocid}&date={nowdate}', headers={API_HEADER:APIKEY})
        res = json.loads(response.text)
        result = result + f"\n인기도 : {res['popularity']}```"

        # 캐릭터 스탯
        response = requests.get(f'{APIADDRESS}/character/stat?ocid={ocid}&date={nowdate}', headers={API_HEADER:APIKEY})
        res = json.loads(response.text)
        res = res['final_stat']
        result = result + f'\n\n```ansi\n{DEFAULT_TYPE}[1;34m스탯 정보\n\n{DEFAULT_TYPE}[0m'
        for v in res:
            result = result + f"{v['stat_name']} : {v['stat_value']}\n"
        result = result + f'\n\n```\n'
        result = result + f'> 기준 날짜 {nowdate}\n'
        return image, result