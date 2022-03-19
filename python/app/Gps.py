import ssl
import certifi
import geopy.geocoders

from geopy.geocoders import Nominatim
from geopy.location import Location

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent='Shark-Attack', scheme='https', timeout=10)


#Convert source data to gps location
def getGpsLocation(location: str, area: str, country: str) -> Location:
    locationIndicators = []
    if location is not None:
        locationIndicators.append(location)
    if area is not None:
        locationIndicators.append(area)
    if len(locationIndicators) == 0 or (len(locationIndicators) == 1 and locationIndicators[0] == country):
        return None

    allLocators = ', '.join(locationIndicators)
    return sendGpsCoordinateRequest(allLocators)


#Get location based on addrss string
# https://stackoverflow.com/questions/5807195/how-to-get-coordinates-of-address-from-python
def sendGpsCoordinateRequest(address: str) -> geopy.location.Location:
    try:
        print('Getting coordinates for: ' + address)
        # return geolocator.geocode(location, exactly_one=True)
        return geopy.location.Location(address='123 street', point='40.7081443,-74.4263388', raw='123 street')
    except Exception:
        print('failed getting location ' + address)
        return None