import werobot
import re

robot = werobot.WeRoBot(token='hello')


@robot.filter(re.compile(".*?帮助.*?"))
def help(message):
    reply = "如需帮助,请联系管理员Email:1138700280@qq.com"
    return reply


def get_username(message):
    pass


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 10000
robot.config["APP_ID"] = "wx395b40f4589090ce"
robot.config['ENCODING_AES_KEY'] = 'yWNNztIzU9QCzi8Fu1B74Xe2prp3kpkX2aGqNdUJha4'
robot.run()
