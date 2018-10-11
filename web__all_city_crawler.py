"""
    author: RealgodJJ
    function: Web crawler for all city of AQI
    version: 1.0
    date: 2018/10/10
"""
import requests
import csv
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        返回URL的文本
    """
    url = "http://pm25.in/" + city_pinyin
    request = requests.get(url, timeout=30)
    soup = BeautifulSoup(request.text, "lxml")
    div_list = soup.find_all("div", {"class": "span1"})

    city_aqi_list = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find("div", {"class": "caption"}).text.strip()
        value = div_content.find("div", {"class": "value"}).text.strip()
        city_aqi_list.append((caption, value))
    return request.status_code, city_aqi_list


def get_all_city_aqi():
    """
        获取所有城市
    """
    url = "http://pm25.in/"
    city_list = []
    request = requests.get(url, timeout=30)
    soup = BeautifulSoup(request.text, "lxml")
    city_div = soup.find_all("div", {"class": "bottom"})[1]
    city_link_list = city_div.find_all("a")
    for city_link in city_link_list:
        city_name = city_link.text
        city_name_pinyin = city_link["href"][1:]
        city_list.append((city_name, city_name_pinyin))
    return request.status_code, city_list


def main():
    header = ["City"]
    request_code, city_list = get_all_city_aqi()
    if request_code == 200:
        # 显示表格抬头
        r_code, city_aqi_list = get_city_aqi(city_list[0][1])
        for city_aqi in city_aqi_list:
            header.append(city_aqi[0])

        print("一共有{}条记录\n".format(len(city_list)))
        with open("china_city_aqi.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for num, city in enumerate(city_list):
                r_code, city_aqi_list = get_city_aqi(city[1])
                row = []
                row += [city[0]]
                for city_aqi in city_aqi_list:
                    row += [city_aqi[1]]
                writer.writerow(row)
                if (num + 1) % 10 == 0:
                    print("已处理{}条记录......".format(num + 1))
                if num == len(city_list) - 1:
                    print("\n处理完成！")


if __name__ == '__main__':
    main()
