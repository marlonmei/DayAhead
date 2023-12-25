import os
import pandas as pd
import glob

from analysis import find_consecutive_negative, create_time_series_features
from constants import COLS_MAPPING


def load_data(file_name) -> pd.DataFrame:
    data = pd.read_excel(file_name).iloc[1:]
    data.set_index('Datum (MEZ)', inplace=True)
    data = data.rename(columns=COLS_MAPPING)
    return data


if __name__ == '__main__':
    cwd = os.getcwd()
    data_path_raw = '/data/raw/'
    data_path_processed = '/data/processed/'
    path_raw = cwd + data_path_raw
    path_processed = cwd + data_path_processed
    file_format = '.xlsx'
    all_files = glob.glob(path_raw + "*" + file_format)

    data = pd.DataFrame()
    for file_name in all_files:
        yearly_data = load_data(file_name=file_name)
        data = pd.concat([data, yearly_data])

    data = create_time_series_features(data)
    data['EMA30'] = data['day_ahead_auction'].ewm(span=30).mean()
    data['EMA15'] = data['day_ahead_auction'].ewm(span=15).mean()
    data['is_six_consecutive_neg'] = find_consecutive_negative(data['day_ahead_auction'].to_list())
    data.to_excel(f'{path_processed}DayAheadAuction.xlsx')