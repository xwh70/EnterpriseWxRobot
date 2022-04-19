from flask import Flask
from myapp import timer_inteval
from flask_apscheduler import APScheduler

"""
@ author:xi
@ 微信:xwh_args
@ 2022-04-19
"""

app = Flask(__name__)  # 实例化flask


@app.route("/")
def hello():
    return "hello world"


# 配置定时任务
app.config.from_object(timer_inteval.Config())  # 为实例化的 flask 引入配置
scheduler = APScheduler()  # 实例化 APScheduler
scheduler.init_app(app)  # 把任务列表放入 flask
scheduler.start()  # 启动任务列表


if __name__ == '__main__':
    app.run()