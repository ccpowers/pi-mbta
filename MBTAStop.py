from MBTAQuery import MBTAQuery
import json

class MBTAStop(object):
    """ Contains data about a specific bus stop. """
    def __init__(self, stop_id, api_key):
        """
        @param stop_id (int) : Unique identifier for this stop.
        """
        self.id = stop_id
        self.name = ''
        self.api_key = api_key
        #initialize possible queries
        self.predictions_query = MBTAQuery(self.api_key, 'predictionsbystop', {'format': 'json', 'stop': self.id})

        #dictionary of predictions by route
        self.predictions = {}

    def fetch_predictions(self):
        """ Fetch predictions for this stop from MBTA Server. """
        results = self.predictions_query.send()

        if not self.name:
            self.name = results['stop_name']

        for mode in results['mode']:
            for route in mode['route']:
                route_predictions = []
                for direction in route['direction']:
                    for trip in direction['trip']:
                        prediction = (trip['trip_headsign'], trip['pre_away'], trip['trip_id'])
                        route_predictions.append(prediction)
                self.predictions[route['route_name']] = route_predictions
                        
        return results

    def __str__(self):
        """ Print information about stop. """
        st = 'Stop: {} ({})\n'.format(self.name, self.id)
        for route, predictions in self.predictions.items():
            st += '\t{}:\n'.format(route)
            for prediction in predictions:
                st += '\t\t{} ({}) : {} seconds away\n'.format(prediction[0], prediction[2], prediction[1])
        return st
