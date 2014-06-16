#from pygeocoder import Geocoder
from googlegeocoder import GoogleGeocoder

import csv, time

addrfile = open('addr.csv', 'r')
stop_time_for_geocoder = 1 # old 0.25

#reader = csv.reader(addrfile)
#allRows = [row for row in reader]
geocoder = GoogleGeocoder()

#for address in allRows:

address = '"8th Ave & 21st St., New York, NY"'

#try:
search  = geocoder.get(str(address)[1:-1])
print search[0].formatted_address + "^" + str(search[0].geometry.location) + "^" + str(search[0].geometry.location_type)

#except:
	#print "bad address"

#time.sleep(stop_time_for_geocoder)


# location_type stores additional data about the specified location. The following values are currently supported:

# "ROOFTOP" indicates that the returned result is a precise geocode for which we have location information accurate down to street address precision.
# "RANGE_INTERPOLATED" indicates that the returned result reflects an approximation (usually on a road) interpolated between two precise points (such as intersections). Interpolated results are generally returned when rooftop geocodes are unavailable for a street address.
# "GEOMETRIC_CENTER" indicates that the returned result is the geometric center of a result such as a polyline (for example, a street) or polygon (region).
# "APPROXIMATE" indicates that the returned result is approximate.