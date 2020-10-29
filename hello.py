import werobot

robot = werobot.WeRoBot(token='hello')


@robot.text
def hello_world():
    return "Hello World!"


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.config["APP_ID"] = "wx395b40f4589090ce"
robot.config['ENCODING_AES_KEY'] = 'yWNNztIzU9QCzi8Fu1B74Xe2prp3kpkX2aGqNdUJha4'
robot.run()
