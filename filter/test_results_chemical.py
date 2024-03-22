from models import scrutinizer, chemical
from utils import df_to_list, general_preprocessing_filter
from pandas import DataFrame
import peewee as pw


def df_to_sql(db: pw.Database, srt: scrutinizer) -> None:
    """将DataFrame数据写入SQL数据库
    :param db: 数据库连接对象
    :param srt: 数据对象
    :return: None
    """
    # 创建表格
    with db:
        # 删除已有表格，防止数据重复
        db.drop_tables([chemical])
        db.create_tables([chemical])

    # 调用过滤器（特定、通用）
    data = preprocessing_filter(srt.data, [0, 1, 2])
    # srt.data.ffill(axis=0)

    # dataframe -> list
    data = df_to_list(srt.data)

    # 表的标题
    title = [
        "unit_name",
        "post",
        "detection_point",
        "detection_project",
        "contact_time",
        "detection_value",
        "PC_STEL_MAC",
        "CTWA",
        "PC_TWA",
    ]

    # 数据写入Sqlite3数据库
    chemical.insert_many(data, title).execute()


########## 预处理过滤器 ###########
def preprocessing_filter(df: DataFrame, column: list):
    """预处理过滤器
    :param df: 数据对象
    :param column: 需要进行padding操作的列号 (FUNC utils.excel_row_padding)
    :return: DataFrame
    """
    # 特定过滤器
    data = check_contact_time(df)
    # 通用过滤器
    data = general_preprocessing_filter(data, column)
    return data


def check_contact_time(df: DataFrame) -> DataFrame:
    # TODO: 每个操作点的接害时间应当一致，如果不一致弹出警告让用户确认是否进行下一步
    pass
    return df
