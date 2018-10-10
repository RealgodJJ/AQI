"""
    author: RealgodJJ
    function: Web crawler of AQI
    version: 1.0
    date: 2018/10/9
"""
import requests
from xpinyin import Pinyin
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        返回URL的文本
    """
    url = "http://pm25.in/" + city_pinyin
    request = requests.get(url, timeout=30)
    soup = BeautifulSoup(request.text, 'lxml')
    div_list = soup.find_all("div", {"class": "span1"})

    city_aqi_list = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find("div", {"class": "caption"}).text.strip()
        value = div_content.find("div", {"class": "value"}).text.strip()
        city_aqi_list.append({caption: value})
    return request.status_code, city_aqi_list

def main():
    city = input("请输入城市：\n")
    p = Pinyin()
    city_pinyin = p.get_pinyin(city, '')

    request_code, city_aqi_list = get_city_aqi(city_pinyin)

    print("{}地区的空气质量情况如下：".format(city))
    for city_aqi in city_aqi_list:
        for caption, value in city_aqi.items():
            print("{}: {}".format(caption, value))


if __name__ == '__main__':
    main()
