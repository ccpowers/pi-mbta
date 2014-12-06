import json
import urllib2 as urllib

class MBTAQuery(object):
    """ Constructs query for MBTA webservices """
    query_format = "http://realtime.mbta.com/developer/api/v2/{}?api_key={}{}"
    def __init__(self, api_key, query, parameters = None):
        self.api_key = api_key
        self.query = query
        self.parameters = parameters

    def send(self):
        """ Send query, parse result """
        #YO BITCH THIS IS MORE COMPLICATED FOR PARAMETERS
        parameter_strings = "".join(["&{}={}".format(key, value) for (key, value) in self.parameters.items()])
        query_string = self.query_format.format(self.query, self.api_key, parameter_strings)
        print 'Sending {}'.format(query_string)
        try:
            response = json.load(urllib.urlopen(query_string))
        except Exception, e:
            print e
            response = ''
        return response

