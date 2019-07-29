from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def run(value, filter_field = None):
    if filter_field == None:
        reader = CSV_Manager("./articles.csv")
        articles = reader.get_csv_as_dicts()
        manipulator = Manipulator(articles)

        filtered = manipulator.filter_by(value)
        print(json.dumps(filtered, indent=2))
    else:
        reader = CSV_Manager("./articles.csv")
        articles = reader.get_csv_as_dicts()
        manipulator = Manipulator(articles)

        filtered = manipulator.filter_by(value, filter_field)
        print(json.dumps(filtered, indent=2))
    
def run_by_date(date):
    
# run("a2", "author")
# run("a1")