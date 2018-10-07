"""
    author: RealgodJJ
    function: AQI calculate
    version: 1.0
    date: 2018/10/6
"""


def cal_linear(iAqi_low, iAqi_high, bp_low, bp_high, cp):
    iAqi = (iAqi_high - iAqi_low) * (cp - bp_low) / (bp_high - bp_low) + iAqi_low
    return iAqi


def cal_pm_iAqi(pm_value):
    iAqi = 0
    if 0 <= pm_value < 35:
        iAqi = cal_linear(0, 50, 0, 35, pm_value)
    elif 35 <= pm_value < 75:
        iAqi = cal_linear(50, 100, 35, 75, pm_value)
    elif 75 <= pm_value < 115:
        iAqi = cal_linear(100, 150, 75, 115, pm_value)
    return iAqi


def cal_co_iAqi(co_value):
    iAqi = 0
    if 0 <= co_value < 2:
        iAqi = cal_linear(0, 2, 0, 35, co_value)
    elif 2 <= co_value < 4:
        iAqi = cal_linear(2, 4, 35, 75, co_value)
    elif 4 <= co_value < 14:
        iAqi = cal_linear(4, 14, 75, 115, co_value)
    return iAqi


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
