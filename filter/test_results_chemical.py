from sqlite3 import IntegrityError
from models import scrutinizer, chemical
from utils import df_to_list, format_print
import peewee as pw


def df_to_sql(db: pw.Database, srt: scrutinizer) -> None:
    """将DataFrame数据写入SQL数据库
    :param db: 数据库连接对象
    :param srt: 数据对象
    :return: None
    """
    # 创建表格
    with db:
        db.create_tables([chemical])

    data = df_to_list(srt.data)
    # print(data)
    # chemicals = [chemical{db.database, unit_name=elem[0], post=elem[1], detection_point=elem[2],
    #                       detection_project=elem[3], contact_time=elem[4],
    #                       detection_value=elem[5], PC_STEL_MAC=elem[6], CTWA=elem[7],
    #                       PC_TWA=elem[8]} for elem in data]
    # print(chemicals)

    # chemicals = []
    # for elem in data:
    #     try:
    #         with db.atomic():
    #             print(elem)
    #             row = chemical.create(unit_name=elem[0], post=elem[1], detection_point=elem[2],
    #                       detection_project=elem[3], contact_time=elem[4],
    #                       detection_value=elem[5], PC_STEL_MAC=elem[6], CTWA=elem[7],
    #                       PC_TWA=elem[8]
    #             )
    #             chemicals.append(row)
    #     except IntegrityError:
    #         format_print("WARNING", "数据重复")
    # print(chemicals[0])

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

    # chemicals = [dict(zip(title, data[i])) for i in range(len(data))]
    # chemical.insert_many(chemicals).execute()
    chemical.insert_many(data, title)



def add_Pk(db: pw.Database, index_name: str, srt: scrutinizer, pk: str) -> None:
    """增加SQLITE表格中主键模板
    :param db: 数据库连接对象
    :param index_name: 主键名称
    :param srt: 数据对象
    :param pk: 主键
    """
    db.cursor.execute(
        "CREATE INDEX ':index_name' ON ':sheet_name' ':primary_key'",
        {
            "index_name": index_name,
            "sheet_name": srt.sheet_name,
            "primary_key": pk,
        },
    )


def add_test_results_chemical_PK(db: pw.Database, srt: scrutinizer) -> None:
    """后续操作：添加`检测结果-化学因素`表主键
    :param db: 数据库连接对象
    :param index_name: 主键名称
    :param srt: 数据对象
    :param pk: 主键元组
    :return: None
    """
    add_Pk(db, "post_idx", srt, "('岗位','检测点')")
    return
