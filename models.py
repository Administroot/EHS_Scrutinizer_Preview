import pandas as pd
from utils import format_print
from config import database, logger_level
import peewee as pw
import logging


# 进行操作的数据对象
class scrutinizer:
    def __init__(
        self, db: str, sht_name: str, excel_path: str, skp_rows: int = 2, choice: str = 'r',
          df: pd.DataFrame = pd.DataFrame()
    ) -> None:
        """scrutinizer构造函数
        :param db: 数据库名称
        :param sht_name: 表名(EXCEL & SQLITE)
        :param excel_path: EXCEL文件路径
        :param skp_rows: EXCEL文件跳过行数
        :param choice: r/w
        :param df: dataframe数据，默认为Dataframe()，读取时需要传参
        """
        self.db_name = db
        self.excel_name = excel_path
        self.sheet_name = sht_name
        self.skip_rows = skp_rows
        self.data = df

        if choice == 'r':
            self.read_excel()
        elif choice == 'w':
            self.write_excel()
        else:
            format_print("ERROR", "choice参数错误")

    def read_excel(self) -> None:
        """读取EXCEL"""
        try:
            self.data = pd.read_excel(
                self.excel_name, sheet_name=self.sheet_name, skiprows=self.skip_rows
            )
        except Exception as e:
            format_print("ERROR", str(e))
            exit(1)

    def write_excel(self) -> None:
        """将数据写入EXCEL"""
        try:
            self.data.to_excel(self.excel_name, sheet_name=self.sheet_name, index=False)
            # print(self.data)
        except Exception as e:
            format_print("ERROR", str(e))
            exit(1)


# 调试时调整logger等级
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logger_level)

    
class BaseModel(pw.Model):
    class Meta:
        database = database


# 数据结构：检测结果-化学因素表
class chemical(BaseModel):
    # TODO: GBZ 2.1后续对应标准值
    unit_name = pw.CharField()
    post = pw.CharField()
    # post = pw.ForeignKeyField("Post")
    detection_point = pw.CharField()
    # detection_point = pw.ForeignKeyField("DetectionPoint")
    detection_project = pw.CharField()
    contact_time = pw.FloatField()
    detection_value = pw.CharField()
    PC_STEL_MAC = pw.IntegerField(null=True)
    CTWA = pw.FloatField(null=True)
    PC_TWA = pw.IntegerField(null=True)

    class Meta:
        # primary_key = pw.CompositeKey('post', 'detection_point')
        primary_key = False
