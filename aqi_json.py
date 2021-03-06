"""
    author: RealgodJJ
    function: AQI calculate with JSON
    version: 1.0
    date: 2018/10/5
"""
import json


def process_json_file(file_path):
    """
        解码json文件
    :param file_path: 文件路径
    :return:
    """
    file = open(file_path, mode="r", encoding="utf-8")
    city_list = json.load(file)
    file.close()
    return city_list


def main():
    file_path = input("请输入文件的名称：")
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]

    file = open("top5_aqi.json", mode="w", encoding="utf-8")
    json.dump(top5_list, file, ensure_ascii=False)
    file.close()


if __name__ == '__main__':
    main()
