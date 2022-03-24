import ssl
import traceback
import certifi
import geopy.geocoders
from geopy.geocoders import Nominatim
from geopy.location import Location

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent='Shark-Attack2', scheme='https', timeout=10)

# Create dict of gps coordinate request results to prevent duplicate requests
locationDict = {}


# Convert source data to gps location
def getGpsLocation(location: str, area: str, country: str) -> Location:
    for address in convertSourceDataToAddresses(location, area, country):
        location = sendGpsCoordinateRequest(address)
        if location is not None:
            return location
    return None


# Convert source data into list of possible address strings. Ordered from most specific, to least specific.
def convertSourceDataToAddresses(location: str, area: str, country: str) -> [str]:
    locationData = []
    if location is not None:
        locationData.append(location.strip())
    if area is not None:
        locationData.append(area.strip())
    if country is not None:
        locationData.append(country.strip())
    if not locationData or (len(locationData) == 1 and locationData[0] == country):
        return []
    locationData.append(', '.join(locationData))
    if (len(locationData) == 3):
        locationData.append(locationData[1] + ', ' + locationData[2])
    return locationData


# Get location based on addrss string
# https://stackoverflow.com/questions/5807195/how-to-get-coordinates-of-address-from-python
def sendGpsCoordinateRequest(address: str) -> geopy.location.Location:
    # Check if we have the result saved from a previous request
    if address in locationDict:
        return locationDict[address]
    try:
        print('Getting coordinates for: ' + address)
        location = geolocator.geocode(address, exactly_one=True)
        print(address + ' result: ' + str(location))

        # save result for future
        locationDict[address] = location
        return location
        # return geopy.location.Location(address='123 street', point='40.7081443,-74.4263388', raw='123 street')
    except Exception:
        print('failed getting location ' + address)
        traceback.print_exc()
        return None
