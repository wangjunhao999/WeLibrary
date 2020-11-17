import werobot
import re
import requests

robot = werobot.WeRoBot(token='hello')


@robot.filter(re.compile(".*?帮助.*?"))
def help(message):
    reply = "如需帮助,请联系管理员Email:1138700280@qq.com"
    return reply


@robot.filter(re.compile(".*?洛天依借记卡.*?"))
def card(message):
    response = requests.post(
        url='https://cloud.bankofchina.com/sh/api/cas_SC/common/jjk/queryJJKCardProgress/esb',
        data={
            'name': '王蕾锦',
            'idType': '01',
            'id': '510524199907250817'
        })
    return response.json()


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.config["APP_ID"] = "wx395b40f4589090ce"
robot.config['ENCODING_AES_KEY'] = 'yWNNztIzU9QCzi8Fu1B74Xe2prp3kpkX2aGqNdUJha4'
robot.run()
