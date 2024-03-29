import googlemaps

print('Please replace API key for Google maps')
API_KEY=''

def getLatLng(place):
    '''
    References
    ----------
    https://github.com/googlemaps/google-maps-services-python
    '''
    gmaps = googlemaps.Client(key=API_KEY)
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    
    return {
        'lat': geocode_result[0]['geometry']['location']['lat'],
        'lng': geocode_result[0]['geometry']['location']['lng'],
        'metadata': geocode_result
    }
