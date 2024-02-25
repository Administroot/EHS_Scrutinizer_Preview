# 检测结果达标情况一览表
from peewee import fn, Case
from models import chemical
from utils import add_sequence
import pandas as pd


def get_table_data() -> pd.DataFrame:
    # 检测结果达标情况一览表SQL
    query = (
        chemical.select(
            chemical.detection_project,
            fn.count(chemical.detection_project).alias("detection_project_num"),
            fn.count(chemical.post).alias("detection_post_num"),
            fn.sum(Case(None, ((chemical.CTWA < chemical.PC_TWA, 1),))).alias(
                "qualified_points"
            ),
        )
        .group_by(chemical.detection_project)
        .order_by(chemical.detection_project)
    )

    rows = []
    for row in query:
        rows.append(
            {
                "检测项目": row.detection_project,
                "检测点位数": row.detection_project_num,
                "检测岗位数": row.detection_post_num,
                "合格点数": row.qualified_points,
            }
        )

    df = pd.DataFrame(rows)
    return df


def calc_qualified_rate(df: pd.DataFrame) -> pd.DataFrame:
    """计算合格率
    :param df: SQL查询结果
    :return: pd.DataFrame
    """
    # 添加一列序号
    df = add_sequence(df)
    # 计算合格率
    df["合格率"] = df["合格点数"] / df["检测点位数"]
    df["合格率"] = df["合格率"].apply(lambda x: format(x, ".1%"))
    return df

