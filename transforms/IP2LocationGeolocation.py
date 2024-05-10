from maltego_trx.maltego import UIM_TYPES
from maltego_trx.entities import IPAddress, Location
from maltego_trx.transform import DiscoverableTransform
from settings import ip2locationio_api_key_setting
from .credentials import API_KEY, FORMAT
import requests

class IP2LocationGeolocation(DiscoverableTransform):
    """
    Lookup Geolocation information for an IP address by using IP2Location.io API.
    """

    @classmethod
    def create_entities(cls, request, response):
        ip =  request.Value
        result = cls.query(ip)
        if result:
            georesult = response.addEntity(Location, result['city_name'] + ", " + result['region_name'] + ", " + result['country_code'])
            georesult.addProperty("country", value = result['country_name'])
            georesult.addProperty("countrycode", value = result['country_code'])
            georesult.addProperty("city", value = result['city_name'])
            georesult.addProperty("latitude", value = result['latitude'])
            georesult.addProperty("longitude", value = result['longitude'])
            georesult.addProperty("Zipcode", value = result['zip_code'])
            georesult.addProperty("Timezone", value = result['time_zone'])
            georesult.addProperty("ASN", value = result['asn'])
            georesult.addProperty("AS", value = result['as'])
            georesult.addProperty("Is Proxy", value = str(result['is_proxy']))
        else:
            response.addUIMessage("Unable to query the geolocation information for this IP.")
    
    @staticmethod
    def query(ip):
        if API_KEY:
            
            query = requests.get(
                f"https://api.ip2location.io/?key={API_KEY}&ip={ip}&source=maltego"
            )
        else:
            query = requests.get(
                f"https://api.ip2location.io/?ip={ip}&source=maltego"
            )
        record  = query.json()
        return record