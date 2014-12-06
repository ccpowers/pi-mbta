""" Main file to run MBTA Nixie Tube clock """
from MBTAQuery import MBTAQuery
from MBTAStop import MBTAStop
import time

if __name__ == "__main__":
    import yaml
    with open('api-key.yaml', 'r') as f:
        keys = yaml.load(f)

    api_key = keys['mbta']

    stop = MBTAStop(2670, api_key)
    while True:
        time.sleep(15)
        stop.fetch_predictions()
        print stop
