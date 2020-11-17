import werobot
import re
import requests

robot = werobot.WeRoBot(token='hello')


@robot.filter(re.compile(".*?帮助.*?"))
def help(message):
    reply = "如需帮助,请联系管理员Email:1138700280@qq.com"
    return reply


@robot.filter(re.compile(".*?洛天依.*?"))
def card(message):
    response = requests.post(
        url='https://cloud.bankofchina.com/sh/api/cas_SC/common/jjk/queryJJKCardProgress/esb',
        data={
            'name': '王蕾锦',
            'idType': '01',
            'id': '510524199907250817'
        })
    response = response.json()
    status = response['data']['cardList'][0]['status']
    applyTypeChinese = {
        "01": "已受理",
        "02": "审批处理中",
        "03": "审批通过",
        "12": "审批未通过",
        "04": "待开卡",
        "14": "开卡失败",
        "05": "制卡中",
        "06": "已寄发",
        "07": "开卡成功",
        "A2": "批量待处理",
        "A3": "开客户号中",
        "A4": "开卡中",
        "A5": "待制三方信息中",
        "A6": "三方信息制作中",
        "A7": "待制卡函文件"
    }
    statusOfChinese = applyTypeChinese.get(status)
    response['data']['cardList'][0]['status'] = statusOfChinese
    print(response['data']['cardList'][0])
    return response['data']['cardList'][0]


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.config["APP_ID"] = "wx395b40f4589090ce"
robot.config['ENCODING_AES_KEY'] = 'yWNNztIzU9QCzi8Fu1B74Xe2prp3kpkX2aGqNdUJha4'
robot.run()
