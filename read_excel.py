import pandas as pd

def get_test_results_chemical(path: str, sht_name: str, skp_rows: int = 2) -> pd.DataFrame:
    data = pd.read_excel(
        path, sheet_name=sht_name, skiprows=skp_rows
    )
    return data