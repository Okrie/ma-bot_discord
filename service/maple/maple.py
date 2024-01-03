"""
    Maple Story API
    Author : Okrie
    Data based on NEXON Open API
"""

import os
import requests
import json
from dotenv import load_dotenv
from module.date.date import get_now_time

load_dotenv()

APIKEY = os.environ.get('APIKEY')
APIADDRESS = os.environ.get('API_ADDRESS')
API_HEADER = os.environ.get('API_HEADER')
DEFAULT_TYPE = os.environ.get('DEFAULT_TYPE')

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
    try:
        ocid = get_ocid(character_name)
    except Exception as e:
        result = '\n\n```ansi\n{DEFAULT_TYPE}[1;34m캐릭터 정보\n'
        result = result + '[0m생성 된지 얼마 안 된 캐릭터 입니다.'
        result = result + '정보를 받을 수 없습니다.```'
        return result
    nowdate = get_now_time()
    response = requests.get(f'{APIADDRESS}/character/basic?ocid={ocid}&date={nowdate}', headers={API_HEADER:APIKEY})

    if response.status_code == 200:
        # 캐릭터 기본 정보
        res = json.loads(response.text)
        if res['character_class'] != 'null':
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
            except_list = [9, 10, 11, 12, 13, 20, 21, 22, 23, 24, 25, 26, 27, 35, 38, 39, 43]
            result = result + f'\n\n```ansi\n{DEFAULT_TYPE}[1;34m스탯 정보\n\n{DEFAULT_TYPE}[0m'
            for i, v in enumerate(res):
                if i not in except_list:
                    result = result + f"{v['stat_name']} : {v['stat_value']}\n"
            result = result + f'\n\n```\n'
            result = result + f'> 기준 날짜 {nowdate}\n'
            result = result + f'환산 : https://maplescouter.com/info?name={character_name}'
            return image, result
        else:
            result = '\n\n```ansi\n{DEFAULT_TYPE}[1;34m캐릭터 정보\n'
            result = result + '[0m생성 된지 얼마 안 된 캐릭터 입니다.'
            result = result + '정보를 받을 수 없습니다.```'
            return result
        
    
# 유저의 유니온 키운 기록 확인
def get_union_record(character_name):
    ocid = get_ocid(character_name)
    nowdate = get_now_time()
    response = requests.get(f'{APIADDRESS}/user/union-raider?ocid={ocid}&date={nowdate}', headers={API_HEADER:APIKEY})
    if response.status_code == 200:
        # 캐릭터 기본 정보
        res = json.loads(response.text)
        res_union = res['union_block']
        result = f'\n\n```ansi\n{DEFAULT_TYPE}[1;34m유니온 정보\n'
        temp = []
        for v in res_union:
            result = result + f"\n{DEFAULT_TYPE}[0m직업 : {v['block_class']} \n레벨 : {v['block_level']}\n"
            temp.append(v['block_class'])
        result = result + f'\n\n```\n'
        result = result + f'> 기준 날짜 {nowdate}\n'
        print('\n')
        for v in temp:
            print(v)
        return result
    else:
        result = '\n\n```ansi\n{DEFAULT_TYPE}[1;34m유니온 정보\n'
        result = result + '[0m생성 된지 얼마 안 됐거나 현재 정보를 불러 올 수 없는 정보 입니다.'
        result = result + '정보를 받을 수 없습니다.```'
        return result
