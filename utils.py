from pandas import DataFrame
def df_to_list(df: DataFrame) -> list:
    """dataframe to list
    :param srt: scrutinizer
    :return: scrunizer.data转换后的临时list
    """
    X = df.iloc[:, :]
    X = (X.values)
    return X.tolist()

def format_print(status: str, msg: str) -> None:
    """人性化的终端输出信息
    :param status: 状态
    :param msg: 信息
    """
    if status == "ERROR":
        print(f"\033[31m[{status}]\033[0m {msg}")
    elif status == "WARN":
        print(f"\033[33m[{status}]\033[0m {msg}")
    elif status == "INFO":
        print(f"\033[34m[{status}]\033[0m {msg}")


def common_preprocessing_filter(df: DataFrame) -> DataFrame:
    """过滤器：通用预处理过滤器
    :param df: DataFrame
    :return: 过滤处理后的数据对象
    """
    # TODO: 后面编写逻辑
    return fill_null(excel_row_padding(df))

def excel_row_padding(df: DataFrame) -> DataFrame:
    """过滤器：填补合并单元格空值
    :param df: DataFrame
    :return: 过滤处理后的数据对象
    """
    # TODO: 后面编写逻辑
    return df


def fill_null(df: DataFrame) -> DataFrame:
    """过滤器：填补以 / , '-- 代替的空值
    :param df: DataFrame
    :return: 过滤处理后的数据对象
    """
    # TODO: 后面编写逻辑
    return df