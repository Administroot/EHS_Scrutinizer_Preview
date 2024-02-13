from models import scrutinizer, chemical
from utils import df_to_list, general_preprocessing_filter
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

    # 调用通用预处理过滤器
    data = general_preprocessing_filter(srt.data, [0, 1, 2])
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

