import click

from app import api
from app import table

@click.group()
def fred():
    pass

@fred.command()
@click.argument('series_id', type=str)
@click.option(
    '-y', '--years', 'years', 
    default=5, type=int, show_default=True
)
def get(series_id, years):
    """Fetches a FRED series dataset based on user input."""

    data = api.get_series_data(series_id, years)
    metadata = api.get_series_metadata(series_id)

    click.clear()

    printable_table = table.make_table(data)
    printable_metadata = table.make_data_table_footer(metadata)

    click.echo(printable_table)
    click.echo()
    click.echo(printable_metadata)
    click.echo()

    pass


@fred.command()
@click.argument('search_term', nargs=-1, type=str)
def search(search_term):
    """Searches the FRED database using a user provided
    search term."""

    continue_search = True
    page_num = 1

    while continue_search:
        complete_search_term = ' '.join(search_term)
        metadata = api.search_fred(complete_search_term, page=page_num)

        data = metadata['data']
        current_page = metadata['current_page']
        total_pages = metadata['total_pages']
        
        click.clear()

        printable_table= table.make_table(data)

        click.echo(printable_table)
        click.echo()
        click.echo(f'Page: {current_page} / {total_pages} | next page (n), prev page (b), exit (e) ')
        click.echo()
        character_pressed = click.getchar()

        if character_pressed == 'n' and current_page != total_pages:
            page_num += 1
        
        elif character_pressed == 'b' and current_page != 1:
            page_num -= 1
        
        elif character_pressed == 'e':
            continue_search = False
        
        else:
            print('Incorrect input, please try again. Press any key to try again.')
            click.pause()

    pass


@fred.command()
@click.argument('series_id', type=str)
def about(series_id):
    """Gives more detail on a FRED series dataset
    given a series ID."""

    data = api.about_series(series_id)

    click.clear()

    printable_table = table.make_table(data)

    click.echo(printable_table)
    click.echo()

    pass



if __name__ == '__main__':
    fred()