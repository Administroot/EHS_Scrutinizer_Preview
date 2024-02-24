import peewee as pw
import logging

# 数据库
DATABASE = "test.db"
database = pw.SqliteDatabase(DATABASE)

# 日志等级
logger_level = logging.WARNING
