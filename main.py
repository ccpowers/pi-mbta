""" Main file to run MBTA Nixie Tube clock """
from MBTAQuery import MBTAQuery

if __name__ == "__main__":
    import yaml
    with open('api-key.yaml', 'r') as f:
        keys = yaml.load(f)

    api_key = keys['mbta']
    query = 'predictionsbystop'
    parameters = {'format': 'json',
                  'stop' : '2670'}

    mbtaquery = MBTAQuery(api_key, query, parameters)
    response = mbtaquery.send()
    print response

    requests_per_day = 10000
    request_frequency = 1/10
