import sys
import urllib.parse
from urllib.request import urlopen
import json

class GeocodeQuery:
    def __init__(self, language=None, region=None):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?language={0}&region={1}&sensor=false'.format(language, region)
        self.jsonResponse = {}
            
    def get_geocode(self, addr):
        addr = urllib.parse.quote(addr)
        url = self.url + '&address={}'.format(addr)
        response = urlopen(url).read().decode('utf8')
        self.jsonResponse = json.loads(response)
        return self.jsonResponse
        
    def get_lat(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["geometry"]["location"]["lat"]

    def get_lng(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["geometry"]["location"]["lng"]
    
    def get_cuntry(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["address_components"][4]["long_name"]

    def get_area(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["address_components"][3]["long_name"]


if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print ('usage: geocodeQuery.py [reverse] [lat] [lng] [country/addr]')
        sys.exit(1)