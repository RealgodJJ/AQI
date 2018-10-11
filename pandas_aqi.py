"""
    author: RealgodJJ
    function: Web crawler for all city of AQI
    version: 1.0
    date: 2018/10/10
"""
import pandas as pd
import matplotlib.pyplot as plt

# 修改默认字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 解决负号的问题
plt.rcParams["axes.unicode_minus"] = False

def main():
    aqi_data = pd.read_csv("china_city_aqi.csv")

    print("===============文件基本信息如下===============")
    print(aqi_data.info())

    # 数据清洗（只保留AQI大于0的数据）
    clean_aqi_data = aqi_data[aqi_data["AQI"] > 0]

    print("\n===============全国AQI排名top10===============")
    top10_cities = clean_aqi_data[["City", "AQI"]].sort_values(by="AQI").head(10)
    print(top10_cities)
    top10_cities.to_csv("top10_cities_aqi.csv", index=False)

    print("\n===============全国AQI排名bottom10===============")
    bottom10_cities = clean_aqi_data[["City", "AQI"]].sort_values(by="AQI", ascending=False).head(10)
    print(bottom10_cities)
    bottom10_cities.to_csv("bottom10_cities_aqi.csv", index=False)

    print("\n===============全国AQI统计===============")
    max = "AQI最大值：" + str(clean_aqi_data["AQI"].max())
    min = "AQI最小值：" + str(clean_aqi_data["AQI"].min())
    mean = "AQI平均值：" + str(clean_aqi_data["AQI"].mean())
    print(max)
    print(min)
    print(mean)
    with open("china_city_aqi_statistics.txt", mode="w", encoding="utf-8", newline="") as file:
        file.write(max + "\n")
        file.write(min + "\n")
        file.write(mean)

    top50_cities = clean_aqi_data[["City", "AQI"]].sort_values(by="AQI").head(50)
    top50_cities.plot(kind="bar", x="City", y="AQI", title="空气质量TOP50", figsize=(20, 10))

    plt.savefig("top50_aqi.png")
    plt.show()

if __name__ == '__main__':
    main()
