"""
    author: RealgodJJ
    function: Process Json or CSV
    version: 1.0
    date: 2018/10/6
"""

import json
import csv
import os


def process_json_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        city_list = json.load(file)
    print(city_list)


def process_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))


def main():
    file_path = input("请输入文件的名称：")
    file_name, file_ext = os.path.splitext(file_path)

    if file_ext == ".json":
        process_json_file(file_path)
    elif file_ext == ".csv":
        process_csv_file(file_path)
    else:
        print("暂不支持读取此类文件！")


if __name__ == '__main__':
    main()
