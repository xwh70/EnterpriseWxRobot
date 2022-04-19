# coding=utf-8
import requests

"""
@ author:xi
@ 微信:xwh_args
@ 2022-04-19
"""

url = "*"  # 微信企业版机器人链接，这里要改成自己的机器人链接
"""
:只做了文本类型的，如果想尝试其他数据类型可以才考下面的官方文档
:文档地址：https://developer.work.weixin.qq.com/document/path/91770
"""


def send_message(message):
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "text",
        "text": {"content": message}
    }
    ret = requests.post(
        url=url,
        # 此处为新建机器人以后生成的链接
        headers=headers,
        json=data
    )
    print(ret.text)  # 成功后的打印结果：{"errcode":0,"errmsg":"ok"}



if __name__ == '__main__':
    send_message("燕云十六州")