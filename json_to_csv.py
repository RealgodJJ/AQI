"""
    author: RealgodJJ
    function: JSON to CSV
    version: 1.0
    date: 2018/10/8
"""
import json
import csv


def process_json_file(file_path):
    """
        解码json文件
    :param file_path:
    :return: 文件路径
    """
    file = open(file_path, mode="r", encoding="utf-8")
    city_list = json.load(file)
    return city_list


def main():
    file_path = input("请输入json文件的名称：")
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    # 列名（表头）
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    file = open("aqi_csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    for line in lines:
        writer.writerow(line)
    file.close()


if __name__ == '__main__':
    main()
