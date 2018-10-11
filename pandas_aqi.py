"""
    author: RealgodJJ
    function: Web crawler for all city of AQI
    version: 1.0
    date: 2018/10/10
"""
import pandas as pd


def main():
    aqi_data = pd.read_csv("china_city_aqi.csv")

    print("===============文件基本信息如下===============")
    print(aqi_data.info())

    print("\n===============全国AQI排名top10===============")
    top10_cities = aqi_data[["City", "AQI"]].sort_values(by="AQI").head(10)
    print(top10_cities)
    top10_cities.to_csv("top10_cities_aqi.csv", index=False)

    print("\n===============全国AQI排名bottom10===============")
    bottom10_cities = aqi_data[["City", "AQI"]].sort_values(by="AQI", ascending=False).head(10)
    print(bottom10_cities)
    bottom10_cities.to_csv("bottom10_cities_aqi.csv", index=False)

    print("\n===============全国AQI统计===============")
    print("AQI最大值：" + str(aqi_data["AQI"].max()))
    print("AQI最小值：" + str(aqi_data["AQI"].min()))
    print("AQI平均值：" + str(aqi_data["AQI"].mean()))


if __name__ == '__main__':
    main()