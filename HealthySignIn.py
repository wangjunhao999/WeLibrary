import json
import requests
import re
import pymongo
import werobot
import time
import logging

logging.basicConfig(level=logging.INFO)

base_url = "https://xsc-health.wh.sdu.edu.cn"
username = '201700800377'
password = 'whsdu@201700800377'


# 登陆模块
def login(username, password):
    data = {
        "jsonrpc": "2.0", "method": "/v2/login/login", "id": 1,
        "params": [username, password, 'false']
    }
    url = base_url + '/mobile/rpc?p=/v2/login/login&t=' + str(int(time.time() * 1000))
    response = s.post(url=url, json=data, verify=False)
    logging.info(response.json())


def get_id():
    data = {"jsonrpc": "2.0", "method": "/v2/fight/ncp/health/report/getId", "id": 1, "params": []}
    url = base_url + '/mobile/rpc?p=/v2/workorder/action/createWithValidate&t=' + str(int(time.time() * 1000))
    response = s.post(url=url, json=data, verify=False)
    logging.info(response.json())
    return response.json().get('result')


def get_info(id, type='40bca208-5184-11ea-887d-cb65bdaac481'):
    data = {"jsonrpc": "2.0", "method": "/v2/cmdb/ci/getById", "id": 1,
            "params": [type, id]}
    url = base_url + '/mobile/rpc?p=/v2/cmdb/ci/getById&t=' + str(int(time.time() * 1000))
    response = s.post(url=url, json=data, verify=False)
    logging.info(response.json())
    return response.json().get('result')


def post_form(type='40bca208-5184-11ea-887d-cb65bdaac481'):
    id = get_id()
    info = get_info(id=id, type=type)
    data = {
        "jsonrpc": "2.0",
        "method": "/v2/workorder/action/createWithValidate",
        "id": 1,
        "params": [
            [
                {
                    # 不同用户id不同
                    "id": id,
                    "type": type,
                    "source": "mobile",
                    # 不同用户apply_user不同
                    "apply_user": info.get('apply_user').get('id'),
                    "xllb": info.get('xllb').get('id'),
                    # 不同用户所在院系不同
                    "szyx": info.get('apply_department').get('id'),
                    # 不同用户姓名不同
                    "xm": info.get('xm'),
                    # 不同用户学号不同
                    "xh": info.get('xh'),
                    # 不同用户性别不同
                    "xb": info.get('xb').get('id'),
                    # 不同用户联系电话不同
                    "lxdh": info.get('lxdh'),
                    # 不同用户健康状态不同
                    "jkzt": info.get('jkzt').get('id'),
                    # 是否发热
                    "shifoufare": info.get("shifoufare").get('id'),
                    # 体温
                    "tiwen": info.get('tiwen'),
                    # 是否就诊住院
                    "shifoujiuzhenzhuyuan": "",
                    "yiyuanmingcheng": info.get('yiyuanmingcheng'),
                    # 是否隔离
                    "shifougeli": info.get('shifougeli').get('id'),
                    "gelifangshi": "",
                    "gelidizhi": info.get('gelidizhi'),
                    # GPS地区
                    "dw": info.get('dw'),
                    # 春节期间是否在校
                    "cunjieqijianshifouzaixiao": info.get('cunjieqijianshifouzaixiao').get('id'),
                    # 是否在校
                    "shifouzaixiao": info.get('shifouzaixiao').get('id'),
                    # 是否已返回或从未离开威海
                    "shifouyifanhuihuocongweilikaixuexiao": info.get('shifouyifanhuihuocongweilikaixuexiao').get('id'),
                    # 目前所在城市
                    "muqiansuozaichengshi": info.get('muqiansuozaichengshi').get('id'),
                    # 省
                    "sheng": info.get("sheng").get('id'),
                    # 市
                    "shi": info.get('shi').get('id'),
                    # 区
                    "qu": info.get('qu').get('id'),
                    # 详细地址
                    "xxdz": info.get('xxdz'),
                    "guowaidizhi": info.get('guowaidizhi'),
                    # 是否确定返回时间
                    "shifouquedingfanhuishijian": info.get('shifouquedingfanhuishijian').get('id'),
                    # 返回时间
                    "fanhuishijian": info.get('fanhuishijian'),
                    # 近一个月是否过湖北
                    "jinyigeyueshifouquguohubei": info.get('jinyigeyueshifouquguohubei').get('id'),
                    # 近一个月是否接触过确诊病例
                    "jinyigeyueshifoujiechuguoquezhenbingli": info.get('jinyigeyueshifoujiechuguoquezhenbingli').get(
                        'id'),
                    # 近一个月是否接触过疑似病例
                    "jinyigeyueshifoujiechuguoyisibingli": info.get('jinyigeyueshifoujiechuguoyisibingli').get('id'),
                    "miqiejiechuguanxi": "",
                    # 感染着
                    "ganranzhe": info.get('ganranzhe').get('id'),
                    # 接触着
                    "jiechuzhe": info.get('jiechuzhe').get('id'),
                    # 居住
                    "juzhu": info.get('juzhu').get('id'),
                    # 发烧
                    "fare": info.get('fare').get('id'),
                    # 湖北境外
                    "hubeijingwai": info.get('hubeijingwai').get('id')
                }
            ],
            [
                "8a525ad7-5187-11ea-a13f-53bf2079bf35"
            ]
        ]
    }
    url = base_url + '/mobile/rpc?p=/v2/workorder/action/createWithValidate&t=' + str(int(time.time() * 1000))
    response = s.post(url=url, json=data, verify=False)
    logging.info(response.json())


if __name__ == '__main__':
    s = requests.session()
    login(username, password)
    post_form()
