import requests, urllib
import simplejson

import pymongo
from pricemonster import settings
from pricemonster.utils.json import JSONDateEncoder
pricing = pymongo.Connection(settings.MONGODB).matrix.pricing

WEB_API_URL = "http://dingbats.ed:8888/api/v1"

class DataProvider(object):

    def __init__(self):
        self.headers = {'content-type': 'application/json'}
    
    def url(self):
        raise NotImplementedYet()
    
    def get(self, resource, **kwargs):
        if not resource:
            raise Exception("Resource is not provided.")
        if not "format" in kwargs:
            kwargs['format'] = "json"
        qstring = urllib.urlencode(kwargs)
        url = "%s/%s?%s" % (self.url(), resource, qstring)
        print url
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        result = simplejson.loads(r.content)
        return result

class WebApi(DataProvider):

    def url(self):
        return WEB_API_URL

def web_api(resource, **kwargs):    
    return WebApi().get(resource, **kwargs)

def get_pricing_retailers():

    products = pricing.find().distinct('retailer')
    return products


if __name__ == "__main__":
    retailers = web_api("pub/retailers/")['objects']
    r_dict =dict( (r['key'],r) for r in retailers)
    print r_dict

    pretailers = get_pricing_retailers()
    print pretailers

    notthere = {}

    for pr in pretailers:
        if pr in r_dict:
            print "%s exists as %s" % (pr, r_dict[pr])
        else:
            notthere[pr] = True
            print "%s doesn't exist" % (pr)

    for k in notthere.keys():
        print "%s" % (k)
