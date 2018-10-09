"""
    author: RealgodJJ
    function:
    version: 1.0
    date:
"""
import requests
from xpinyin import Pinyin


def get_html_text(url):
    """
        返回URL的文本
    """
    request = requests.get(url, timeout=30)
    return request.status_code, request.text


def main():
    city = input("请输入城市：\n")
    p = Pinyin()
    city_pinyin = p.get_pinyin(city, '')
    url = "http://pm25.in/" + city_pinyin
    request_status_code, request_text = get_html_text(url)
    if request_status_code == 200:
        aqi_div = '''<div class="span12 data">
                <div class="span1">
                  <div class="value">
                    '''
        index = request_text.find(aqi_div)
        begin_index = index + len(aqi_div)
        end_index = begin_index + 2
        aqi_value = request_text[begin_index:end_index]
        print("{}的空气质量指数为{}".format(city_pinyin, aqi_value))
    else:
        print("不存在您输入的资源网址！")


if __name__ == '__main__':
    main()
