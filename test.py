import pandas as pd
import filter.df_to_sql as df_to_sql
from models import sqlite_db, scrutinizer

def show_data(srt: scrutinizer) -> None:
    """ 临时展示测试数据
    :param data: 读取的EXCEL数据
    :param description: 自定义输出描述，默认为空
    :return: None
    """
    pd.set_option("display.max_columns", None)  # 显示所有列
    pd.set_option("display.max_rows", None)  # 显示所有行
    pd.set_option("display.width", None)  # 显示宽度是无限
    pd.set_option("display.unicode.east_asian_width", True)  # 显示时列对齐

    print('*' * 10 + ' ' + srt.sheet_name + ' ' + '*' * 10)
    print('data.columns= ' + srt.data.columns)
    print('data.shape= ', srt.data.shape)
    print('sample= ', srt.data[0:4], sep='\n')
    print('#' * 40)
    print('\n\n')


if __name__ == "__main__":
    # 连接测试数据库
    test_db = "test.db"
    db = sqlite_db(test_db)

    test1_name = "检测结果-化学因素"
    chemical_test = scrutinizer(test_db, test1_name, "test/test.xlsx", 2)
    # show_data(chemical_test)
    df_to_sql.df_to_sql(db, chemical_test)
    df_to_sql.add_test_results_chemical_PK(db, chemical_test)