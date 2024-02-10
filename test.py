import pandas as pd
import read_excel
import filter.df_to_sql


def show_data(data: pd.DataFrame, description: str = "") -> None:
    """ 临时展示测试数据
    :param data: 读取的EXCEL数据
    :param description: 自定义输出描述，默认为空
    :return: None
    """
    pd.set_option("display.max_columns", None)  # 显示所有列
    pd.set_option("display.max_rows", None)  # 显示所有行
    pd.set_option("display.width", None)  # 显示宽度是无限
    pd.set_option("display.unicode.east_asian_width", True)  # 显示时列对齐

    print('*' * 10 + ' ' + description + ' ' + '*' * 10)
    print('data.columns= ' + data.columns)
    print('data.shape= ', data.shape)
    print('sample= ', data[0:4], sep='\n')
    print('#' * 40)


if __name__ == "__main__":
    chemical_test = read_excel.get_test_results_chemical(
        "test/test.xlsx", "检测结果-化学因素", 2
    )
    # show_data(chemical_test, "化学因素实例测试数据")
    filter.df_to_sql.df_to_sql(chemical_test, "test.db", "检测结果-化学因素")