import pandas as pd
import filter.test_results_chemical as test_results_chemical
from models import scrutinizer
from config import database
from query.test_results_compliance import get_table_data, calc_qualified_rate

# 测试数据库
# db_name = "test.db"
# db = pw.SqliteDatabase(db_name)


def __init__(self):
    database.connect()


def __del__(self):
    database.close()


def show_data(srt: scrutinizer) -> None:
    """临时展示测试数据
    :param data: 读取的EXCEL数据
    :param description: 自定义输出描述，默认为空
    :return: None
    """
    pd.set_option("display.max_columns", None)  # 显示所有列
    pd.set_option("display.max_rows", None)  # 显示所有行
    pd.set_option("display.width", None)  # 显示宽度是无限
    pd.set_option("display.unicode.east_asian_width", True)  # 显示时列对齐

    print("*" * 10 + " " + srt.sheet_name + " " + "*" * 10)
    print("data.columns= " + srt.data.columns)
    print("data.shape= ", srt.data.shape)
    print("sample= ", srt.data[0:4], sep="\n")
    print("#" * 40)
    print("\n\n")


if __name__ == "__main__":
    db_name = "test.db"

    test1_name = "检测结果-化学因素"
    chemical_test = scrutinizer(db_name, test1_name, "test/test.xlsx", 2)
    test_results_chemical.df_to_sql(database, chemical_test)

    print(calc_qualified_rate(get_table_data()))
