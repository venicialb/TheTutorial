import pandas as pd


def fixed_dataset():
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        for file in Path ().glob("flightlist_*.csv.gz")
    )
return