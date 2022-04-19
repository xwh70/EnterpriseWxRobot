import datetime
from myapp import wx_robot as wb
from myapp import spider

"""
@ author:xi
@ 微信:xwh_args
@ 2022-04-19
"""


class Config(object):
    JOBS = [
        {
            'id': 'task1',  # 定时器标识
            'func': 'myapp.timer_inteval:task',  # 指定运行的函数
            'args': (),  # 传入函数的参数
            'trigger': 'interval',  # 指定 定时任务的类型
            'seconds': 5  # 运行的间隔时间，*秒，实际使用或者测试的时候可以调整
        },
        {
            'id': 'task2',  # 定时器标识
            'func': 'myapp.timer_inteval:task2',
            'args': (),
            'trigger': 'cron',  # 指定任务触发器 cron
            'day_of_week': 'mon-fri',  # 每周1至周5
            'hour': 9,  # 早上9点执行
            'minute': 00  # 00分
        }
    ]

    SCHEDULER_API_ENABLED = True


def task():  # 运行的定时任务的函数
    # 这个定时任务用来测试的
    print(datetime.datetime.now())


def task2():
    try:
        res = spider.get_content()
    except Exception as e:
        res = "一花一世界，一叶一菩提"
        print(e)
    wb.send_message(res)


if __name__ == '__main__':
    task2()