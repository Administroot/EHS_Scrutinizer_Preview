import pandas as pd
from pandas.testing import assert_frame_equal
import pytest
import filter.test_results_chemical as test_results_chemical
from models import scrutinizer
from config import database
from query.test_results_compliance import get_df, get_table_data

# 测试数据库
db_name = "test.db"


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


def test_sampling_detection():
    ########## 写入数据 ###########
    test_name = "检测结果-化学因素"
    res_name = "检测结果达标情况一览表"

    chemical_test = scrutinizer(db_name, test_name, "test/test.xlsx", 2, "r")
    # 将数据写入sqlite数据库
    test_results_chemical.df_to_sql(database, chemical_test)
    ########## 写入数据结束 ###########

    # 获取sqlite数据库数据
    df = get_df(get_table_data())
    # print(df)

    # 实例化scrutinizer，写入EXCEL
    test_results_compliance = scrutinizer(
        db_name, res_name, "test/res.xlsx", 0, "w", df=df
    )
    show_data(test_results_compliance)

    # 检查是否与标准数据相匹配
    # 读取答案EXCEL数据
    ans_df = pd.read_excel("test/ans.xlsx", sheet_name=res_name)
    # 读取结果EXCEL数据
    res_df = pd.read_excel("test/res.xlsx", sheet_name=res_name)
    
    assert_frame_equal(res_df, ans_df)


if __name__ == "__main__":
    # pytest.main(["-s", "${0}"])
    pytest.main(["-s", "ehs_scrutinizer_test.py"])
