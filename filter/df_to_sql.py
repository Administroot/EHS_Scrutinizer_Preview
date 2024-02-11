from models import sqlite_db, scrutinizer


def df_to_sql(db: sqlite_db, srt: scrutinizer) -> None:
    """将DataFrame数据写入SQL数据库
    :param db: 数据库连接对象
    :param srt: 数据对象
    :return: None
    """

    # 将df转换为sql语句
    srt.data.to_sql(
        name=srt.sheet_name, con=db.connection, if_exists="replace", index=False
    )


def add_Pk(db: sqlite_db, index_name: str, srt: scrutinizer, pk: str) -> None:
    """增加SQLITE表格中主键模板
    :param db: 数据库连接对象
    :param index_name: 主键名称
    :param srt: 数据对象
    :param pk: 主键
    """
    # db.cursor.execute(
    #     "CREATE INDEX ':index_name' ON ':sheet_name' ':primary_key'",
    #     {
    #         "index_name": index_name,
    #         "sheet_name": srt.sheet_name,
    #         "primary_key": pk,
    #     },
    # )
    print("srt.sheet_name=", srt.sheet_name)
    db.cursor.execute(
        "CREATE INDEX ':index_name' ON ':sheet_name' ('岗位','检测点')",
        {
            "index_name": index_name,
            # TODO: using ORM sdk(Peewee)
            "sheet_name": srt.sheet_name,
        },
    )


def excel_row_padding(srt: scrutinizer) -> scrutinizer:
    """过滤器：填补合并单元格空值
    :param srt: 数据对象
    :return: 过滤处理后的数据对象
    """
    # TODO: 后面编写逻辑
    pass


def add_test_results_chemical_PK(db: sqlite_db, srt: scrutinizer) -> None:
    """后续操作：添加`检测结果-化学因素`表主键
    :param db: 数据库连接对象
    :param index_name: 主键名称
    :param srt: 数据对象
    :param pk: 主键元组
    :return: None
    """
    add_Pk(db, "post_idx", srt, "('岗位','检测点')")
    return
