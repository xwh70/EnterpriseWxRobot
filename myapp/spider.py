# coding=utf-8
import requests
from lxml import etree
import datetime
import json
import linecache
import random

"""
@ author:xi
@ 微信:xwh_args
@ 2022-04-19
"""


def request_url(url):
    """
    :return: response对象
    """
    response = requests.get(url)
    # 请求失败的地址写入文件里
    if response.status_code != 200:
        print(datetime.datetime.now() + f": {url} 天气地址请求失败")
    return response


def parse_response(response):
    """
    :param response: response对象
    :return: etree(xpath)对象
    """
    data = response.content.decode()
    html = etree.HTML(data)  # 格式化为xpath对象
    return html  # xpath对象


def parse_response_json(response):
    """
    :param response: response对象
    :return: etree(xpath)对象
    """
    data = response.content.decode()
    return data  # xpath对象


def get_file_data():
    """
    读取本地文件，在天气末尾加的一句名言，我的文件里一共有59行，随机读取1行，可自行更换文件调整参数
    :return:
    """
    content = linecache.getline("dddd.txt", random.randint(1, 59))
    data = content.split(')')[-1].replace("\n", "").replace(" ", "")
    return data


def get_content():
    """
    下面是武汉的天气获取API接口，如果要更换其他城市请直接更改链接最后的city="你所在的城市"
    此链接可以直接在浏览器测试
    :return:
    """
    url = "https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=%E6%AD%A6%E6%B1%89"
    response = requests.get(url)
    html = parse_response_json(response)
    weather_dict = json.loads(html)
    today_data = weather_dict['data'][0]
    content = f"{today_data['date']}:{today_data['week']}\n" \
              f"{today_data['wea']}\n" \
              f"最低气温{today_data['tem2']}°，最高气温{today_data['tem1']}°\n" \
              f"天气状况:{today_data['narrative']}\n" \
              f"日出:{today_data['sunrise']}\n" \
              f"日落:{today_data['sunset']}"

    return content + "\n\n" + get_file_data()


if __name__ == '__main__':
    res = get_content()
    # res = get_file_data()
    print(res)
