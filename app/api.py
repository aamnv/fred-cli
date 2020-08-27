import os
import math
from datetime import datetime, timedelta
import fred

fred_api_key = os.environ.get('FRED_API_KEY')
fred.key(fred_api_key)

days_in_a_year = 365.25

def get_series_data(series, years=5):
    today = datetime.today().strftime('%Y-%m-%d')
    five_years_ago = (datetime.today() - timedelta(days=years*days_in_a_year)).strftime('%Y-%m-%d')

    api_call_result = fred.observations(
        series, observation_start=five_years_ago, observation_end=today
    )

    series_data = _unpack_series_data(series, api_call_result)

    return series_data


def get_series_metadata(series):
    api_call_result = fred.series(series)
    metadata = api_call_result['seriess'][0]
    metadata_dict = {
        'Table Info': ['Title:', 'Units:', 'Frequency:'],
        '': [metadata['title'], metadata['units'], metadata['frequency']]
    }

    return metadata_dict


def search_fred(search_string, page=1):
    results_per_page = 15

    api_call_result = fred.search(search_string)
    total_pages = math.ceil(api_call_result['count'] / results_per_page)

    upper_result_bound = page * results_per_page - 1
    lower_result_bound = upper_result_bound - results_per_page + 1

    search_results = api_call_result['seriess']
    page_results = search_results[lower_result_bound:upper_result_bound]

    page_data = _unpack_search_data(page_results)

    metadata = {
        'data': page_data,
        'total_pages': total_pages,
        'current_page': page
    }

    return metadata


def about_series(series):
    api_call_result = fred.series(series)
    series_metadata = api_call_result['seriess'][0]

    series_detail_dict = {
        'Series Info:': [
            'ID:', 'Title:', 'Obs. Start:', 'Obs. End:',
            'Frequency:', 'Units:', 'Seasonal Adjustment:',
            'Last Updated:'
        ],
        '': [
            series_metadata['id'], series_metadata['title'],
            series_metadata['observation_start'], series_metadata['observation_end'],
            series_metadata['frequency'], series_metadata['units'],
            series_metadata['seasonal_adjustment'], series_metadata['last_updated']
        ]
    }

    return series_detail_dict



def _unpack_search_data(search_results):
    result_dict = {
        'ID': [],
        'Title': [],
        'Units': [],
        'Freq.':  [],
    }

    for result in search_results:
        result_dict['ID'].append(result['id'])
        result_dict['Title'].append(result['title'][:35]) # limiting at 35 chars
        result_dict['Freq.'].append(result['frequency_short'][:35]) # limiting  at 35 chars
        result_dict['Units'].append(result['units_short'])

    return result_dict


def _unpack_series_data(series, data_dict):
    observations = data_dict['observations']
    result_dict = {
        'Period': [],
        series: []
    }

    for data_point in observations:
        result_dict['Period'].append(data_point['date'])
        result_dict[series].append(_make_float(data_point['value'], 2))

    return result_dict


def _make_float(text_number, round_to):
    float_unrounded = float(text_number)
    float_number = round(float_unrounded, round_to)

    return float_number


if __name__ == '__main__':
    print(search_fred('gross national product'))


