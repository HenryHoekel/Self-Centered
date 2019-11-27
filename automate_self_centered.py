from scrape       import scrape_all
from get_metadata import get_all_metadata
from jsonParse    import parse_json
import os

def clean_up_files(user):

    files_to_remove = [str(user) + '_short.json',
                       str(user) + '.json'      ,
                       str(user) + '.csv'       ,
                       str(user) + '.zip'       ]

    for _file in files_to_remove:

        if (os.path.exists(_file)):
            os.remove(_file)
        else:
            print(str(_file) + ' does not exist')

# end clean_up_files

def run_one_user(user, start_date, end_date):
    scrape_all(user, start_date, end_date)
    get_all_metadata(user)
    parse_json(user)
    clean_up_files(user)
# end run_one_user

def run_everything():
    # Put all Queries to be ran here
    run_one_user('Jumpman23', '01/01/2019', '01/03/2019')
    run_one_user('Adobe'    , '01/01/2019', '01/03/2019')
# end run_everything

run_everything()
