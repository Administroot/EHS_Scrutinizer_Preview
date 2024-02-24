from pandas import DataFrame, isnull
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


def general_preprocessing_filter(df: DataFrame, column: list) -> DataFrame:
    """过滤器：通用预处理过滤器
    :param df: DataFrame
    :param column: 需要进行padding操作的列号
    :return: 过滤处理后的数据对象
    """
    return fill_null(excel_row_padding(df, column))

def excel_row_padding(df: DataFrame, column: list) -> DataFrame:
    """过滤器：填补合并单元格空值
    :param df: DataFrame
    :param column: 需要进行padding操作的列号
    :return: 过滤处理后的数据对象
    """
    # 判断column中元素是否均为int
    for i in column:
        if not isinstance(i, int):
            format_print("ERROR", "FUNC excel_row_padding: column中元素必须为int类型")
            raise TypeError("column must be int")

    for j in column:
        for i in range(1, df.shape[0]):
            last_row_val = df.iloc[i - 1, j]
            this_row_val = df.iloc[i, j]
            if isnull(this_row_val):
                # print('(%d, %d)改为(%d, %d)值=%s' % (i, j, i-1, j, last_row_val))
                # 与上一行值相同
                df.iloc[i, j] = last_row_val

    # print(df)
    # print(df["unit_name"])
    return df


def fill_null(df: DataFrame) -> DataFrame:
    """过滤器：填补以 / , '-- 代替的空值
    :param df: DataFrame
    :return: 过滤处理后的数据对象
    """
    # df.replace("'--", nan).replace('/', nan)
    df.where(df != "/", inplace=True)
    df.where(df != "'--", inplace=True)
    return df

def add_sequence(df: DataFrame) -> DataFrame:
    """添加序列号
    :param df: DataFrame
    :return: 添加序列号后的数据对象
    """
    # df["序号"] = range(1, df.shape[0] + 1)
    df.insert(0, "序号", range(1, df.shape[0]+1))
    return df
