from asyncio import exceptions
import pandas as pd
import sqlite3
from utils.echo import format_print


# 数据库连接句柄
class sqlite_db():
    def __init__(self, database_name: str) -> None:
        self.database_name = database_name
        try:
            self.connection = sqlite3.connect(database_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            format_print("ERROR", str(e))
            exit(2)

    def __del__(self) -> None:
        try:
            self.connection.close
        except sqlite3.Error as e:
            format_print("ERROR", str(e))


# 进行操作的数据对象
class scrutinizer():
    def __init__(self, db: str, sht_name: str, excel_path: str, skp_rows: int = 2) -> None:
        """scrutinizer构造函数
        :param db: 数据库名称
        :param sht_name: 表名(EXCEL & SQLITE)
        :param excel_path: EXCEL文件路径
        :param skp_rows: EXCEL文件跳过行数
        """
        self.db_name = db
        self.excel_name = excel_path
        self.sheet_name = sht_name
        try:
            self.data = pd.read_excel(excel_path, sheet_name=sht_name, skiprows=skp_rows)
        except exceptions as e:
            format_print("ERROR", str(e))
            exit(1)