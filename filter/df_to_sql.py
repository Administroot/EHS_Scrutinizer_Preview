import pandas as pd
import sqlite3


def df_to_sql(df: pd.DataFrame, database_name: str, table_name: str) -> None:
    """将DataFrame数据写入SQL数据库
    :param df: DataFrame数据
    :param database_name: SQL数据库名
    :param table_name: SQL表名
    :return: None
    """
    conn = sqlite3.connect(database_name)
    df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)
    conn.close()

def excel_row_padding(data: pd.DataFrame) -> pd.DataFrame:
    """填补合并单元格空值
    :param data: 原始数据
    :return: 填补后的数据
    """
    # TODO: 后面编写逻辑
    return data
