from tabulate import tabulate

def make_table(series_data):
    table = tabulate(series_data, headers='keys', tablefmt='github')

    return table


def make_data_table_footer(series_metadata):
    table = tabulate(series_metadata, headers='keys')

    return table