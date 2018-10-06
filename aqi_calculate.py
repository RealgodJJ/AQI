"""
    author: RealgodJJ
    function: AQI calculate
    version: 1.0
    date: 2018/10/6
"""


def cal_pm_iAqi(pm_value):
    pass


def cal_co_iAqi(co_value):
    pass


def cal_aqi(param_list):
    pm_value = param_list[0]
    co_value = param_list[1]

    pm_iaqi = cal_pm_iAqi(pm_value)
    co_iaqi = cal_co_iAqi(co_value)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi


def main():
    print("请输入以下信息，用空格分隔")
    input_str = input("(1)PM2.5 (2)CO:")
    input_str.split(' ')
    pm_value = float(input_str[0])
    co_value = float(input_str[1])

    param_list = []
    param_list.append(pm_value)
    param_list.append(co_value)

    aqi_value = cal_aqi(param_list)
    print("空气质量指数为：{}".format(aqi_value))


if __name__ == '__main__':
    main()
