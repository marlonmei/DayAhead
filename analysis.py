import pandas as pd


def find_consecutive_negative(prices: list) -> list:
    results = []
    work = []
    number_of_consecutive_negative_hours = 6

    for i in range(len(prices)):
        price = prices[i]
        if price < 0:
            work.append(None)
            if len(work) >= number_of_consecutive_negative_hours:
                work = [True for _ in range(len(work))]

        else:
            if (len(work) != 0) and (len(work) < number_of_consecutive_negative_hours):
                results.extend([False for _ in range(len(work))])
            else:
                results.extend([True for _ in range(len(work))])

            results.append(False)
            work = []

    if (len(work) != 0) and (len(work) < number_of_consecutive_negative_hours):
        results.extend([False for _ in range(len(work))])
    else:
        results.extend([True for _ in range(len(work))])

    return results


def create_time_series_features(data: pd.DataFrame) -> pd.DataFrame:
    data['hour'] = data.index.hour
    data['dayofweek'] = data.index.dayofweek
    data['quarter'] = data.index.quarter
    data['month'] = data.index.month
    data['year'] = data.index.year
    data['dayofyear'] = data.index.dayofyear
    data['dayofmonth'] = data.index.day
    data['weekofyear'] = data.index.isocalendar().week
    return data
